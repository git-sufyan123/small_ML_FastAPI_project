from fastapi import FastAPI,Path,HTTPException
from fastapi.responses import JSONResponse
from user_input_schema import data_validation
from preprocessor import preprocess_data
from predict import run_predictiction
import traceback

app = FastAPI()

@app.get("/")
def welcome():
    return "Medical Bill Prediction system api pls  use /docs for more information"

@app.post('/predict')
def predict(data:data_validation):

    user_input = {
        "age": data.age,
        "sex": data.sex,
        "bmi": data.bmi,
        "children": data.children,
        "smoker": data.smoker,
        "region": data.region
    }

    # Preprocess the input data
    preprocessed_data = preprocess_data(**user_input)

    # Make predictions using the preprocessed data
    try:
        prediction = run_predictiction(preprocessed_data)
        return JSONResponse(status_code=200, content={"your estimated medical bill is": float(prediction.round(2)[0])})
    except Exception as e:
        raise HTTPException(status_code=500, detail=traceback.format_exc())



