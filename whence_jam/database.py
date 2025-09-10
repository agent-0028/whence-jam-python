"""Database abstraction layer for whence-jam."""

from abc import ABC, abstractmethod
from typing import List
from .models import MusicRecommendation


class DatabaseInterface(ABC):
    """Abstract interface for database operations."""
    
    @abstractmethod
    def add_recommendation(self, recommendation: MusicRecommendation) -> None:
        """Add a music recommendation to the database."""
        pass
    
    @abstractmethod
    def get_all_recommendations(self) -> List[MusicRecommendation]:
        """Get all recommendations, sorted by date descending."""
        pass
    
    @abstractmethod
    def close(self) -> None:
        """Close database connection."""
        pass


class SQLiteDatabase(DatabaseInterface):
    """SQLite implementation of the database interface."""
    
    def __init__(self, db_path: str = "recommendations.db"):
        self.db_path = db_path
        # TODO: Implement SQLite connection and schema creation
    
    def add_recommendation(self, recommendation: MusicRecommendation) -> None:
        """Add a music recommendation to the SQLite database."""
        # TODO: Implement SQLite insertion
        pass
    
    def get_all_recommendations(self) -> List[MusicRecommendation]:
        """Get all recommendations from SQLite, sorted by date descending."""
        # TODO: Implement SQLite query
        return []
    
    def close(self) -> None:
        """Close SQLite database connection."""
        # TODO: Implement connection cleanup
        pass