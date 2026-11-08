import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

scaler          = joblib.load('scaler.pkl')
feature_columns = joblib.load('feature_columns.pkl')

def preprocess_data(age, sex, bmi, children, smoker, region):
    
    # Create a DataFrame with the input data
    data = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }])

    # Step 2 — recreate engineered features
    data['bmi_category'] = pd.cut(
        data['bmi'],
        bins=[0, 18.5, 25, 30, 100],
        labels=['underweight', 'normal', 'overweight', 'obese']
    )
    data['age_group'] = pd.cut(
        data['age'],
        bins=[0, 30, 45, 60, 100],
        labels=['young', 'adult', 'middle_age', 'senior']
    )
    data['smoker_bmi'] = data['bmi'] * (data['smoker'] == 'yes')

    # Step 3 — encode exactly like training
    data['sex']    = data['sex'].map({'female': 0, 'male': 1})
    data['smoker'] = data['smoker'].map({'yes': 1, 'no': 0})
    data = pd.get_dummies(data, columns=['region'], drop_first=True)
    data = pd.get_dummies(data, columns=['bmi_category', 'age_group'], drop_first=True)
    data = data.astype(int)

    # Step 4 — align columns (handles any missing dummy columns)
    data = data.reindex(columns=feature_columns, fill_value=0)

    # Step 5 — scale and predict
    data_scaled = scaler.transform(data)

    return data_scaled





    
    
    