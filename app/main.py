
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from sqlalchemy import schema
from starlette.requests import Request
from model import Organization,Tenant
from database import engine,get_db
from schema import User
import model

model.Base.metadata.create_all(engine)

app=FastAPI()

@app.post('/createuser/')
def create_user(request:User,db:Session=Depends(get_db)):
    organization=Organization(id=request.organization_id,name=request.organization_name)
    tenant=Tenant(id=request.tenant_id,name=request.tenant_name,company_logo=request.tenant_company_logo)
    group=Group(id=request.group_id,name=request.group_name)
    role=Role(id=request.role_id,name=request.role_name(id=request.tenantuser_id,username=request.tenantuser_user_name,first_name=request.tenantuser_first_name,
    last_name=request.tenantuser_last_name,email=request.tenantuser_email)
    group_user=GroupUsers(id=request.)
    tenant_user=TenantUser(groupuser_id=request.groupuser_id,user_id=request.groupuser_user_id,group_id=request.group_id)
    db.add(organization)
    db.add(tenant)
    db.add(group)
    db.add(role)                                 
    db.add(tenant_user)
    db.commit()
    db.commit()
    db.commit()
    db.commit()
    db.commit()
    db.refresh(organization)
    db.refresh(tenant)
    db.refersh(group)
    # db.refresh(role)
    db.refresh(tenant_user)
    return {'msg':'data stored successfully'}




