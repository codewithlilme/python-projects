from fastapi import FastAPI
from models import Lesson
app = FastAPI()

@app.get("/")
def greet():
    return "Hello"

lessons = [ 
    Lesson(id=1,name="Lily",Lecturer="Maggy",fees=3000),
    Lesson(id=2,name="Mso",Lecturer="aggy",fees=300),
    Lesson(id=5,name="Lily",Lecturer="dan",fees=40)
]

#fetching all lessons
@app.get("/lessons")
def all_lessons():
    return lessons

#fetching lessons by id 
@app.get("/lesson/{id}")
def get_all_lessons(id:int):
    for Lesson in lessons:
        if Lesson.id == id:
            return Lesson
    return "product not found"  
  
#add a lesson
@app.post("/lesson")
def add_lesson(lesson:Lesson):
    lessons.append(lesson)
    return lesson