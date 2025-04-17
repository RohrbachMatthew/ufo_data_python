"""
This file is meant for temporal patterns worldwide
- Time analysis:
    - Total sightings for days of the month (1-31)
    - Total sightings for each day of the week

TODO:
    - Show the time of day when sightings occur more frequently
    - Seasonal trend of sightings

    TODO: DAY OF WEEK PLOT
    TODO: Time of day plot
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

    # Creates new column in the same dataframe
    # Converts to a datetime object from datetime column
    # Extracts day from datetime (dt.day)
    # Set as int instead of float (.astype())
    df['day_of_month'] = pd.to_datetime(df['datetime']).dt.day.astype(int)

    # Group the data by number of sightings per days of the week
    day_of_month = df.groupby('day_of_month').size().reset_index(name='Per_Day_Month')

    return day_of_month

def day_of_month_bar(day_of_month, save=False):

    # size of plot
    plt.figure(figsize=(25, 10))

    # Seaborn creates the bar plot, ax is the seaborn generated plot object
    # x = horizontal, y = vertical, data= tells where to get the data from
    ax = sns.barplot(x='day_of_month', y='Per_Day_Month', data=day_of_month)

    # Get the positions of the bars
    bar_positions = ax.get_xticks()

    # add the labels on each bar
    for position, row in zip(bar_positions, day_of_month.iterrows()):
        index, row_data = row
        ax.annotate(f'{row_data['Per_Day_Month']}',
                    (position, 100),  # Lifts the numbers off the bottom of x-axis in plot
                    ha='center', va='bottom', fontsize=13, color='black')


    # x-axis label
    plt.xlabel('Day Of Month')
    # y-axis label
    plt.ylabel('Sightings total')
    # title
    plt.title('Total Per Day In Month For All Data')

    # Save plot option
    if save:
        plt.savefig('events_per_day_of_month')
    else:
        plt.show()


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

    # Convert to datetime
    df['datetime'] = pd.to_datetime(df['datetime'])
    # Extract hour (dt.hour)
    df['hour'] = df['datetime'].dt.hour
    # Convert time to 12-hour AM PM time format
    df['formatted_time'] = pd.to_datetime(df['hour'], format='%H').dt.strftime('%I %p')

    hourly_events = df.groupby('formatted_time').size().reset_index(name='event_count')
    hourly_events = hourly_events.sort_values(by='event_count')
    return hourly_events
    # Remove # to test print
    # print(hourly_events)

def time_day_line(hourly_events, save=False):
    plt.figure(figsize=(20, 10))
    ax = sns.barplot(x='formatted_time', y='event_count', data=hourly_events)

    # Get the positions of the bars
    bar_positions = ax.get_xticks()

    # add the labels on each bar
    for position, row in zip(bar_positions, hourly_events.iterrows()):
        index, row_data = row
        ax.annotate(f'{row_data['event_count']}',
                    (position, 100),  # Lifts the numbers off the bottom of x-axis in plot
                    ha='center', va='bottom', fontsize=13, color='black')

    plt.xlabel('Time of Day', fontsize=15)
    plt.ylabel('Total amount of Sightings', fontsize=28)
    plt.title('Amount of sightings per hour', fontsize=28)
    plt.xticks(rotation=45, fontsize=15)

    if save:
        plt.savefig('events_per_hour_plot')
    else:
        plt.show()

# Remove # to run functions individually

# EVENTS PER DAY IN MONTH (1-31)
#events_per_day = prepare_day_of_month()
#day_of_month_bar(events_per_day)

# EVENTS PER DAY OF WEEK (MON-SUN)
# events_per_day_week = prepare_day_of_week()

# EVENTS PER HOUR OF THE DAY (12-hour format)
# events_per_hour = prepare_time_day()
# time_day_line(events_per_hour)