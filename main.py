from fastapi import FastAPI
import json
app=FastAPI()

def data_load():
    with open('pat.json','r') as f:
        data=json.load(f)
    return data

@app.get('/view')
def view():
    data=data_load()
    return data

@app.get('/')
def hello():
    return {'message':'Swapnali'}

@app.get('/hello')
def demo():
    return {'demo':'Example'}