import joblib

model = joblib.load('model.pkl')

def run_predictiction(data):
    # Make predictions using the loaded model
    predictions = model.predict(data)
    return predictions