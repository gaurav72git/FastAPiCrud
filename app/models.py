from app.database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Source(Base):
    __tablename__ = "source_details"

    source_id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    source_type = Column(String)
    source_tag = Column(String)
    last_update_date = Column(TIMESTAMP(timezone=True))
    from_date = Column(TIMESTAMP(timezone=True))
    to_date = Column(TIMESTAMP(timezone=True))
    frequencey = Column(String)

_source_ = Source()
