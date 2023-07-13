from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import FileResponse
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import string
import random

uri = "mongodb+srv://michaelsutu:cxgWzARj9HyQlOYj@cluster0.kgl30mi.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

app=FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def makeid(N):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))

def authKey(key):
    db = client['Users']
    collection = db['People']
    result = collection.update_one({"Key": key}, {"$inc": {"Calls": 1}})
    if result.modified_count > 0:
        return True
    else:
        return False

class Post(BaseModel):
    mrn:int
    problist: list # the format in the post should be as follows "title": ["atom", "btom", "ctom"],
    medlist: list
    medclist: list
    smkstatus:str
    bmi: Optional[float]    
    egfr: int
    egfr0: int
    hba1c: float
    pltcnt: int
    o2depend: Optional[str]
    albumin: Optional[float] = 5
    pth: Optional[float]
    inr: Optional[float] = 1
    PHQ2: Optional[int] = 0
   
@app.get("/")
def root():
    return FileResponse('index.html')

@app.get("/script.js")
def root():
    return FileResponse('script.js')

@app.get("/styles.css")
def root():
    return FileResponse('styles.css')

@app.get("/login")
def root(username: str, password: str):
    db = client['Users']
    collection = db['People']
    document = collection.find_one({
        "Username": username
    })
    if document:
        if document["Password"] == password:
            return document["userid"]
        else:
            return
    else:
        return

@app.get("/signup")
def root(username: str, password: str):
    db = client['Users']
    collection = db['People']
    newUserId = makeid(10)
    collection.insert_one({
        "Username": username,
        "Password": password,
        "userid": newUserId,
        "Key": makeid(10),
        "Calls": 0
    })
    return newUserId

@app.get("/get")
def root(userid: str):
    db = client['Users']
    collection = db['People']
    document = collection.find_one({
        "userid": userid
    })
    if document:
        return {
            "Key": document["Key"],
            "Calls": document["Calls"]
        }
    else:
        return

@app.post("/posts")
def create_posts(new_post: Post, key: str):
    if authKey(key):
        problist=new_post.problist
        medlist=new_post.medlist
        medclist=new_post.medclist
        egfr1=new_post.egfr
        egfr0=new_post.egfr0
        bmi=new_post.bmi
        mrn=new_post.mrn
        o2depend=new_post.o2depend
        bmi=new_post.bmi
        hba1c=new_post.hba1c
        diaglist=[]
        diaglist.append(problist)
        diaglist.append(medlist)
        return diaglist
    else:
        return "Authentication Error."

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)