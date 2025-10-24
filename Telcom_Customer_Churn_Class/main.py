from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from utils.interface import predict_new
from utils.config import APP_NAME, VERSION, SECRET_KEY_TOKEN, preprocessor, forest_model
from utils.customdata import CustomData


app = FastAPI(title=APP_NAME, version=VERSION)
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_methods=["*"],
   allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Welcome to the Telcom Customer Churn Prediction API"}



api_key_header = APIKeyHeader(name='X-API-Key')
async def verify_api_key(api_key: str=Depends(api_key_header)):
    if api_key != SECRET_KEY_TOKEN:
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return api_key


@app.post("/predict_churn")
async def predict_churn(customer_data: CustomData, api_key: str=Depends(verify_api_key)) -> dict:
    try:
        result = predict_new(data=customer_data, preprocessor=preprocessor, model=forest_model)
        return result
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))
