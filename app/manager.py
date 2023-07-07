from datetime import datetime
from venv import logger
from sqlalchemy.orm import Session
from models import Source
from schema import SourceSchema

def get_data_by_source_id(db: Session, source_id: int):
    try:
        _source = db.query(Source).filter(Source.source_id==source_id)
        return _source
    except Exception as e:
        logger.info("There isn't any source associated with this source_id {}".format(source_id))

def add_data(db: Session, source: SourceSchema):
    _source = Source(
        source = source.source,
        source_type = source.source_type,
        source_tag = source.source_tag,
        last_update_date = source.last_update_date,
        from_date = source.from_date,
        to_date = source.to_date
    )
    db.add(_source)
    db.commit()
    db.refresh(_source)
    return _source

def update_data(db: Session, source_id: int, from_date: datetime, to_date:datetime, last_update_date: datetime):
    _source = get_data_by_source_id(db=db, source_id=source_id)
    _source.from_date = from_date
    _source.to_date = to_date
    _source.last_update_date = last_update_date

    db.commit()
    db.refresh(_source)
    return _source

