from fastapi import FastAPI,Path,HTTPException,Query
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

@app.get('/pat/{p_id}')
def get_data(p_id:str = Path(...,description='Ids of Patients in DB',example='P001')):
    data=data_load()
    if p_id in data:
        return data[p_id]
    raise HTTPException(status_code=404,detail='Patient not found')

@app.get('/sort')
def sorting(sort_by:str=Query(...,description='Sort by value'),order:str=Query('asc',description='Order by asc or desc')):
    data=data_load()
    default_value=['age']
    if sort_by not in default_value:
        raise HTTPException(status_code=404,detail="something went wrong")
    if order not in ['asc','desc']:
        raise HTTPException(status_code=404,detail="something went wrong")
    rev= True if order=='desc' else False
    order_value=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=rev)
    return order_value