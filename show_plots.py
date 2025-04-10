# This file is used to show all the plots from a menu along with and optional save for each plot
import pandas as pd
from create_df import fetch_data
from events_per_year_plot import prepare_data_year, bar_plot
from events_country import prepare_data_country, country_bar_plot

def show_data():
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)

    total_rows = df.index.size  # Counts the number of rows

    pd.set_option('display.max_columns', None)  # Display all columns
    pd.set_option('display.expand_frame_repr', None)  # Prevents wrap around

    # Print the dataframe and total number of rows
    print(f'total number of rows: {total_rows}')
    print(f'\nDataframe:\n{df}')


print("""
    ***********************************
    *      Pick a Graph to view       *
    ***********************************
    *   1. Show the UFO dataframe     *
    *   2. Events Per Year Plot       *
    *   3. Events Per Country Plot    *
    ***********************************""")

user = input("Enter Selection: ")

# Show data
if user == '1':
    show_data()


# Events per year plot
if user == '2':
    print("Events Reported Each Year\n"
          "1. View the bar plot\n"
          "2. Save plot as .png")
    user = input("Enter Choice: ")
    # View plot
    if user == '1':
        events_per_year = prepare_data_year()
        bar_plot(events_per_year)
    # Save plot
    if user == '2':
        print("Saving Plot...")
        events_per_year = prepare_data_year()
        bar_plot(events_per_year, save=True)


# Events per country plot
if user == '3':
    print("Events Reported per Country\n"
          "1. View the bar plot\n"
          "2. Save plot as .png")
    user = input('Enter Choice: ')
    if user == '1':  # View
        events_per_country = prepare_data_country()
        country_bar_plot(events_per_country)
    if user == '2':  # Save
        print("Saving Plot")
        events_per_country = prepare_data_country()
        country_bar_plot(events_per_country, save=True)
