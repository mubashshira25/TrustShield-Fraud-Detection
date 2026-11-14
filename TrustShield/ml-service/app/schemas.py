from pydantic import BaseModel,Field
class TransactionInput(BaseModel):
 amount:float=Field(gt=0)
 country:str=Field(min_length=2,max_length=80)
 device:str=Field(default="known",pattern="^(known|new|emulator)$")
 ip_risk:float=Field(ge=0,le=100)
 account_age_days:int=Field(ge=0)
 failed_attempts:int=Field(ge=0)
