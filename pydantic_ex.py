from pydantic import BaseModel
from typing import List,Dict,Optional
class Patient(BaseModel):
    name:str
    age:int
    allergy:Optional[List[str]]=None
    contact:Dict[str,str]



def insert_data(p:Patient):
    print(p.name)
    print(p.age)
    print(p.allergy)
    print(p.contact)

info={'name':'smv','age':23,'allergy':['Milk','Fish'],'contact':{'add':'pune','pin':'413106'}}
p1=Patient(**info)

insert_data(p1)
