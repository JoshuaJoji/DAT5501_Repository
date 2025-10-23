import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('US-2016-primary.csv', sep=';')

candidate_name = 'Donald Trump'
candidate_filter = df[df['candidate'].str.strip() == candidate_name]

state_votes = candidate_filter.groupby('state')['fraction_votes'].mean().reset_index()
state_votes = state_votes.sort_values('fraction_votes', ascending=False)

plt.figure(figsize=(10, 5))
plt.bar(state_votes['state'], state_votes['fraction_votes'], color='steelblue')

plt.title(f'Fraction of Votes by State for {candidate_name}')
plt.xlabel('State')
plt.ylabel('Fraction of Votes')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()