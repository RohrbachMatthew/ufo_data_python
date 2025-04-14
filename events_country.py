# This file shows all events per country
import matplotlib.pyplot as plt
import pandas as pd
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

    # convert to categorical data type
    df['country'] = df['country'].astype('category')

    # Group events by country
    events_per_country = df.groupby('country', observed=False).size().reset_index(name='Events_per_country')

    return events_per_country
    # Remove # to print
    # print(events_per_country)

# make bar plot
def country_bar_plot(events_per_country, save=False):

    # Size of plot
    plt.figure(figsize=(8, 12))

    # Seaborn creates the bar plot
    # x = horizontal, y = vertical, data= tells where to get the data from
    sns.barplot(x='country', y='Events_per_country', data=events_per_country)

    # X-Axis label
    plt.xlabel('Country')
    # Y-Axis label
    plt.ylabel('Events Per Country')
    # Title of plot
    plt.title('Number Of Events Reported Per Country')

    # if save for saving plot as .png
    if save:
        plt.savefig('events_per_country.png')

    else:
        plt.show()
