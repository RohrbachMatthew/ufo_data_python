# This file is used to show all the plots from a menu along with and optional save for each plot
"""
TODO: Add to Comparison Menu
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

# PLOT MENUS
def main():
    while True:
        print("""
        *********************************************
        *         UFO Sightings Main Menu           *
        *********************************************
        *       Type q To Quit The Program          *
        *       1. View the Data Frame              *
        *       2. World Wide Plots                 *
        *       3. US Based Plots                   *
        *       4. US Excluded Plots                *
        *       5. Comparison Plots                 *
        *********************************************
        """)
        user = input('Enter Choice: ')

        if user == 'q':
            print('Exiting Program...')
            break

        elif user == '1':
            show_data()
            continue

    # WORLD WIDE PLOTS
        elif user == '2':
            print("""
            ***************************************************************
            *                UFO World Wide Plots Menu                    *
            ***************************************************************
            *       1. Events World Plot          7.                      *
            *       2. Events Per Country         8.                      *
            *       3. Events Per Year            9.                      *
            *       4. Events Per Month           10. Back to Main Menu   *
            *       5. Events Per Day of Month                            *
            *       6. Events Per Hour                                    *
            ***************************************************************
            """)
            user = input('Enter Choice: ')

        # World Plot
            if user == '1':
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

        # Per Country Plot
            if user == '2':
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

        # Events Per Year Plot
            if user == '3':
                print('Events per year')
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

        # Events per month plot
            if user == '4':
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

        # Events reported per day plot
            if user == '5':
                print("""
                *********************************************
                *     Events Reported per Day World Wide    *
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

        # Events per hour plot
            if user == '6':
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

        # Leave the Worldwide menu
            if user == '10':
                continue

    # US-BASED PLOTS
        elif user == '3':
            print("""
            *******************************************
            *       UFO US BASED Plots Menu         *
            *******************************************
            *       1. Events Per State               *
            *       2.                                *
            *       3.                                *
            *       4. Back to Main Menu              *
            *******************************************
            """)
            user = input('Enter Choice: ')
        # Events per state in US Plot
            if user == '1':
                print('Events Per State')
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
        # Leave US-Based sightings
            if user == '4':
                continue

    # Excluding US Plots
        elif user == '4':
            print("""
            *******************************************
            *       UFO Sightings Excluding US        *
            *******************************************
            *       1. Events Per Month               *
            *       2.                                *
            *       3.                                *
            *       4. Back to Main Menu              *
            *******************************************
            """)
            user = input('Enter Choice: ')

            if user == '1':
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
            # Go Back to main
                if user == '3':
                    continue
        # ANOTHER PLOT
            if user == '2':
                print('Non US Plot')
        # ANOTHER PLOT
            if user == '3':
                print('Non US Plot')
        # Go Back to Main From Sightings Excluding US Menu
            if user == '4':
                continue

        elif user == '5':
            print("""
                *******************************************
                *       UFO Comparison Plots Menu         *
                *******************************************
                *       1. Events Per Year US and Non US  *
                *       2.                                *
                *       3.                                *
                *       4. Back to Main Menu              *
                *******************************************
                """)
            user = input('Enter Choice: ')
            if user == '1':
                continue
            if user == '2':
                continue

if __name__ == '__main__':
    main()