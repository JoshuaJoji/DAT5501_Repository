import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

os.chdir(os.path.dirname(os.path.abspath(__file__)))
data = pd.read_csv("meat-consumption-vs-gdp-per-capita.csv")

countries = ["India", "United States"]
subset = data[data["Country"].isin(countries)].copy()#focus on years between 1990–2022
subset = subset[(subset["Year"] >= 1990) & (subset["Year"] <= 2022)]

subset["Year"] = pd.to_numeric(subset["Year"], errors="coerce")
subset["Meat_kg_per_person"] = pd.to_numeric(subset["Meat_kg_per_person"], errors="coerce")
subset["GDP_per_capita_PPP"] = pd.to_numeric(subset["GDP_per_capita_PPP"], errors="coerce")

#Line graphs: GDP and Meat Consumption over time
for country in countries:
    df = subset[subset["Country"] == country]

    fig, ax1 = plt.subplots(figsize=(8,5))
    ax1.plot(df["Year"], df["GDP_per_capita_PPP"], color="blue", label="GDP per Capita (PPP, $)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("GDP per Capita (PPP, $)", color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")

    ax2 = ax1.twinx()
    ax2.plot(df["Year"], df["Meat_kg_per_person"], color="red", linestyle="--", label="Meat Consumption (kg/person)")
    ax2.set_ylabel("Meat Consumption (kg/person/year)", color="red")
    ax2.tick_params(axis="y", labelcolor="red")

    plt.title(f"GDP per Capita and Meat Consumption — {country} (1990–2022)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

#Linear Regression and R2 values
for country in countries:
    df = subset[subset["Country"] == country].dropna(subset=["GDP_per_capita_PPP", "Meat_kg_per_person"])
    
    X = df[["GDP_per_capita_PPP"]]
    y = df["Meat_kg_per_person"]

    model = LinearRegression().fit(X, y)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)

    print(f"{country} — R²: {r2:.3f}")

#Scatter with regression line
for country in countries:
    df = subset[subset["Country"] == country]

    plt.figure(figsize=(7,5))
    sns.regplot(
        data=df,
        x="GDP_per_capita_PPP",
        y="Meat_kg_per_person",
        scatter_kws={"s":60, "alpha":0.7},
        line_kws={"color":"red"}
    )
    plt.title(f"Meat Consumption vs GDP per Capita — {country} (1990–2022)")
    plt.xlabel("GDP per Capita (PPP, $)")
    plt.ylabel("Meat Consumption (kg/person/year)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()