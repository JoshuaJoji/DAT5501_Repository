import pandas as pd
import matplotlib.pyplot as plt

def calculate_fractions(filename='US-2016-primary.csv', candidate_name='Donald Trump'):
    df = pd.read_csv(filename, sep=';')
    df['candidate'] = df['candidate'].str.strip()
    df['state'] = df['state'].str.strip()

    state_candidate_votes = df.groupby(['state', 'candidate'])['votes'].sum().reset_index()
    state_totals = state_candidate_votes.groupby('state')['votes'].sum().reset_index()
    state_totals = state_totals.rename(columns={'votes': 'total_votes'})

    merged = pd.merge(state_candidate_votes, state_totals, on='state')
    merged['fraction'] = merged['votes'] / merged['total_votes']

    candidate_filter = merged[merged['candidate'] == candidate_name].sort_values('fraction', ascending=False)
    return candidate_filter

def plot_candidate_fractions(candidate_filter, candidate_name):
    plt.figure(figsize=(20, 10))
    plt.bar(candidate_filter['state'], candidate_filter['fraction'], color='steelblue')
    plt.xticks(rotation=90, ha='right')
    plt.title(f'Fraction of Votes by State for {candidate_name}')
    plt.xlabel('State')
    plt.ylabel('Fraction of Votes')
    plt.tight_layout()
    plt.savefig('candidate_fraction_plot.png')#save


if __name__ == "__main__":
    candidate_name = 'Donald Trump'
    candidate_filter = calculate_fractions('US-2016-primary.csv', candidate_name)
    plot_candidate_fractions(candidate_filter, candidate_name)