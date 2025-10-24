# Telcom Customer Churn Classification

End-to-end Telcom customer churn classification service. This project trains models to predict whether a customer will churn and exposes a FastAPI service to make predictions using the trained models.

Project layout
- [main.py](Telcom_Customer_Churn_Class/main.py) — FastAPI app entrypoint.
- [utils/__init__.py](Telcom_Customer_Churn_Class/utils/__init__.py)
- [`utils.config`](Telcom_Customer_Churn_Class/utils/config.py) — app configuration, model & preprocessor loading.
- [`utils.customdata.CustomData`](Telcom_Customer_Churn_Class/utils/customdata.py) — request schema / data class used by the API.
- [`utils.interface.predict_new`](Telcom_Customer_Churn_Class/utils/interface.py) — prediction helper that applies preprocessing and model inference.
- Models: [Telcom_Customer_Churn_Class/Models/](Telcom_Customer_Churn_Class/Models/) — saved models and preprocessor (joblib files).
- Dataset: [Telcom_Customer_Churn_Class/Dataset/Telco_Cusomer_Churn.csv](Telcom_Customer_Churn_Class/Dataset/Telco_Cusomer_Churn.csv)
- Environment example: [Telcom_Customer_Churn_Class/.env.example](Telcom_Customer_Churn_Class/.env.example)
- Requirements: [Telcom_Customer_Churn_Class/requierment.txt](Telcom_Customer_Churn_Class/requierment.txt)

### Prerequisites
1. Python 3.8+ installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # Unix/macOS
    ```

3. Install dependencies:

```bash
pip install -r Telcom_Customer_Churn_Class/requierment.txt
```

4. Configuration

Copy and edit env file:

```bash
copy Telcom_Customer_Churn_Class\.env.example Telcom_Customer_Churn_Class\.env
```
    Fill in any required values (e.g. SECRET_KEY_TOKEN).

### Running the API (recommended)  

1. Change directory into the project package (important to avoid import errors):
```bash
cd Telcom_Customer_Churn_Class
```

2. Start the server:

```bash
uvicorn main:app --reload
```
* If you run uvicorn from the repository root, use the package import form instead:

```bash
uvicorn Telcom_Customer_Churn_Class.main:app --reload
```
` Note: running from the package folder avoids common "No module named 'utils'" import errors.`

### API usage

* Open the interactive docs at: http://127.0.0.1:8000/docs after starting the server.

* The request body schema is implemented as `utils.customdata.CustomData`. Consult that file for exact fields and types.
* The prediction logic is implemented in `utils.interface.predict_new` and uses the preprocessor & models from `utils.config`.

Example request (replace fields with values matching CustomData)

```json
{
  "customerID": "0001-ABCD",
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes"
  // ... other fields per CustomData schema ...
}
```

cURL example (adjust fields to match CustomData schema):

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d @sample_input.json
```

#### Notes & troubleshooting

* If you see "ModuleNotFoundError: No module named 'utils'" when running uvicorn, run uvicorn from inside the `Telcom_Customer_Churn_Class` folder:

```bash
cd Telcom_Customer_Churn_Class
uvicorn main:app --reload
```

This ensures package-relative imports like `from .utils...` or module resolution for `utils` work as expected.

* Inspect model & preprocessor files in `Models` if you need to replace or retrain models.