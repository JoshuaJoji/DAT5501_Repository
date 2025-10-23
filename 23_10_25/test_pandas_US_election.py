import os
import pandas as pd
import pytest
from pandas_US_election import calculate_fractions, plot_candidate_fractions


def test_only_selected_candidate_returned():
    candidate = 'Donald Trump'
    result = calculate_fractions('US-2016-primary.csv', candidate)
    assert result['candidate'].nunique() == 1, "Should only return one candidate"
    assert result['candidate'].iloc[0] == candidate, "Returned candidate should match input"


def test_state_fractions_sum_to_one():
    df = calculate_fractions('US-2016-primary.csv', 'Donald Trump')

    merged = pd.read_csv('US-2016-primary.csv', sep=';')
    merged['candidate'] = merged['candidate'].str.strip()
    merged['state'] = merged['state'].str.strip()
    totals = merged.groupby(['state', 'candidate'])['votes'].sum().reset_index()
    state_totals = totals.groupby('state')['votes'].sum().reset_index()
    totals = pd.merge(totals, state_totals, on='state')
    totals['fraction'] = totals['votes_x'] / totals['votes_y']
    
    state_sums = totals.groupby('state')['fraction'].sum()
    assert state_sums.between(0.99, 1.01).all(), "Fractions per state should sum to ~1"


def test_plot_saves_file(tmp_path):
    candidate = 'Donald Trump'
    df = calculate_fractions('US-2016-primary.csv', candidate)
    plot_candidate_fractions(df, candidate)
    assert os.path.exists("candidate_fraction_plot.png"), "Plot file was not created"   