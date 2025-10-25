import pandas as pd

def calculate_demographic_data(print_data=True):
    # 加载数据集
    df = pd.read_csv('adult.data.csv')

    # 1. 每种种族的人口数量
    race_count = df['race'].value_counts()

    # 2. 男性的平均年龄
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. 拥有学士学位的人口占比
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = (bachelors_count / total_count) * 100

    # 4. 高等教育且收入>50K的人口占比
    higher_ed = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_ed_rich_count = higher_ed[higher_ed['salary'] == '>50K'].shape[0]
    higher_ed_total = higher_ed.shape[0]
    percentage_higher_ed = (higher_ed_rich_count / higher_ed_total) * 100

    # 5. 非高等教育且收入>50K的人口占比
    lower_ed = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_ed_rich_count = lower_ed[lower_ed['salary'] == '>50K'].shape[0]
    lower_ed_total = lower_ed.shape[0]
    percentage_lower_ed = (lower_ed_rich_count / lower_ed_total) * 100

    # 6. 每周工作的最少小时数
    min_work_hours = df['hours-per-week'].min()

    # 7. 每周工作最少小时数且收入>50K的人口占比
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]
    min_hours_rich_count = min_hours_workers[min_hours_workers['salary'] == '>50K'].shape[0]
    min_hours_total = min_hours_workers.shape[0]
    rich_percentage = (min_hours_rich_count / min_hours_total) * 100

    # 8. 收入>50K占比最高的国家及对应百分比
    country_rich_ratio = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = country_rich_ratio.idxmax()
    highest_earning_country_percentage = country_rich_ratio.max()

    # 9. 印度收入>50K人群中最受欢迎的职业
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # 格式化输出（保留一位小数）
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", round(average_age_men, 1))
        print(f"Percentage with Bachelors degrees: {round(percentage_bachelors, 1)}%")
        print(f"Percentage with higher education that earn >50K: {round(percentage_higher_ed, 1)}%")
        print(f"Percentage without higher education that earn >50K: {round(percentage_lower_ed, 1)}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {round(rich_percentage, 1)}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {round(highest_earning_country_percentage, 1)}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'percentage_higher_ed': round(percentage_higher_ed, 1),
        'percentage_lower_ed': round(percentage_lower_ed, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }

# 运行函数
calculate_demographic_data()
