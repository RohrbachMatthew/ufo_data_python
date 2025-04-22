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
from temporal_patterns_worldwide import prepare_day_of_month, day_of_month_bar, prepare_time_day, time_hourly_bar, prepare_month, month_plot
from geographic_world_wide import prepare_data_world_plot, world_plot
from non_us_data import prepare_month_non_us, month_non_us_plot

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
    while True:
        print("""
            ************************************
            *       Pick a Graph to view       *
            ************************************
            *   Type 'q' to quit program       *
            *   1. Show the UFO dataframe      *
            *   2. Events Per Year             *
            *   3. Events Per Country          *
            *   4. Events Per State in US      *
            *   5. Events Per Day of Month     *
            *   6. Events Per Month Worldwide  *
            *   7. Events Per Hour Worldwide   *
            *   8. Events World Plot           *
            *   9. Events Per Month Non US     *
            ************************************""")

        user = input("\nEnter Selection: ")

        # Quit program
        if user == 'q':
            break

# Show data
        if user == '1':
            show_data()
            continue

# Events per year plot
        elif user == '2':
            print("""
            ***********************************
            *   Events Reported Each Year     *
            ***********************************
            *     1. View the bar plot        *
            *     2. Save plot as .png        *
            *     3. Back to main menu        *
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
            # Back to main
            if user == '3':
                continue

# Events per country plot
        elif user == '3':
            print("""
            ***********************************
            *   Events Reported per Country   *
            ***********************************
            *     1. View the bar plot        *
            *     2. Save plot as .png        *
            *     3. Back to main menu        *
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
            # Back to main
            if user == '3':
                continue

# Events per state in the US
        elif user == '4':
            print("""
            *********************************************
            *  Events Reported per State in US country  *
            *********************************************
            *       1. View the bar plot                *
            *       2. Save plot as .png                *
            *       3. Back to main menu                *
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
            # Back to main
            if user == '3':
                continue

#  Events per day of the month
        elif user == '5':
            print("""
            *********************************************
            *     Events Reported per Day of Month      *
            *********************************************
            *       1. View the bar plot                *
            *       2. Save plot as .png                *
            *       3. Back to main menu                *
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
            # Back to main
            if user == '3':
                continue

# Events Per Month Worldwide
        elif user == '6':
            print("""
                *********************************************
                *     Events Reported Month Worldwide      *
                *********************************************
                *       1. View the bar plot                *
                *       2. Save plot as .png                *
                *       3. Back to main menu                *
                *********************************************
                """)
            user = input('Enter Choice: ')
            if user == '1':
                print('Loading Plot...')
                months = prepare_month()
                month_plot(months)
            if user == '2':
                print('Saving Plot...')
                months = prepare_month()
                month_plot(months, save=True)
                print("Plot Saved Successfully")
            if user == '3':
                continue

# Worldwide Sightings Per Hour
        elif user == '7':
            print("""
            *********************************************
            *    Events Reported per Hour World Wide    *
            *********************************************
            *       1. View the bar plot                *
            *       2. Save plot as .png                *
            *       3. Back to main menu                *
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
            # Back to main
            if user == '3':
                continue

        elif user == '8':
            print("""
            *********************************************
            *    Events Reported World Plot             *
            *********************************************
            *       1. View the bar plot                *
            *       2. Save plot as .png                *
            *       3. Back to main menu                *
            *********************************************
            """)
            user = input('Enter Choice: ')
            if user == '1':
                print('Loading Plot...')
                world_plot_data = prepare_data_world_plot()
                world_plot(world_plot_data)
            if user == '2':
                print('Saving Plot...')
                world_plot_data = prepare_data_world_plot()
                world_plot(world_plot_data, save=True)
                print("Plot Saved Successfully")
            if user == '3':
                continue

        elif user == '9':
            print("""
            *********************************************
            *    Events Reported Per Month Non US       *
            *********************************************
            *       1. View the bar plot                *
            *       2. Save plot as .png                *
            *       3. Back to main menu                *
            *********************************************
            """)
            user = input('Enter Choice: ')
            if user == '1':
                print('Loading Plot...')
                per_month = prepare_month_non_us()
                month_non_us_plot(per_month)
            if user == '2':
                print('Saving Plot...')
                per_month = prepare_month_non_us()
                month_non_us_plot(per_month, save=True)
                print("Plot Saved Successfully")
            if user == '3':
                continue

if __name__ == '__main__':
    main()