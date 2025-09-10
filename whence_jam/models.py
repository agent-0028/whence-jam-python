"""Data models for whence-jam."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MusicRecommendation:
    """A music recommendation from a person."""
    
    song_title: str
    spotify_url: str
    recommended_by: str
    date_added: datetime
    id: Optional[int] = None