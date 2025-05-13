from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import realestate

app= FastAPI(
    title="Switzerland Realestate ML Model",
    description="Realestate price prediction"
)

with open("C:/Users/90584/OneDrive/Desktop/Data Science/ml_pipeline/model.pkl","rb") as f:
    model=pickle.load(f)
    

@app.get("/")
def index():
    return " welcome to Switzerland's Realestate price prediction FastAPI "

@app.post("/predict")
def model_predict(realestate_obj:realestate):
    sample=pd.DataFrame({
        'type':[realestate_obj.type],
        'amenities':[realestate_obj.amenities], 
        'postcode':[realestate_obj.postcode], 
        'Area':[realestate_obj.Area],
        'living area':[realestate_obj.living_area],
        'surface of garden for houses':[realestate_obj.surface_of_garden_for_houses],
        'Building height':[realestate_obj.Building_height],
        'proprerty average height':[realestate_obj.proprerty_average_height],
        'number of floors':[realestate_obj.number_of_floors],
        'perimeter':[realestate_obj.perimeter],
       'age in years':[realestate_obj.age_in_years],
    })
    
    predicted_value=model.predict(sample)
    
    return "price is "+str(round(float(10**(predicted_value[0])),2))

    
