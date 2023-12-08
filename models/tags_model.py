import uuid
from sqlalchemy import Column, String, UUID, Integer
from sqlalchemy.orm import relationship
from database.database import Base


class Tag(Base):
    __tablename__ = "tags"

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), unique=True, index=True)

