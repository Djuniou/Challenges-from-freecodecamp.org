import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',sep=',')
df = df.set_index('date')

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975)) 
    ]

def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig = df_line.plot(kind='line',
            title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
            legend=False,
            xlabel='Date',
            ylabel='Page Views',
            figsize=(32,10),
            color='red'
            ).figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().reset_index()
    df_bar['Years'] = pd.DatetimeIndex(df_bar['date']).year
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    df_bar['Month'] = pd.DatetimeIndex(df_bar['date']).month_name()
    df_bar['Month'] = pd.Categorical(df_bar['Month'],categories=months,ordered=True)
    df_bar = df_bar.sort_values(by=['Month']) 
    df_bar = df_bar.groupby(['Years','Month']).mean().unstack()
    
    # Draw bar plot
    fig = df_bar.plot(kind='bar',
                      figsize=(8,8),
                      xlabel='Years',
                      ylabel='Average Page Views',
                      ).legend(labels=months,title='Months').figure  

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy().reset_index()
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    df_box['Month'] = pd.DatetimeIndex(df_box['date']).month_name()
    month_condition = [
        df_box['Month'] == 'January',
        df_box['Month'] == 'February',
        df_box['Month'] == 'March',
        df_box['Month'] == 'April',
        df_box['Month'] == 'May',
        df_box['Month'] == 'June',
        df_box['Month'] == 'July',
        df_box['Month'] == 'August',
        df_box['Month'] == 'September',
        df_box['Month'] == 'October',
        df_box['Month'] == 'November',
        df_box['Month'] == 'December'
        ]
    df_box['Month'] = np.select(month_condition,months)    
    df_box['Month'] = pd.Categorical(df_box['Month'],categories=months,ordered=True)  
    df_box['Year'] = pd.DatetimeIndex(df_box['date']).year
    df_box = df_box.rename(columns={'value':'Page Views'})      
    df_box = df_box.sort_values(by=['Month'])
    # Draw box plots (using Seaborn)    
    fig, axes = plt.subplots(figsize=(20,10),ncols=2)
    sns.despine(left=True)
    sns.boxplot(x='Year',
                y='Page Views',
                data=df_box,
                ax=axes[0]
                ).set_title('Year-wise Box Plot (Trend)').figure
    sns.boxplot(x='Month',
                y='Page Views',
                data=df_box,
                ax=axes[1],
                order=months
                ).set_title('Month-wise Box Plot (Seasonality)').figure
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
