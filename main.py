from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def hello():
    return {'message':'Swapnali'}

@app.get('/hello')
def demo():
    return {'demo':'Example'}