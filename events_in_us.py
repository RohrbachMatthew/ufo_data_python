""""# This file is meant for data from the US.
- TODO:
    - Dataprep for events per state in the US
    - Plot for events per state in US (possibly show results for null values for states in US as "Non-Labeled)
    - Dataprep for events in cities for each state in the US
    - Plot for events per city per state in US.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.core.interchange.dataframe_protocol import DataFrame

from create_df import fetch_data

def prep_data_states_us():
    # Fetch Data
    rows, columns = fetch_data()

    # Convert
    df = pd.DataFrame(rows, columns=columns)

    # Convert blank to NA
    df.replace('', pd.NA, inplace=True)

    # Check how many Na in states in US (5,797 Na)
    print(df['state'].isna().sum())

    # Pandas extract from states in US countries.

    # group by

    # Test print results


prep_data_states_us()