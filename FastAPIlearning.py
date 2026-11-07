from fastapi import FastAPI
from models import Lesson
from database import session , engine
import databasemodels

app = FastAPI()

databasemodels.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return "Hello"

lessons = [ 
    Lesson(id=1,name="Lily",Lecturer="Maggy",fees=3000),
    Lesson(id=2,name="Mso",Lecturer="aggy",fees=300),
    Lesson(id=5,name="Lily",Lecturer="dan",fees=40)
]

def init_db():
    db = session()
    for lesson in lessons:
        db.add(databasemodels.Lesson(**lesson.model_dump()))
    db.commit()

init_db()

#fetching all lessons
@app.get("/lessons")
def get_all_lessons():
    #db = session()
    #db.query()
    return lessons

#fetching lessons by id 
@app.get("/lesson/{id}")
def get_lesson_by_id(id:int):
    for Lesson in lessons:
        if Lesson.id == id:
            return Lesson
    return "product not found"  
  
#add a lesson
@app.post("/lesson")
def add_lesson(lesson:Lesson):
    lessons.append(lesson)
    return lesson

#updating a lesson
@app.put("/lesson")
def update_lesson(id:int,lesson:Lesson):
    for i in range(len(lessons)):
        if lessons[i].id == id:
            lessons[i] = lesson
            return "Product updated successfully"
    return "Unable to update product."

#deleting lesson
@app.delete("/lesson")
def delete_lesson(id:int):
    for i in range(len(lessons)):
        if lessons[i].id == id:
            del lessons[i]
            return "Lesson successfully deleted"
    return "Lesson not found"

@app.get("/lesson/fees/{fees}")
def get_lesson_by_fees(fees:int):
    for Lesson in lessons:
        if Lesson.fees == fees:
            return Lesson
    return "Lesson not found"