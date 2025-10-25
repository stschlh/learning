import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data():
    df = pd.read_csv('fcc-forum-pageviews.csv')
    df.set_index('date', inplace=True)
    df.index = pd.to_datetime(df.index)
    lower = df['value'].quantile(0.025)
    upper = df['value'].quantile(0.975)
    df = df[(df['value'] >= lower) & (df['value'] <= upper)]
    return df

def draw_line_plot():
    df = load_and_clean_data().copy()
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], 'r-')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.savefig('line_plot.png')
    plt.close()
    return plt.gcf()

def draw_bar_plot():
    df = load_and_clean_data().copy()
    df['Year'] = df.index.year
    df['Month'] = df.index.month_name()
    df_grouped = df.groupby(['Year', 'Month'])['value'].mean().unstack()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    df_grouped = df_grouped[months]
    ax = df_grouped.plot(kind='bar', figsize=(12, 8))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.savefig('bar_plot.png')
    plt.close()
    return plt.gcf()

def draw_box_plot():
    df = load_and_clean_data().copy()
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Month Name'] = df.index.month_name().str[:3]
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x='Year', y='value', data=df, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    sns.boxplot(x='Month Name', y='value', data=df, order=month_order, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.close()
    return plt.gcf()
