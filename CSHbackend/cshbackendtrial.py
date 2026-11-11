from fastapi import FastAPI , APIRouter
from configurations import collection
from Database.schemas import share_story , allstories
from Database.models import Story

app = FastAPI()
router = APIRouter()


@router.get("/")
def get_all_stories():
    stories = list(collection.find({}))
    return allstories(stories)

@router.post("/story")
def share_story(tribe: str, story: str, title: str):
    # Logic to share the story for the specified tribe
    return {f"Story shared for {tribe} tribe."}


app.include_router(router)