from app.core.database import Base  # Importa o Base compartilhado
from sqlalchemy import Column, String, Text, DateTime, Integer, Boolean
from sqlalchemy.sql import func

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, unique=True)
    slug = Column(String(255), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=True, onupdate=func.now())
    is_published = Column(Boolean, default=False)
    author = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}', slug='{self.slug}', created_at='{self.created_at}')>"
