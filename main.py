from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def home():
    return{
        "message":"Hello ji myself FastAPI"
    }