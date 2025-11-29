import os
import pandas as pd
import pytest
from pandas_US_election import calculate_fractions, plot_candidate_fractions

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "US-2016-primary.csv")

# Test cases for pandas_US_election.py
def test_only_selected_candidate_returned():
    candidate = 'Donald Trump'
    df, _ = calculate_fractions(csv_path, candidate)
    assert df['candidate'].nunique() == 1, "Should only return one candidate"
    assert df['candidate'].iloc[0] == candidate, "Returned candidate should match input"

# Test that fractions are calculated correctly
def test_state_fractions_sum_to_one():
    df, _ = calculate_fractions(csv_path, 'Donald Trump')

    merged = pd.read_csv(csv_path, sep=';')
    merged['candidate'] = merged['candidate'].str.strip()
    merged['state'] = merged['state'].str.strip()

    totals = merged.groupby(['state', 'candidate'])['votes'].sum().reset_index()
    state_totals = totals.groupby('state')['votes'].sum().reset_index()

    totals = pd.merge(totals, state_totals, on='state', suffixes=('_cand', '_state'))
    totals['fraction'] = totals['votes_cand'] / totals['votes_state']

    state_sums = totals.groupby('state')['fraction'].sum()

    assert state_sums.between(0.99, 1.01).all(), "Fractions per state should sum to ~1"

# Test that the plot function creates a file
def test_plot_saves_file(tmp_path):
    candidate = 'Donald Trump'

    df, script_folder = calculate_fractions(csv_path, candidate)
    
    plot_path = os.path.join(tmp_path, "candidate_fraction_plot.png")
    plot_candidate_fractions(df, candidate, script_folder=tmp_path)

    assert os.path.exists(plot_path), "Plot file was not created"