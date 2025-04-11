# This file shows all events per country

import pandas as pd
import matplotlib
import seaborn as sns
from create_df import fetch_data

def prepare_data_country():
    # Fetch the data and convert to dataframe
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)

    # Replace blank values with NA
    df.replace('', pd.NA, inplace=True)

# remove ''' around code below to print out the dataframe
    '''
    pd.set_option('display.max_columns', None)  # Display all columns
    pd.set_option('display.expand_frame_repr', None)  # Prevents wrap around
    print(df)
    '''

    # remove # to print the total of null values (9670)
    # print(df['country'].isna().sum())

    # Drop NA values in country column
    df = df.dropna(subset=['country'])

    df['country'] = df['country'].astype('category')

    # Group events by country
    events_per_country = df.groupby('country').size().reset_index(name='Events_per_country')

    return events_per_country
    # Remove # to print
    # print(events_per_country)

# make bar plot
def country_bar_plot():

    # Size of plot

    # Seaborn creates the bar plot
    # x = horizontal, y = vertical, data= tells where to get the data from

    # X-Axis label

    # Y-Axis label

    # Title of plot

    # if save to save plot as .png

prepare_data_country()
