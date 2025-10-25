import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 加载数据
    df = pd.read_csv('epa-sea-level.csv')
    
    # 1. 全周期（1880-2050）的线性回归拟合
    x_all = df['Year']
    y_all = df['CSIRO Adjusted Sea Level']
    slope_all, intercept_all, r_value, p_value, std_err = linregress(x_all, y_all)
    x_pred_all = pd.Series(range(1880, 2051))
    y_pred_all = slope_all * x_pred_all + intercept_all
    
    # 2. 2000年以来的线性回归拟合
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    slope_recent, intercept_recent, _, _, _ = linregress(x_recent, y_recent)
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = slope_recent * x_pred_recent + intercept_recent
    
    # 绘制图表
    plt.figure(figsize=(12, 8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')
    plt.plot(x_pred_all, y_pred_all, 'r', label='Best Fit Line (1880-2050)')
    plt.plot(x_pred_recent, y_pred_recent, 'g', label='Best Fit Line (2000-2050)')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # 保存并返回图像
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
