# This file is used to show all the plots from a menu and optional save
import pandas as pd
from create_df import fetch_data
from events_per_year_plot import prepare_data_year, bar_plot

def show_data():
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)

    total_rows = df.index.size  # Counts the number of rows

    pd.set_option('display.max_columns', None)  # Display all columns
    pd.set_option('display.expand_frame_repr', None)  # Prevents wrap around

    # Print the dataframe and total number of rows
    print(f'total number of rows: {total_rows}')
    print(f'\nDataframe:\n{df}')


print("Pick a Graph to view\n"
      "1. Number of Events Per Year > 100 Sighting"
      "2. Print plot")

user = input("Enter Selection")

if user == '1':
    print("Loading bar graph...")
    events_per_year = prepare_data_year()
    bar_plot(events_per_year)

if user == '2':
    print("Saving plot...")
    events_per_year = prepare_data_year()
    bar_plot(events_per_year, save=True)

if user == '3':
    show_data()
