# Machine Learning & Deep Learning Examples

This repository contains end-to-end example projects for ML/DL experiments, notebooks, trained models and a small FastAPI service for Telcom customer churn prediction.

## Contents (high level)
- [TensorFlow.ipynb](TensorFlow.ipynb) — general TensorFlow notebook.
- [2_Car_price_Prediction/](2_Car_price_Prediction/) — car price regression notebook and dataset.
- [3_Malaria_Detection/](3_Malaria_Detection/) — malaria detection notebooks and trained model (.h5).
- [Telcom_Customer_Churn_Class/](Telcom_Customer_Churn_Class/) — packaged churn classification project (API, models, notebooks, dataset).

## Telcom Customer Churn Package
- API entrypoint: [Telcom_Customer_Churn_Class/main.py](Telcom_Customer_Churn_Class/main.py)
- Request schema: [`utils.customdata.CustomData`](Telcom_Customer_Churn_Class/utils/customdata.py)
- Prediction helper: [`utils.interface.predict_new`](Telcom_Customer_Churn_Class/utils/interface.py)
- Config & model loader: [`utils.config`](Telcom_Customer_Churn_Class/utils/config.py) — includes [`utils.config.APP_NAME`](Telcom_Customer_Churn_Class/utils/config.py), [`utils.config.VERSION`](Telcom_Customer_Churn_Class/utils/config.py), [`utils.config.SECRET_KEY_TOKEN`](Telcom_Customer_Churn_Class/utils/config.py), [`utils.config.preprocessor`](Telcom_Customer_Churn_Class/utils/config.py), [`utils.config.forest_model`](Telcom_Customer_Churn_Class/utils/config.py)
- Saved models & preprocessors: [Telcom_Customer_Churn_Class/Models/](Telcom_Customer_Churn_Class/Models/)
- Dataset: [Telcom_Customer_Churn_Class/Dataset/Telco_Cusomer_Churn.csv](Telcom_Customer_Churn_Class/Dataset/Telco_Cusomer_Churn.csv)
- Example notebooks: [Telcom_Customer_Churn_Class/notebooks/](Telcom_Customer_Churn_Class/notebooks/)
- Env example: [Telcom_Customer_Churn_Class/.env.example](Telcom_Customer_Churn_Class/.env.example)
- Requirements: [Telcom_Customer_Churn_Class/requierment.txt](Telcom_Customer_Churn_Class/requierment.txt)

