import axios from "axios";
export async function scoreTransaction(payload) {
  const {data}=await axios.post(`${process.env.ML_SERVICE_URL}/predict`,payload,{timeout:10000});
  return data;
}
