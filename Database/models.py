from pydantic import BaseModel

class Story(BaseModel):
    tribe: str
    story: str
    story_title: str
