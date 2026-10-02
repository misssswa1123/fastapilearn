from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name:str
    age:int=Field(gt=0)
    email:EmailStr
    link:AnyUrl
    married:bool=False
    allergy:Optional[List[str]]=None
    contact:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,val):
        valid=['icici.com','sbi.in']

        dt=val.split('@')[-1]
        if dt not in valid:
            raise ValueError('Enter valid email Id')
        return val



def insert_data(p:Patient):
    print(p.name)
    print(p.age)
    print(p.allergy)
    print(p.contact)
    print(p.email)
    print(p.link)
    print(p.married)


info={'name':'smv','age':23,'email':'smv@sbi.in','link':'https://mail.google.com/mail/u/0/#all','allergy':['Milk','Fish'],'contact':{'add':'pune','pin':'413106'}}
p1=Patient(**info)

insert_data(p1)
