import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample disaster dataset
data = {
    "Rainfall": [
        10, 15, 20, 25, 30,
        40, 50, 60, 70, 80,
        90, 100, 110, 120, 130
    ],

    "Water_Level": [
        10, 12, 15, 18, 20,
        25, 30, 35, 40, 45,
        50, 55, 60, 70, 80
    ],

    "Wind_Speed": [
        5, 6, 8, 10, 12,
        15, 18, 20, 22, 25,
        28, 30, 32, 35, 40
    ],

    "Risk": [
        "Low", "Low", "Low", "Low", "Low",
        "Medium", "Medium", "Medium", "Medium", "Medium",
        "High", "High", "High", "High", "High"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features
X = df[["Rainfall", "Water_Level", "Wind_Speed"]]

# Target
y = df["Risk"]

# Create Decision Tree
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X, y)

print("AI Model Trained Successfully!")


def predict_risk(rainfall, water_level, wind_speed):

    new_data = [[rainfall, water_level, wind_speed]]

    prediction = model.predict(new_data)[0]

    return prediction