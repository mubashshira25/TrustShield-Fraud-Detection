import mongoose from "mongoose";
const schema = new mongoose.Schema({
  amount:{type:Number,required:true}, currency:{type:String,default:"USD"},
  country:{type:String,required:true}, device:{type:String,enum:["known","new","emulator"],default:"known"},
  ipRisk:{type:Number,required:true}, accountAgeDays:{type:Number,required:true}, failedAttempts:{type:Number,required:true},
  riskScore:{type:Number,required:true}, riskBand:{type:String,enum:["LOW","MEDIUM","HIGH"]},
  prediction:{type:String,enum:["REVIEW","ALLOW"]}, explanation:[{feature:String,impact:String,detail:String}],
  modelVersion:{type:String,default:"trustshield-demo-1.0"}
},{timestamps:true});
export default mongoose.model("Transaction",schema);
