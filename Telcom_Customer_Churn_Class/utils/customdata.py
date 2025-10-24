from pydantic import BaseModel, field_validator, ValidationError
from typing import Literal

class CustomData(BaseModel):
    gender: Literal['Female', 'Male']
    seniorcitizen: Literal['No', 'Yes']
    partner: Literal['Yes', 'No']
    dependents: Literal['No', 'Yes']
    tenure: int
    phoneservice: Literal['No', 'Yes']
    multiplelines: Literal['No phone service', 'No', 'Yes']
    internetservice: Literal['DSL', 'Fiber optic', 'No']
    contract: Literal['Month-to-month', 'One year', 'Two year']
