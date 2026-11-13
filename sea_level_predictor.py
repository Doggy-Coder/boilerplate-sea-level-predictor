import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('D:/Data Analysis/Final Tests/boilerplate-sea-level-predictor-main/epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[0]
    y_intercept1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[1]
    x1 = np.arange(1880, 2051)
    y1 = x1*slope1 + y_intercept1
    ax.plot(x1, y1)

    # Create second line of best fit
    slope2 = linregress(
        df.loc[df['Year']>=2000, 'Year'],
        df.loc[df['Year']>=2000, 'CSIRO Adjusted Sea Level']
    )[0]
    y_intercept2 = linregress(
            df.loc[df['Year']>=2000, 'Year'],
            df.loc[df['Year']>=2000, 'CSIRO Adjusted Sea Level']
        )[1]
    x2 = np.arange(2000, 2051)
    y2 = x2*slope2 + y_intercept2
    ax.plot(x2, y2)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()