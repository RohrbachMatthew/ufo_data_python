# This file is used to show all the plots from a menu and optional save

from events_per_year_plot import prepare_data_year, bar_plot

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
