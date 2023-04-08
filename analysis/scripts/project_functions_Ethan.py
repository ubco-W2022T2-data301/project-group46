import pandas as pd
import matplotlib.pyplot as plt

def seperate_listed_in(df):
    df['listed_in'] = df['listed_in'].str.split(', ')
    df = df.explode('listed_in')
    return df

def genres(df):
    df['listed_in'] = df['listed_in'].str.strip().str.lower()
    hulu_genres = df.groupby('listed_in').size().reset_index(name='counts').sort_values(['counts'], ascending=False)
    hulu_genre_distribution = hulu_genres.groupby('listed_in')['counts'].sum().sort_values(ascending=False)

    return hulu_genre_distribution

def genre_plot(df,str):
    # visualize the distribution of genres on each platform
    plt.figure(figsize=(10,6))
    plt.plot(df.index, df.values, label='Hulu')
    plt.title(f'Distribution of Genres on {str}')
    plt.xlabel('Genres')
    plt.ylabel('Number of Titles')
    plt.xticks(rotation=315, ha='left')
    # plt.legend()
    plt.show()

def find_name_per_genre(df,str):
    # create a copy of the original dataframe
    df_copy = df.copy()

    # split the 'listed_in' column into multiple rows based on delimiter ','
    df_copy = df_copy.assign(listed_in=df_copy.listed_in.str.split(', ')).explode('listed_in')

    # create a new dataframe with 'director' and 'listed_in' columns only
    df_director_genre = df_copy[[str, 'listed_in']]

    # group the dataframe by 'listed_in' and 'director', and count the number of occurrences
    df_director_genre = df_director_genre.groupby(['listed_in', str]).size().reset_index(name='counts')

    # for each genre, find the director with the highest count and create a new dataframe
    result_df = pd.DataFrame(columns=['genre', str, 'counts'])
    for genre in df_director_genre['listed_in'].unique():
        df_genre = df_director_genre[df_director_genre['listed_in'] == genre]
        max_counts = df_genre['counts'].max()
        row = df_genre[df_genre['counts'] == max_counts].iloc[0]
        result_df = result_df.append({'genre': genre, str: row[str], 'counts': max_counts}, ignore_index=True)

    return result_df

def seperate_director(df,str):
    df.dropna(subset=[str], inplace=True)
    df[str] = df[str].str.split(', ')
    df = df.explode(str)
    return df
