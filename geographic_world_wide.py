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

# REMOVE # to run individual functions

# WORLD PLOT
# world_wide_plot = prepare_data_world_plot()
# world_plot(world_wide_plot, save=True)