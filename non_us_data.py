# This file will be for non US data
# US has most of the data, looking for insights from other countries

import pandas as pd
import matplotlib as plt
import seaborn as sns
from pandas import DataFrame

from create_df import fetch_data

def prepare_month_non_us():
    rows, columns = fetch_data()
    df = DataFrame(rows, columns=columns)

    # Remove NA
    df.replace('', pd.NA, inplace=True)

    df = df.dropna(subset=['datetime'])

    df = df[df['country'] != 'us']

    df['month'] = pd.to_datetime(df['datetime']).dt.month.astype(int)

    months = df.groupby('month').size().reset_index(name='per_month')

    return months

def month_non_us_plot(month, save=False):
