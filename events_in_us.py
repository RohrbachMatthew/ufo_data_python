""""# This file is meant for data from the US.

    - Dataprep for events per state in the US
        - filters na values in us country (0)
        - Orders by ascending order

    - Plot for events per state in US
        - Displays count for each state on bottom of each bar in plot

- TODO:
    - Dataprep for events in cities for each state in the US
    - Plot for events per city per state in US.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from create_df import fetch_data

# Events Per State in US
def prep_data_states_us():
    # Fetch Data
    rows, columns = fetch_data()

    # Convert
    df = pd.DataFrame(rows, columns=columns)

    # Convert blank to NA, (not dropping na in this plot)
    df.replace('', pd.NA, inplace=True)

    # Check how many Na in states in data frame (5,797 Na)
    # print(df['state'].isna().sum())

    # Filter data by us in country column
    filtered_df = df[df['country'].str.lower() == 'us']

    '''
    - Create a copy of DF, avoids SettingWithCopyWarning
    - Groups states with na values together, names them 'Unknown (No na values in this new df (filtered_df))
    - Remove # below to run and run test print'''
    filtered_df = filtered_df.copy()
    # filtered_df['state'] = filtered_df['state'].fillna('Unknown')

    filtered_df['state'] = filtered_df['state'].str.upper()

    # Remove # to test print the data frame
    # print(filtered_df)

    # Group by events per state (explained in events_per_year_plot.py line:33)
    state_count = filtered_df.groupby('state').size().reset_index(name='num_of_events')

    # Order by count ascending
    state_count = state_count.sort_values(by='num_of_events', ascending=True)

    # Test print results
    # print(state_count)

    return state_count

# Plot for Events per State
def states_us_barplot(state_count, save=False):
    # Sets size of plot
    plt.figure(figsize=(25, 8))

    # Seaborn bar plot, x = horizontal, y = vertical, data= tells where to get the data from
    # ax is a Seaborn generated plot object
    ax = sns.barplot(x='state', y='num_of_events', data=state_count)


    # Get the positions of the bars
    bar_positions = ax.get_xticks()

    # Add labels for total counts on each bar
    for position, row in zip(bar_positions, state_count.iterrows()):
        index, row_data = row
        ax.annotate(f'{row_data["num_of_events"]}',
                    (position, 0),
                    ha='center', va='bottom', fontsize=10, color='black')

    # make x-axis label
    plt.xlabel('States', fontsize=20)
    # make y-axis label
    plt.ylabel('Total Sightings', fontsize=30)
    # make title
    plt.title('Total Sightings In Each State In US', fontsize=30)

    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    if save:
        plt.savefig('events_per_state_us.png')
    else:
        plt.show()

# Remove # below to run
#events_per_state = prep_data_states_us()
#states_us_barplot(events_per_state)
