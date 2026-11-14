import Transaction from "../models/Transaction.js";
import {scoreTransaction} from "../services/mlClient.js";

export async function analyze(req,res,next){
 try{
  const {amount,currency="USD",country,device="known",ipRisk,accountAgeDays,failedAttempts}=req.body;
  if(!country || !(Number(amount)>0) || !(Number(ipRisk)>=0 && Number(ipRisk)<=100) || !(Number(accountAgeDays)>=0) || !(Number(failedAttempts)>=0))
   return res.status(400).json({message:"Provide valid amount, country, IP risk (0–100), account age and failed attempts."});
  const result=await scoreTransaction({amount:Number(amount),country,device,ip_risk:Number(ipRisk),account_age_days:Number(accountAgeDays),failed_attempts:Number(failedAttempts)});
  const transaction=await Transaction.create({amount:Number(amount),currency,country,device,ipRisk:Number(ipRisk),accountAgeDays:Number(accountAgeDays),failedAttempts:Number(failedAttempts),riskScore:result.risk_score,riskBand:result.risk_band,prediction:result.prediction,explanation:result.explanation,modelVersion:result.model_version});
  res.status(201).json({transaction});
 }catch(e){if(e.code==="ECONNREFUSED" || e.code==="ECONNABORTED") return res.status(503).json({message:"ML service unavailable. Start the FastAPI service on port 8000."});next(e);}
}
export async function list(req,res,next){try{res.json({transactions:await Transaction.find().sort({createdAt:-1}).limit(100)});}catch(e){next(e);}}
export async function getOne(req,res,next){try{const transaction=await Transaction.findById(req.params.id);if(!transaction)return res.status(404).json({message:"Not found"});res.json({transaction});}catch(e){next(e);}}
