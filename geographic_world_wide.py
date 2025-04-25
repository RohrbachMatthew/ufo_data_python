"""
TODO: Add cities that appear more than a certain amount of times (hot spot cities).
    - Do they appear at cities near airports or military bases?
"""
from types import new_class

import pandas as pd
import matplotlib.pyplot as plt

# Geopandas extends pandas for geometric types
import geopandas as gpd
from create_df import fetch_data

def prepare_data_world_plot():
    rows, columns = fetch_data()

    df = pd.DataFrame(rows, columns=columns)

    df.replace('', pd.NA, inplace=True)

    # Check how many is na (0)
    # print(df[['longitude', 'latitude']].isna().sum())

    data = df
    return data

def world_plot(data, save=False):
    df = pd.DataFrame(data)

    # Convert the dataframe to a GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

    # Load the world map from a URL
    url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
    world = gpd.read_file(url)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 8))
    world.plot(ax=ax, color='lightgrey')
    gdf.plot(ax=ax, color='red', markersize=0.5)

    # Set plot title and labels
    ax.set_title('World Geographical Plot of UFO Sightings', fontsize=20)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_yticks([])
    ax.set_xticks([])

    if save:
        plt.savefig('plots\\world_map_sightings.png')
    # Show the plot
    else:
        plt.show()

def prepare_cities():
    rows, columns = fetch_data()
    df = pd.DataFrame(rows, columns=columns)
    df.replace('', pd.NA, inplace=True)
    #print(df.columns)
    cities = df
    return cities

def filter_cities(cities):
    df = cities
    df = df[df['city'].notna()]
    city_count = df.groupby('city').size().reset_index(name='per_city')
    filtered_cities = city_count[city_count['per_city'] > 200]
    filtered_cities = filtered_cities.merge(df[['city', 'country', 'longitude','latitude']], on='city', how='left')
    #print(filtered_cities.columns)
    return filtered_cities

def cities_map_usa(filtered_cities, save=False):
    df = filtered_cities.dropna(subset=['longitude', 'latitude'])  # Remove rows with missing geolocation data
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

    # Load the world map and filter for the USA
    url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
    world = gpd.read_file(url)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 8))
    world.plot(ax=ax, color='lightgrey')  # Plot only the USA
    gdf.plot(ax=ax, color='red', markersize=0.01)  # Plot UFO sightings in the USA

    # Set plot title and labels
    ax.set_title('Geographical Plot of UFO Sightings in the USA', fontsize=20)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_yticks([])
    ax.set_xticks([])

    if save:
        plt.savefig("ufo_sightings_usa_map.png")

    plt.show()



city = prepare_cities()
filter_cities = filter_cities(city)
cities_map_usa(filter_cities)

# REMOVE # to run individual functions

# WORLD PLOT
# world_wide_plot = prepare_data_world_plot()
# world_plot(world_wide_plot, save=True)