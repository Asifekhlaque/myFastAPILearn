from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


# class Users(BaseModel):
#     name:str
#     age:int



@app.get('/')
def home():
    return{
        "message":"Hello ji myself FastAPI"
    }

# About Route
@app.get('/about')
def about():
    return{
        "message":"Welcome to About"
    }

# Users Route
@app.get('/user')
def user():
    return{
        "user":{
            "Name":"Mohit",
            "Age":24,
            "Course":"BTech CS"
        }
    }

# Dynamic Route
# Path Parameters-> get spicific id from database
# Data Type -> It validating what you are passing In the parameters It can be integer It can be string or anything. That is basic validation.

'''
@app.get('/users/{userId}')
def users(userId:int):
    return{
        "userID":userId
    }
'''

# Query Parameters

@app.get('/users/')
# optional Parameter
def users(name: str=None):
    return{
        "Name":name
    }

@app.get('/product')
# default Parameter
def product(limit:int =10):
    return{
        "Limit":limit
    }

@app.get('/items')
def items(productName:str=None,price:int=0):
    return{
        "Product Name: ":productName,
        "Price: ":price
    }

# Request Body-> Request given by user to server as an input(Post Request)
'''
@app.post("/create-user")
def create_user(data:Users):
    return{
        "Message":"User Create",
        "data":data
    }
'''

# Pydantic

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/users-create")
def users_create(data:User):
    return data