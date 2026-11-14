import {Router} from "express";
import {analyze,list,getOne} from "../controllers/transactionController.js";
const router=Router();
router.post("/analyze",analyze);router.get("/",list);router.get("/:id",getOne);
export default router;
