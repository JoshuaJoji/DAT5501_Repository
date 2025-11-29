import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate vote fractions for a specific candidate by state
def calculate_fractions(filename='US-2016-primary.csv', candidate_name='Donald Trump'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, filename)

    df = pd.read_csv(csv_path, sep=';') #, dtype={'state': str, 'candidate': str, 'votes': int})
    df['candidate'] = df['candidate'].str.strip()
    df['state'] = df['state'].str.strip()# Remove leading/trailing spaces

    state_candidate_votes = df.groupby(['state', 'candidate'])['votes'].sum().reset_index() # Group by state and candidate to sum votes
    state_totals = state_candidate_votes.groupby('state')['votes'].sum().reset_index()
    state_totals = state_totals.rename(columns={'votes': 'total_votes'})

    merged = pd.merge(state_candidate_votes, state_totals, on='state')# Merge to get total votes per state
    merged['fraction'] = merged['votes'] / merged['total_votes']

    candidate_filter = merged[merged['candidate'] == candidate_name].sort_values('fraction', ascending=False)
    return candidate_filter, script_dir  

# Plotting function
def plot_candidate_fractions(candidate_filter, candidate_name, script_folder):
    """Plot fraction of votes by state for one candidate."""
    plt.figure(figsize=(20, 10))
    plt.bar(candidate_filter['state'], candidate_filter['fraction'], color='steelblue')
    plt.xticks(rotation=90, ha='right')
    plt.title(f'Fraction of Votes by State for {candidate_name}')
    plt.xlabel('State')
    plt.ylabel('Fraction of Votes')
    plt.tight_layout()

    output_path = os.path.join(script_folder, "candidate_fraction_plot.png")
    plt.savefig(output_path)
    plt.close()

    print(f"Plot saved to: {output_path}")

if __name__ == "__main__":
    candidate_name = 'Donald Trump'
    candidate_filter, script_dir = calculate_fractions('US-2016-primary.csv', candidate_name)
    plot_candidate_fractions(candidate_filter, candidate_name, script_dir)