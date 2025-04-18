# This file is used to show all the plots from a menu along with and optional save for each plot
"""
TODO: Add main menu, sub menu then plot selection
    (Example: main -> us based events -> events per state in US plot)
    (Example: main -> world wide events -> events per year plot)
"""
import pandas as pd
from create_df import fetch_data
from events_per_year_plot import prepare_data_year, bar_plot
from events_country import prepare_data_country, country_bar_plot
from events_in_us import prep_data_states_us, states_us_barplot
from temporal_patterns_worldwide import prepare_day_of_month, day_of_month_bar, prepare_time_day, time_hourly_bar

def show_data():
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)

    total_rows = df.index.size  # Counts the number of rows

    pd.set_option('display.max_columns', None)  # Display all columns
    pd.set_option('display.expand_frame_repr', None)  # Prevents wrap around

    # Print the dataframe and total number of rows
    print(f'total number of rows: {total_rows}')
    print(f'\nDataframe:\n{df}')

def main():
    print("""
        ************************************
        *       Pick a Graph to view       *
        ************************************
        *   1. Show the UFO dataframe      *
        *   2. Events Per Year             *
        *   3. Events Per Country          *
        *   4. Events Per State in US      *
        *   5. Events Per Day of Month     *
        *   6. Events Per Hour Worldwide   *
        ************************************""")

    user = input("\nEnter Selection: ")

    # Show data
    if user == '1':
        show_data()


    # Events per year plot
    if user == '2':
        print("""
        ***********************************
        *   Events Reported Each Year     *
        ***********************************
        *     1. View the bar plot        *
        *     2. Save plot as .png        *
        ***********************************
              """)
        user = input("Enter Choice: ")
        # View plot
        if user == '1':
            print("Loading Plot...")
            events_per_year = prepare_data_year()
            bar_plot(events_per_year)
        # Save plot
        if user == '2':
            print("Saving Plot...")
            events_per_year = prepare_data_year()
            bar_plot(events_per_year, save=True)
            print("Plot Saved Successfully")

    # Events per country plot
    if user == '3':
        print("""
        ***********************************
        *   Events Reported per Country   *
        ***********************************
        *     1. View the bar plot        *
        *     2. Save plot as .png        *
        ***********************************
            """)
        user = input('Enter Choice: ')
        if user == '1':  # View
            print("Loading Plot...")
            events_per_country = prepare_data_country()
            country_bar_plot(events_per_country)
        if user == '2':  # Save
            print("Saving Plot...")
            events_per_country = prepare_data_country()
            country_bar_plot(events_per_country, save=True)
            print("Plot Saved Successfully")

    # Events per state in the US
    if user == '4':
        print("""
        *********************************************
        *  Events Reported per State in US country  *
        *********************************************
        *    1. View the bar plot                   *
        *    2. Save plot as .png                   *
        *********************************************
        """)
        user = input('Enter Choice: ')
        if user == '1':  # View plot
            print("Loading plot...")
            events_per_state = prep_data_states_us()
            states_us_barplot(events_per_state)
        if user == '2':  # Save plot
            print("Saving Plot...")
            events_per_state = prep_data_states_us()
            states_us_barplot(events_per_state, save=True)
            print("Plot Saved Successfully")

#  Events per day of the month
    if user == '5':
        print("""
        *********************************************
        *     Events Reported per Day of Month      *
        *********************************************
        *    1. View the bar plot                   *
        *    2. Save plot as .png                   *
        *********************************************
        """)
        user = input('Enter Choice: ')
        if user == '1':
            print("Loading Plot...")
            events_per_day_month = prepare_day_of_month()
            day_of_month_bar(events_per_day_month)
        if user == '2':
            print("Saving Plot...")
            events_per_day_month = prepare_day_of_month()
            day_of_month_bar(events_per_day_month, save=True)
            print("Plot Saved Successfully")

# Worldwide Sightings Per Hour
    if user == '6':
        print("""
        *********************************************
        *    Events Reported per Hour World Wide    *
        *********************************************
        *    1. View the bar plot                   *
        *    2. Save plot as .png                   *
        *********************************************
        """)
        user = input("Enter choice: ")
        if user == '1':
            print('Loading Plot...')
            events_per_hour = prepare_time_day()
            time_hourly_bar(events_per_hour)
        if user == '2':
            print('Saving Plot....')
            events_per_hour = prepare_time_day()
            time_hourly_bar(events_per_hour, save=True)
            print('Plot Saved Successfully')

if __name__ == '__main__':
    main()