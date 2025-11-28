import pandas as pd

df = pd.read_csv('E0.csv')
print(df.head())

df["GoalDiff"] = df["FTHG"] - df["FTAG"]
df["Result"] = df["FTR"].map({"H": 1, "A": 0, "D": 0.5})#win=1,draw=0.5,loss=0

home = df.groupby("HomeTeam")[["FTHG", "FTAG", "HS", "HST", "HC", "HF", "HY", "HR", "Result"]].mean()
away = df.groupby("AwayTeam")[["FTAG", "FTHG", "AS", "AST", "AC", "AF", "AY", "AR", "Result"]].mean()

home.columns = [col.replace("H","") + "_home" for col in home.columns]
away.columns = [col.replace("A","") + "_away" for col in away.columns]

team_stats = pd.concat([home,away], axis=1).fillna(0)
print(team_stats.head())

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

merged = pd.merge(points, team_stats, left_on="HomeTeam", right_index=True)

X = merged.drop(columns=["HomeTeam", "TotalPoints"])
y = merged["TotalPoints"]

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("R² score:", r2_score(y_test, y_pred))

preds = model.predict(X)
merged["PredictedPoints"] = preds
predicted_table = merged[["HomeTeam", "TotalPoints", "PredictedPoints"]].sort_values(by="PredictedPoints", ascending=False)
print(predicted_table)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.barh(predicted_table["HomeTeam"], predicted_table["PredictedPoints"])
plt.gca().invert_yaxis()
plt.title("Predicted Premier League Standings")
plt.xlabel("Predicted Points")