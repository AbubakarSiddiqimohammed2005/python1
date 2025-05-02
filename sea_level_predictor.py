import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Line of best fit for all data
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_all = pd.Series(range(1880, 2051))
    y_pred_all = res_all.intercept + res_all.slope * x_pred_all
    ax.plot(x_pred_all, y_pred_all, 'r', label='Best fit: 1880–2050')

    # Line of best fit from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    ax.plot(x_pred_recent, y_pred_recent, 'g', label='Best fit: 2000–2050')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save and return figure
    plt.tight_layout()
    fig.savefig('sea_level_plot.png')
    return fig
