import pandas as pd
from .customdata import CustomData

def predict_new(data:CustomData, preprocessor, model)->dict:
    
    df = pd.DataFrame([data.model_dump()])

    df_processed = preprocessor.transform(df)
    
    prediction = model.predict(df_processed)
    prediction_Prob = model.predict_proba(df_processed)


    return {"prediction": bool(prediction[0]),
            "probability_of_churn": float(prediction_Prob[0][1])}