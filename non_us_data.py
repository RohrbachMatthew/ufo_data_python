# This file will be for non US data
# US has most of the data, looking for insights from other countries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from create_df import fetch_data

def prepare_month_non_us():
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)

    # Remove NA
    df.replace('', pd.NA, inplace=True)

    df = df.dropna(subset=['datetime'])

    df = df[df['country'] != 'us']

    df['month'] = pd.to_datetime(df['datetime']).dt.month.astype(int)

    months = df.groupby('month').size().reset_index(name='per_month')

    return months

def month_non_us_plot(months, save=False):

    # Size of plot
    plt.figure(figsize=(10, 8))

    sns.lineplot(x='month', y='per_month', data=months)

    plt.xlabel('Month', fontsize='16')
    plt.ylabel('Total Sightings', fontsize='16')
    plt.title('Total Sightings For Each Month\n (non-us)', fontsize='16')

    if save:
        plt.savefig('plots\\per_month_non_us')
    else:
        plt.show()

# month_data = prepare_month_non_us()
# month_non_us_plot(month_data)
