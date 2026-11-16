from fastapi import FastAPI,Request
import time

app=FastAPI()

# My Middleware

# @app.middleware("http")
# async def myMiddleWare(request:Request,call_next):
#     print("Middleware Hit Ho gyia")
#     response=await call_next(request)
#     print("Responce Sent")
#     return response

# Log Middleware
@app.middleware("http")
async def logMiddle(request:Request,call_next):
    startTime=time.time()
    response=await call_next(request)
    processTime=time.time()-startTime
    print(f"Path: {request.url.path} | Process Time: {processTime}")

    return response