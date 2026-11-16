# Depends():
# Is used to tell FastAPI that a function or class is a dependency that should be executed automatically and its return value injected into another function.
from fastapi import FastAPI,Header,Depends,HTTPException

app=FastAPI()

def tokenVerify(token:str=Header(None)):
    if token!="mytoken":
        raise HTTPException(
            status_code=401,
            detail="Unknown User"
        )
    return(
        "User Found Good To Go!!"
    )

@app.get("/")
def home(user=Depends(tokenVerify)):
    return{
        "Everything Is GOOD!"
    }