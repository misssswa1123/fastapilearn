from fastapi import FastAPI,Path,HTTPException,Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Annotated,Literal,Optional
app=FastAPI()

class Patient(BaseModel):
    id:str
    name:str
    age:Annotated[int,Field(...,gt=0,lt=120,description='Enter age')]
    gender:Annotated[Literal['Male','Female','Other'],Field(...,description='Enter gender')]
    phone:str
    diagnosis:str
    doctor:str


class patient_update(BaseModel):
    name: Optional[str] = None
    age: Optional[Annotated[int, Field(gt=0, lt=120)]] = None
    gender: Optional[Literal['Male', 'Female', 'Other']] = None
    phone: Optional[str] = None
    diagnosis: Optional[str] = None
    doctor: Optional[str] = None

def data_load():
    with open('pat.json','r') as f:
        data=json.load(f)
    return data
def save_data(data):
    with open('pat.json','w') as f:
        json.dump(data,f)


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

@app.post('/create')
def create_pat(p:Patient):
    data=data_load()
    if p.id in data:
        raise HTTPException(status_code=400,detail="Value is already present!!")
    data[p.id]=p.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201,content={'message':'pat created successfully'})

@app.put('/update/{p_id}')
def update_info(p_id: str, pat_update: patient_update):
    data = data_load()

    if p_id not in data:
        raise HTTPException(
            status_code=404,
            detail='User not present'
        )

    existing_user_info = data[p_id]

    updated_patient_info = pat_update.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    existing_user_info.update(updated_patient_info)

    existing_user_info['id'] = p_id

    p_py_obj = Patient(**existing_user_info)

    data[p_id] = p_py_obj.model_dump(exclude={'id'})

    save_data(data)

    return {
        'message': 'Patient updated successfully',
        'patient': data[p_id]
    }

@app.delete('/delete/{p_id}')
def delete_patient(p_id:str):
    data=data_load()

    if p_id not in data:
        raise HTTPException(status_code=404,detail='user not present!!')

    del data[p_id]

    save_data(data)
    return JSONResponse(status_code=200,content={'message':'deleted successfully'})