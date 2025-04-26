# This file will be for making comparison plots between the US and non US data

import pandas as pd
import matplotlib.pyplot as plt

from create_df import fetch_data


def prepare_yearly_comparison():
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)
    df.replace('', pd.NA, inplace=True)
    # Drop NA in both to prevent error: Cannot convert non-finite values(NA or inf)to integer
    df = df.dropna(subset=['datetime', 'country'])

    # Extract Year from datetime column
    df['year'] = pd.to_datetime(df['datetime']).dt.year.astype(int)
    df = df[df['year'] > 1985]
    # Categorize into US and non-US
    df['region'] = df['country'].apply(lambda x: 'US' if x == 'us' else 'non-US')
    # Group by year and region then count references
    grouped_countries = df.groupby(['year', 'region']).size().reset_index(name='grouped')

    # Pivot for plotting (make US and Non US a column), simplifies making side-by-side bars on the plot
    # year becomes unique index values
    # region(us, non-US) becomes columns
    # adds values of grouped(cell values)
    # fills na values with 0.0
    pivot = grouped_countries.pivot(index='year', columns='region', values='grouped').fillna(0)

    #print(pivot)
    return pivot

def yearly_comparison_bar(pivot, save=False):
    pivot.plot(kind='bar', stacked=False, figsize=(8, 4), color=['blue', 'red'])

    plt.title("Yearly Comparison")
    plt.xlabel('year')
    plt.ylabel('Amount of Sightings')
    plt.legend(title='Region', labels=['United States', 'Non-Unite States'])
    # spacing is adjusted to avoid overlapping
    plt.tight_layout()

    if save:
        plt.savefig('plots\\us_world_compare_bar.png')
    plt.show()


data = prepare_yearly_comparison()
yearly_comparison_bar(data, save=True)
