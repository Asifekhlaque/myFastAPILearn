from fastapi import FastAPI

app=FastAPI()

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

