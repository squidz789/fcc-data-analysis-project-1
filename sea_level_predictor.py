import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))

    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    

    # Create first line of best fit
    slope, intercept, a, b, c = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(1880, 2051))
    plt.plot(years, intercept + slope * years, color='green')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    slope2, intercept2, a2, b2, c2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    years2 = pd.Series(range(2000, 2051))
    plt.plot(years2, intercept2 + slope2 * years2, color='red')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()