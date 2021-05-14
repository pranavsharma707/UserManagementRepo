
from pydantic import BaseModel,EmailStr


class User(BaseModel):
    organization_id:int
    organization_name:str
    tenant_id:int
    tenant_name:str
    tenant_company_logo:str
    group_id:int
    group_name:str
    role_id:int
    role_name:str
    tenantuser_id:int
    tenantuser_user_name:str
    tenantuser_first_name:str
    tenantuser_last_name:str
    tenantuser_email:str
    groupuser_id:int
    groupuser_user_id:int
    group_id:int
