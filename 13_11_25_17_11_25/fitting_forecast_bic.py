import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "UK_Pop_1950_2025.csv")
df = pd.read_csv(csv_path)
df.columns = ['Year', 'Population']
df['Year'] = df['Year'].astype(float)
df['Population'] = df['Population'].astype(float)

train = df.iloc[:-10]
test = df.iloc[-10:]

x_train = train['Year'].values
y_train = train['Population'].values

x = df['Year'].values
y = df['Population'].values

N = len(x)
sigma = 0.025 * y #2.5% uncertaint

degrees = range(1, 12)
bic_values = []
chi2_values = []

for deg in degrees:
    coeffs = np.polyfit(x_train, y_train, deg)
    poly = np.poly1d(coeffs)
    y_pred = poly(x)

    chi2 = np.sum((y - y_pred)**2 / sigma**2)
    N_params = deg + 1
    BIC = chi2 + N_params * np.log(N)

    bic_values.append(BIC)
    chi2_values.append(chi2 / (N - N_params))

best_deg = degrees[np.argmin(bic_values)]
best_coeffs = np.polyfit(x_train, y_train, best_deg)
best_poly = np.poly1d(best_coeffs)

print(f"Best model degree (lowest BIC): {best_deg}")
plt.figure(figsize=(12,6))

plt.errorbar(
    x, y, yerr=sigma, fmt='o', markersize=4,
    color="tab:blue", ecolor="lightblue",
    capsize=2, label="Observed data with uncertainties"
)

x_fit = np.linspace(x.min(), x.max(), 500)
y_fit = best_poly(x_fit)

plt.plot(
    x_fit, y_fit, color="orange", linewidth=3,
    label=f"Best BIC polynomial (order {best_deg})"
)

fit_limit = x_train.max()
plt.axvline(
    x=fit_limit, color="black", linestyle="--",
    label=f"Fit limit ({int(fit_limit)})"
)

plt.title("Weighted Polynomial Model Selection", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population", fontsize=12)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

#refit with covariance matrix
best_coeffs, cov = np.polyfit(x_train, y_train, best_deg, cov=True)
best_poly = np.poly1d(best_coeffs)

param_uncertainties = np.sqrt(np.diag(cov))

print(f"\nBest polynomial degree = {best_deg}")
print("\nParameter estimates with uncertainties:")

for i, (c, u) in enumerate(zip(best_coeffs, param_uncertainties)):
    print(f"a{i} = {c:.4e} ± {u:.4e}")

x_fit = np.linspace(x.min(), x.max(), 500)
y_fit = best_poly(x_fit)
y_fit_unc = np.zeros_like(y_fit)

for i in range(len(best_coeffs)):
    y_fit_unc += (param_uncertainties[i] * x_fit**(best_deg - i))**2