"""
This file is meant for temporal patterns worldwide
- Time analysis:
    - Total sightings for days of the month (1-31)
    - Total sightings for each day of the week

TODO:
    - Show the time of day when sightings occur more frequently
    - Seasonal trend of sightings

    TODO: ADD DAY OF MONTH PLOT
    TODO: DAY OF WEEK PLOT

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from create_df import fetch_data

# prepare and plot sightings per month day
def prepare_day_of_month():
    rows, columns = fetch_data()

    df = pd.DataFrame(rows, columns=columns)

    df.replace('', pd.NA, inplace=True)

    # Show total NA in datetime column (694)
    # print(df['datetime'].isna().sum())

    # Drop Na values
    df = df.dropna(subset=['datetime'])

    # Creates new column in same dataframe
    # Converts to a datetime object from datetime column
    # Extracts day from datetime (dt.day)
    # Set as int instead of float (.astype())
    df['day_of_month'] = pd.to_datetime(df['datetime']).dt.day.astype(int)

    # Group the data by number of sightings per days of the week
    day_of_month = df.groupby('day_of_month').size().reset_index(name='Per Day Month')

    return day_of_month

######### TODO: ADD DAY OF MONTH PLOT

def prepare_day_of_week():
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)
    df.replace('', pd.NA, inplace=True)
    df.dropna(subset=['datetime'])

    # dt.day captures year, month, and day, calculates day of the week and gets the name of the day
    df['day_of_week'] = pd.to_datetime(df['datetime']).dt.day_name()

    day_of_week = df.groupby('day_of_week').size().reset_index(name='Number per day')

    day_of_week = day_of_week.sort_values(by='Number per day')

    return day_of_week

# TODO: ADD DAY OF THE WEEK PLOT


# TODO: ADD TIME OF DAY
def prepare_time_day():
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)
    df.replace('', pd.NA, inplace=True)
    df.dropna(subset=['datetime'])

# Remove # to run functions individually
# prepare_day_of_month()
# prepare_day_of_week()