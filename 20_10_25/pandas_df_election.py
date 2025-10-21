import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("US-2016-primary.csv", sep=";")

#print(df.head())
#print(df.columns)

#Histogram of fraction votes
plt.figure(figsize=(6,5))
plt.hist(df['fraction_votes'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Fraction Votes in US 2016 Primary Elections')
plt.xlabel('Fraction of Votes')
plt.ylabel('Frequency')
plt.grid(True)

#Histogram grouped by party
plt.figure(figsize=(8,5))
for party in df['party'].unique():
    subset = df[df['party'] == party]
    plt.hist(subset['fraction_votes'], bins=20, alpha=0.5, label=party)

plt.title('Fraction of Votes by Party')
plt.xlabel('Fraction of Votes')
plt.ylabel('Frequency')
plt.legend()

plt.show(block=True)