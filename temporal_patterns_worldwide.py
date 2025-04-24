"""
This file is meant for temporal patterns worldwide
- Time analysis:
    - Total sightings for days of the month (1-31)
    - Total sightings for each day of the week

TODO:
    - Seasonal trend of sightings

    TODO: DAY OF WEEK PLOT
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from create_df import fetch_data

# For custom legend labels
import matplotlib.patches as mpatches

# Prepare and plot Sightings per month
def prepare_month():
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)

    # Remove NA
    df.replace('', pd.NA, inplace=True)

    df = df.dropna(subset=['datetime'])

    df['month'] = pd.to_datetime(df['datetime']).dt.month.astype(int)

    months = df.groupby('month').size().reset_index(name='per_month')

    return months

def month_plot(months, save=False):
    plt.figure(figsize=(10, 8))

    sns.lineplot(x='month', y='per_month', data=months)

    plt.xlabel('Month', fontsize='16')
    plt.ylabel('Total Sightings', fontsize='16')
    plt.title('Total Sightings For Each Month\n (World Wide)', fontsize='16')

    if save:
        plt.savefig('plots\\per_month_worldwide')
    else:
        plt.show()

# prepare and plot sightings per day in months
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

    # Function to determine color based on values
    def get_color(value):
        if value >= 5000:
            return "red"

        elif 3000 < value < 5000:
            return "yellow"

        elif 2000 < value < 3000:
            return "blue"

        else:
            return 'grey'
    colors = day_of_month['Per_Day_Month'].apply(get_color).to_list()

    # Seaborn creates the bar plot, ax is the seaborn generated plot object
    # x = horizontal, y = vertical, data= tells where to get the data from
    ax = sns.barplot(x='day_of_month', y='Per_Day_Month', data=day_of_month, hue='day_of_month', palette=colors)

    # Get the positions of the bars
    bar_positions = ax.get_xticks()

    # add the labels on each bar
    for position, row in zip(bar_positions, day_of_month.iterrows()):
        index, row_data = row
        ax.annotate(f'{row_data['Per_Day_Month']}',
                    (position, 100),  # Lifts the numbers off the bottom of x-axis in plot
                    ha='center', va='bottom', fontsize=13, color='black')

    # Define custom legend labels
    red_patch = mpatches.Patch(color='red', label='5000+ sightings')
    yellow_patch = mpatches.Patch(color='yellow', label='4000 - 5000 sightings')
    blue_patch = mpatches.Patch(color='blue', label='Less than 3000 sightings')
    grey_patch = mpatches.Patch(color='grey', label='Less than 2000 sightings')
    # Add the custom legend to the plot
    plt.legend(handles=[red_patch, yellow_patch, blue_patch, grey_patch], fontsize=20)

    # x-axis label
    plt.xlabel('Day Of The Month', fontsize=20)
    # y-axis label
    plt.ylabel('Total amount of Sightings', fontsize=25)
    # title
    plt.title('Total Sightings For The Day Number In All Months', fontsize=25)

    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    # Save plot option
    if save:
        plt.savefig('plots\\events_per_day_of_month')
    else:
        plt.show()

# Prep and plot day of the week
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
# TODO: make plot for day of week

# Events Per Hour of the Day
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

# Events per hour plot
def time_hourly_bar(hourly_events, save=False):
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
    plt.ylabel('Total Amount of Sightings', fontsize=28)
    plt.title('Amount of Sightings Rer Hour', fontsize=28)
    plt.xticks(rotation=45, fontsize=15)

    if save:
        plt.savefig('plots\\events_per_hour_plot')
    else:
        plt.show()

# Remove # to run functions individually

# EVENTS PER MONTH
# events_per_month = prepare_month()
# month_plot(events_per_month)

# EVENTS PER DAY IN MONTH (1-31)
#events_per_day = prepare_day_of_month()
#day_of_month_bar(events_per_day)

# EVENTS PER DAY OF WEEK (MON-SUN)
# events_per_day_week = prepare_day_of_week()

# EVENTS PER HOUR OF THE DAY (12-hour format)
#events_per_hour = prepare_time_day()
#time_hourly_bar(events_per_hour)