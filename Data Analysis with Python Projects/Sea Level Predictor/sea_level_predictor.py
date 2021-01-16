import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',sep=',',float_precision='legacy')
    # Create scatter plot
    fig = df.plot(x='Year',
            y='CSIRO Adjusted Sea Level',
            kind='scatter'
            ).figure

    # Create first line of best fit
    x = list(range(df['Year'].to_list()[0],2050)) 
    res = linregress(df['Year'],df['CSIRO Adjusted Sea Level']) 
    df_predict = pd.DataFrame(x,columns=['Year']) 
    df_predict['prediction'] = res.intercept + res.slope*df_predict['Year']
    
    plt.plot(df_predict['Year'],df_predict['prediction'],'r')
  
    # Create second line of best fit
    df2 = df.copy()
    df2 = df2[df2['Year'] >= 2000]
    x2 = list(range(df2['Year'].to_list()[0],2050)) 
    res2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level']) 
    df_predict2 = pd.DataFrame(x2,columns=['Year']) 
    df_predict2['prediction'] = res2.intercept + res2.slope*df_predict2['Year']
    plt.plot(df_predict2['Year'],df_predict2['prediction'],'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
