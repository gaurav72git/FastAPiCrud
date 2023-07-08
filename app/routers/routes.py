from datetime import datetime
from uuid import uuid4
from app import models, schemas
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Request, status, APIRouter, Response
from database import get_db
from app import manager
from app.models import _source_

router = APIRouter()

@router.post('/add_data', status_code=status.HTTP_201_CREATED, response_model=schemas.SourceCreatedResponse)
def add_data(_source: schemas.SourceSchema ,source: str, source_tag: str, source_type: str,
              from_date: datetime, to_date: datetime, last_update_date: datetime, db: Session = Depends(get_db)):
    _source.source_id =str(uuid4())
    _source.source = source
    _source.source_tag = source_tag
    _source.source_type = source_type
    _source.from_date = from_date
    _source.to_date = to_date
    _source.last_update_date = last_update_date
    _source.frequencey = str(datetime.timestamp(to_date) - datetime.timestamp(from_date))

    db.add(_source)
    db.commit()
    db.refresh(_source)

    return _source


@router.get('/get_data/{source_id}', status_code=status.HTTP_200_OK, response_model=schemas.ListSources)
def get_data(source_id: str, db: Session = Depends(get_db)):

    source_searched = db.query(models.Source).filter(models.Source.source_id == source_id)
    if not source_searched:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No source with this id: {source_id} found")
    return source_searched


@router.get('/get_data_trigger', status_code=status.HTTP_200_OK, response_model=schemas.UpdatedSourceResponse)
def get_data_trigger(source_id: str(uuid4()), db: Session = Depends(get_db)):
    source_data = db.query(models.Source).filter(models.Source.source_id == source_id)
    source_data.from_date += source_data.frequencey
    source_data.to_date += source_data.frequency

    db.add(source_data)
    db.commit()
    db.refresh(source_data)
    return source_data


@router.put('/update_data/{id}', status_code=status.HTTP_200_OK, response_model=schemas.SourceCreatedResponse)
def update_data(source_id, from_date, to_date, last_update_date, db:Session = Depends(get_db)):
    source_data = db.query(models.Source).filter(models.Source.source_id == source_id)
    if not source_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"NO source Exist for the corrosponding {source_id}")
    source_data.from_date = from_date
    source_data.to_date = to_date
    source_data.last_update_date = last_update_date

    db.add(source_data)
    db.commit()
    db.refresh(source_data)

    return source_data