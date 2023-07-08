
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
def get_source(source_id:int):
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
def create_source(_source:Source):
    """
    This Method is used to Create the New Source.
    example: 
    {
        "source_id": 2,
        "source": "flipkart",
        "source_type": "COD",
        "source_tag": "FK",
        "last_update_date": "2023-07-08 12:53",
        "from_date": "2023-07-08 12:59",
        "to_date": "2023-07-08 01:10",
        "frequency": "5M"
    }
    """
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
def update_source(source_id:int,_source:Source):
    """
    This Method is useful for updating the existing data.
    param1: source_id
    param2: from_date
    param3: to_date
    param4: last_update_date
    """
    update_source=db.query(models.Source).filter(models.Source.source_id==source_id).first()
    if update_source is not None:
        raise HTTPException(status_code=404,detail="Source does not exists")
    
    update_source.from_date=_source.from_date
    update_source.to_date=_source.to_date
    update_source.last_update_date=_source.last_update_date

    db.commit()

    return update_source

@app.get('/get_data_trigger/{source_id}',response_model=Source,status_code=status.HTTP_200_OK)
def get_data_triggered(source_id: int, _source: Source):
    """
    This Method is used to update from_date & To_date
    param1: source_id {for the source which you want to update from_date and to_date}
    param2: from_date
    param3: to_date
    """
    __source = db.query(models.Source).filter(models.Source.source_id == source_id).first()

    if __source is None:
        raise HTTPException(status_code=404, detail="Source does not exists for corrosponding {source_id}")

    __source.from_date = _source.from_date + _source.frequency
    __source.to_date = _source.to_date + _source.frequency

    db.commit()
    return __source
