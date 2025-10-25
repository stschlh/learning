import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. 导入数据
df = pd.read_csv('medical_examination.csv')

# 计算BMI：Weight(kg) / (Height(m))^2
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
# 根据BMI设置 overweight 列：1（超重，BMI≥25）、0（不超重）
df['overweight'] = np.where(df['BMI'] >= 25, 1, 0)

# 3. 归一化 cholesterol（胆固醇）、gluc（血糖）：1→0（正常），2/3→1（异常）
for col in ['cholesterol', 'gluc']:
    df[col] = np.where(df[col] == 1, 0, 1)

# 4. 重塑数据：将胆固醇、血糖、吸烟、饮酒、运动、超重转换为“长表”格式
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

# 5. 分组统计：按cardio（是否患病）和特征值分组，计算每个组的样本数
df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')

# 6. 绘制分类图
sns.catplot(x='variable', y='count', hue='value', col='cardio', data=df_cat, kind='bar')
plt.savefig('catplot.png')  # 保存图表

# 11. 清洗异常值：保留满足以下条件的行
df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &  # 舒张压≤收缩压
    (df['height'] >= df['height'].quantile(0.025)) &  # 身高≥2.5%分位数
    (df['height'] <= df['height'].quantile(0.975)) &  # 身高≤97.5%分位数
    (df['weight'] >= df['weight'].quantile(0.025)) &  # 体重≥2.5%分位数
    (df['weight'] <= df['weight'].quantile(0.975))  # 体重≤97.5%分位数
]

# 12. 计算相关系数矩阵
corr = df_heat.corr()

# 13. 生成上三角掩码（避免重复显示）
mask = np.triu(np.ones_like(corr, dtype=bool))

# 14. 绘制热图
plt.figure(figsize=(10, 8))
sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm')
plt.savefig('heatmap.png')  # 保存图表

