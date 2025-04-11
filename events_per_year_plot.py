"""
This file prepares data, creates a bar plot for events per year and is grouped by each year

User can save the plot as an image or view the plot in a window
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from create_df import fetch_data


def prepare_data_year():
    # Use fetch_data function to get rows and columns
    rows, columns = fetch_data()

    # Convert fetched data to pandas dataframe
    df = pd.DataFrame(rows, columns=columns)

    # Check for null values (Shows 694 null values)
    # print(df['datetime'].isna().sum())

    # Drop null values
    df = df.dropna(subset=['datetime'])

    # Pandas extract all years from datetime column, set as int instead of float
    df['year'] = pd.to_datetime(df['datetime']).dt.year.astype(int)

    # Group events per year
    events_per_year = df.groupby('year').size().reset_index(name='Number_of_events')
    '''
    groups by year (df.groupby()) and counts how many times the same year appears(.size())
    turns year index into regular column(reset_index)
    adds new column to display count per year (name=)
    '''


    # Filter out results with less than 1 event per year
    events_per_year = events_per_year[events_per_year['Number_of_events'] > 100]
    '''
    Selecting specific rows from events_per_year
    selects the column 'Number_of_events' from [events_per_year (this filters while keeping structure)
    '''
    return events_per_year

# Test Print the data
# print(events_per_year)


# Make Bar Plot with data, Uses events_per_year as params
def bar_plot(events_per_year, save=False):
    # Sets size of plot
    plt.figure(figsize=(12, 8))

    # Seaborn creates the bar plot
    # x = horizontal, y = vertical, data= tells where to get the data from
    sns.barplot(x='year', y='Number_of_events', data=events_per_year)

    # Make x-axis label
    plt.xlabel('Year')
    # Make y-axis label
    plt.ylabel('Events per year')
    # Make Title of plot
    plt.title('Events per year with over 100 sightings')

    # Define the limits of the plot
    # Sets the highest value to 8,000 to ensure it scales right
    plt.ylim(0, 8000)

    # Rotates the labels 45 degrees to make them easier to read
    plt.xticks(rotation=85)

    if save:
        # Optional save plot as image (remove #'s to run)
        plt.savefig('events_per_year_over100_barplot.png')

    else:
        plt.show()
