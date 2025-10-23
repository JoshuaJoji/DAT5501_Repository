import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('US-2016-primary.csv', sep=';')

df['candidate'] = df['candidate'].str.strip()
df['state'] = df['state'].str.strip()

state_candidate_votes = df.groupby(['state', 'candidate'])['votes'].sum().reset_index()

state_totals = state_candidate_votes.groupby('state')['votes'].sum().reset_index()
state_totals = state_totals.rename(columns={'votes': 'total_votes'})

merged = pd.merge(state_candidate_votes, state_totals, on='state')
merged['fraction'] = merged['votes'] / merged['total_votes']

candidate_name = 'Donald Trump'
candidate_filter = merged[merged['candidate'] == candidate_name]

candidate_filter = candidate_filter.sort_values('fraction', ascending=False)

plt.figure(figsize=(20, 10))
plt.bar(candidate_filter['state'], candidate_filter['fraction'], color='steelblue')
plt.xticks(rotation=90, ha='right')
plt.title(f'Fraction of Votes by State for {candidate_name}')
plt.xlabel('State')
plt.ylabel('Fraction of Votes')

plt.tight_layout()
plt.show()