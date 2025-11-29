import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "E0.csv")
df = pd.read_csv(csv_path)

#df = pd.read_csv('E0.csv')
print(df.head())

# Feature Engineering
df["GoalDiff"] = df["FTHG"] - df["FTAG"]
df["Result"] = df["FTR"].map({"H": 1, "A": 0, "D": 0.5})#win=1,draw=0.5,loss=0

# Aggregate team statistics
home = df.groupby("HomeTeam")[["FTHG", "FTAG", "HS", "HST", "HC", "HF", "HY", "HR", "Result"]].mean()
away = df.groupby("AwayTeam")[["FTAG", "FTHG", "AS", "AST", "AC", "AF", "AY", "AR", "Result"]].mean()

# Rename columns to indicate home/away
home.columns = [col.replace("H","") + "_home" for col in home.columns]
away.columns = [col.replace("A","") + "_away" for col in away.columns]

# Combine home and away stats
team_stats = pd.concat([home,away], axis=1).fillna(0)
print(team_stats.head())

# Prepare data for modeling
points = (
    df.assign(
        HomePoints= df["FTR"].map({"H": 3, "D": 1, "A": 0}),
        AwayPoints= df["FTR"].map({"H": 0, "D": 1, "A": 3}),
    )
    .groupby("HomeTeam")[["HomePoints", "AwayPoints"]]
    .sum()
    .sum(axis=1)
    .reset_index(name="TotalPoints")
)

# Merge points with team stats
merged = pd.merge(points, team_stats, left_on="HomeTeam", right_index=True)

# Modeling
X = merged.drop(columns=["HomeTeam", "TotalPoints"])
y = merged["TotalPoints"]

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("R² score:", r2_score(y_test, y_pred))

# Predict total points
preds = model.predict(X)
merged["PredictedPoints"] = preds
predicted_table = merged[["HomeTeam", "TotalPoints", "PredictedPoints"]].sort_values(by="PredictedPoints", ascending=False)
print(predicted_table)

import matplotlib.pyplot as plt

# Visualize predicted standings
plt.figure(figsize=(10,6))
plt.barh(predicted_table["HomeTeam"], predicted_table["PredictedPoints"])
plt.gca().invert_yaxis()
plt.title("Predicted Premier League Standings")
plt.xlabel("Predicted Points")