from fastapi import FastAPI
import numpy as np
from .schemas import TransactionInput
from .model import MODEL,MODEL_VERSION
app=FastAPI(title="TrustShield ML Service",version="1.0.0")
DEMO_FLAGGED_COUNTRY_CODES={"XX","ZZ"}
@app.get("/health")
def health(): return {"status":"ok","model_version":MODEL_VERSION}
@app.post("/predict")
def predict(p:TransactionInput):
 new=int(p.device=="new"); emulator=int(p.device=="emulator"); country=int(p.country.upper() in DEMO_FLAGGED_COUNTRY_CODES)
 X=np.array([[p.amount,p.ip_risk,p.account_age_days,p.failed_attempts,new,emulator,country]])
 score=round(float(MODEL.predict_proba(X)[0][1])*100,1)
 band="HIGH" if score>=70 else "MEDIUM" if score>=40 else "LOW"
 decision="REVIEW" if score>=40 else "ALLOW"
 factors=[]
 if p.ip_risk>=65: factors.append({"feature":"IP reputation","impact":"increases risk","detail":f"IP risk indicator is {p.ip_risk}/100."})
 if p.amount>=500: factors.append({"feature":"Transaction amount","impact":"increases risk","detail":f"Amount is {p.amount:g}, above the demo threshold of 500."})
 if p.account_age_days<14: factors.append({"feature":"Account age","impact":"increases risk","detail":f"Account is only {p.account_age_days} days old."})
 if p.failed_attempts>=3: factors.append({"feature":"Failed attempts","impact":"increases risk","detail":f"There have been {p.failed_attempts} failed attempts."})
 if new: factors.append({"feature":"Device","impact":"increases risk","detail":"This device is new to the account."})
 if emulator: factors.append({"feature":"Device","impact":"increases risk","detail":"Device marked as emulator in this demo."})
 if country: factors.append({"feature":"Country code","impact":"increases risk","detail":"Demo-only country flag; not a real country risk classification."})
 if not factors: factors.append({"feature":"No prominent risk signal","impact":"neutral","detail":"No configured demo threshold was triggered."})
 return {"risk_score":score,"risk_band":band,"prediction":decision,"explanation":factors,"model_version":MODEL_VERSION}
