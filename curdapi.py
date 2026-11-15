# CURD Opertation using List in TODO API

from fastapi import FastAPI

from pydantic import BaseModel

app=FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool


# Create
@app.post('/create-todos')
def createTodo(todo:Todo):
    todos.append(todo)
    return{
        "The data is added"
    }

# Read
@app.get('/todos')
def readTodos():
    return todos

# Read based on path params
@app.get("/todos/{todoid}")
def get_Todo(todoid:int):
    for todo in todos:
        if todo.id==todoid:
            return todo
    return {"Todo no found"}

# Update
@app.put("/todos/{todoid}")
def updateTodo(todoid:int,updateTodo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todoid:
            todos[index]=updateTodo
            return{
                "Data updated"
            }
    return{
        "No data found"
    }


# Delete

@app.delete("/todos/{todoid}")
def updateTodo(todoid:int,updateTodo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todoid:
            todos.pop(index)
            return{
                "Data Deleted"
            }
    return{
        "No data found"
    }