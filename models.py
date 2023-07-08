from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column
from sqlalchemy import TIMESTAMP

class Source(Base):

    __tablename__ = "source_table"

    source_id = Column(Integer, primary_key=True)
    source = Column(String(200), nullable=False)
    source_type = Column(String(20), nullable=False)
    source_tag = Column(String(10))
    last_update_date = Column(String, nullable=False)
    from_date = Column(String, nullable=False)
    to_date = Column(String, nullable=False)
    frequency = Column(String, default='')

    def __repr__(self):
        return f"source_id={self.source_id}, source={self.source}, source_type={self.source_type}, source_tag={self.source_tag}"


