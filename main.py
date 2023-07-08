
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models
from datetime import datetime
from sqlalchemy import TIMESTAMP

app=FastAPI()

class Source(BaseModel):
    source_id : int
    source : str
    source_type : str
    source_tag : str
    last_update_date : str
    from_date : str
    to_date : str
    frequency : str


    class Config:
        from_attributes=True


db=SessionLocal()


@app.get('/get_data/{source_id}',response_model=Source,status_code=status.HTTP_200_OK)
def get_an_item(source_id:int):
    """
    This Method will provide the source corrosponding to the 
    source_id.
    """
    source=db.query(models.Source).filter(models.Source.source_id==source_id).first()
    if source is None:
        return f"No source"
        
    return source

@app.post('/add_data',response_model=Source,
        status_code=status.HTTP_201_CREATED)
def create_an_item(_source:Source):
    db_source=db.query(models.Source).filter(models.Source.source==_source.source).first()

    if db_source is not None:
        raise HTTPException(status_code=400,detail="Source already exists")

    response = {
        'data': None
    }
    err = []
    if _source.source_tag is None:
        err.append('source_tag is mising')

    
    if len(err):
        response.data = None
        response.error = err
        return response

    new_source=models.Source(
        source=_source.source,
        source_type=_source.source_type,
        source_tag = _source.source_tag,
        last_update_date = _source.last_update_date,
        from_date = _source.from_date,
        to_date = _source.to_date,
        frequency = _source.frequency
    )


    db.add(new_source)
    db.commit()
    db.refresh(new_source)
    response['data'] = new_source

    return response

@app.put('/update_data/{source_id}',response_model=Source,status_code=status.HTTP_200_OK)
def update_an_item(source_id:int,_source:Source):
    update_source=db.query(models.Source).filter(models.Source.source_id==source_id).first()
    update_source.from_date=_source.from_date
    update_source.to_date=_source.to_date
    update_source.last_update_date=_source.last_update_date

    db.commit()

    return update_source

@app.get('/get_data_trigger/{source_id}',response_model=Source,status_code=status.HTTP_200_OK)
def get_data_triggered(source_id: int, _source: Source):
    __source = db.query(models.Source).filter(models.Source.source_id == source_id).first()
    __source.from_date = _source.from_date + _source.frequency
    __source.to_date = _source.to_date + _source.frequency

    db.commit()
    return __source
