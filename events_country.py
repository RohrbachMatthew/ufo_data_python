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
    df['country'] = df['country'].str.upper()

    # Group events by country
    events_per_country = df.groupby('country', observed=False).size().reset_index(name='Events_per_country')

    return events_per_country
    # Remove # to print
    # print(events_per_country)

# make bar plot
def country_bar_plot(events_per_country, save=False):

    # Size of plot
    plt.figure(figsize=(8, 8))

    # Seaborn creates the bar plot
    # x = horizontal, y = vertical, data= tells where to get the data from
    sns.barplot(x='country', y='Events_per_country', data=events_per_country)

    # X-Axis label
    plt.xlabel('')
    # Y-Axis label
    plt.ylabel('Total Sightings', fontsize=20)
    # Title of plot
    plt.title('Total Sightings Per Country', fontsize=25)

    plt.xticks(fontsize=20)
    plt.yticks(fontsize=12)

    # if save for saving plot as .png
    if save:
        plt.savefig('events_per_country.png')

    else:
        plt.show()

# Remove # to view plot
#events_country = prepare_data_country()
#country_bar_plot(events_country)