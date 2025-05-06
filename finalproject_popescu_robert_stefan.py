import pandas as pd
from dataprocessing import prepare_data
df = pd.read_csv('fit_trackr_data.csv')
df = prepare_data(df)
rows, columns = df.shape
print(f"There are {rows} rows and {columns} columns.\n")
df.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in df.columns]
df.to_csv('fit_trackr_data.csv', index=False, encoding="utf-8-sig")

# 1. Care este durata medie a activității?
mean_val = df['duration'].mean()
print(f"Medium duration of activity is: {mean_val:.2f} minutes.\n")
# 2. Ce tip de activitate practica cel mai des utilizatorii?
mode_val = df['activity'].mode()
print(f"Most practiced activty by users are: {", ".join(mode_val.astype(str))}\n")
# 3. Care este cea mai frecventa stare de spirit a utilizatorului dupa activitate?
mode_val = df['mood'].mode()
print(f"The most common mood is: {", ".join(mode_val.astype(str))}\n")
# 4. Care este variatia consumului de calorii in functie de tipul de activitate?
calories_stats = df.groupby('activity', observed=True).agg(
    calories_std = ('calories', 'std'),
    activities_count = ('activity', 'count')
)
calories_sorted = calories_stats.sort_values(by=["calories_std"], ascending=False)
print(calories_sorted.head(8))
# 5. Care este diferenta intre varstele utilizatorilor fata de 50% din mijlocul datelor?
q2 = df['age'].quantile(0.50)
df['age_diff_from_median'] = (df['age'] - q2).abs()
print(df[['age', 'age_diff_from_median']].head())
# 6. Ce tipuri de activitati determina in cea mai fericita dispozitie? 
happy_df = df[df['mood'] == 'Happy'].copy()
activity_stats = happy_df.groupby('activity', observed=True).agg(
    activity_count = ('activity', 'count')
)
activity_count_sorted = activity_stats.sort_values(by=['activity_count'], ascending=False)
print(activity_count_sorted)
# 7. Utilizatorii cu activitati mai lungi au o dispozitie mai fericita?
happy_df = df[df['mood'] == 'Happy'].copy()
Q1 = happy_df['duration'].quantile(0.25)
Q2 = happy_df['duration'].quantile(0.50)
Q3 = happy_df['duration'].quantile(0.75)

def assign_quartile(duration):
    if duration <= Q1:
        return '1st quartile'
    elif duration <= Q2:
        return '2nd quartile'
    elif duration <= Q3:
        return '3rd quartile'
    else:
        return '4th quartile'

happy_df['duration_quartile'] = happy_df['duration'].apply(assign_quartile)

duration_per_quartile = happy_df.groupby('duration_quartile')['activity'].count().reset_index()

print(duration_per_quartile)
print("No, taking more time doesn't bring more happiness.")




