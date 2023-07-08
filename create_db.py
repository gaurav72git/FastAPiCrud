from database import Base,engine
from models import Source

print("Creating database ....")

Base.metadata.create_all(engine)