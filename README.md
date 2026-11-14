# TrustShield — Explainable Payment Fraud Detection

Standalone portfolio project: React + Vite, Node.js + Express, MongoDB, and a Python FastAPI/scikit-learn scoring service.

## Requirements
Node.js LTS, Python 3.10+, Docker Desktop, VS Code recommended.

## Run MongoDB
From this folder:
```bash
docker compose up -d
docker compose ps
```

## Run ML service (Terminal 1)
```bash
cd ml-service
python -m venv .venv
```
PowerShell: `.venv\\Scripts\\Activate.ps1`
Command Prompt: `.venv\\Scripts\\activate.bat`
macOS/Linux: `source .venv/bin/activate`
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
Health: http://localhost:8000/health

## Run backend (Terminal 2)
```bash
cd server
```
PowerShell: `Copy-Item .env.example .env`
Command Prompt: `copy .env.example .env`
```bash
npm install
npm run dev
```
Health: http://localhost:5002/api/health

## Run frontend (Terminal 3)
```bash
cd client
```
PowerShell: `Copy-Item .env.example .env`
Command Prompt: `copy .env.example .env`
```bash
npm install
npm run dev
```
Open http://localhost:5174

## Demo
Submit a transaction in the dashboard. The Express API sends its features to FastAPI, receives a risk score and explanation, and stores the result in MongoDB. Review recent transactions in the dashboard.

## API
- GET `/api/health`
- POST `/api/v1/transactions/analyze`
- GET `/api/v1/transactions`
- GET `/api/v1/transactions/:id`
- ML: GET `/health`, POST `/predict`

## Notes
The model is trained at startup on synthetic demonstration data. It is not a validated production fraud model and must not be used to approve or decline real payments. Do not enter real customer or payment data.
