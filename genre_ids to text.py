import csv
import pandas as pd


def get_genre_names(genre_ids):
    # Define a dictionary to map genre IDs to genre names
    genres = {
        '28': 'Action',
        '12': 'Adventure',
        '16': 'Animation',
        '35': 'Comedy',
        '80': 'Crime',
        '99': 'Documentary',
        '18': 'Drama',
        '10751': 'Family',
        '14': 'Fantasy',
        '36': 'History',
        '27': 'Horror',
        '10402': 'Music',
        '9648': 'Mystery',
        '10749': 'Romance',
        '878': 'Science Fiction',
        '10770': 'TV Movie',
        '53': 'Thriller',
        '10752': 'War',
        '37': 'Western'
    }

    # Get the genre names for the given genre IDs
    genre_names = [genres.get(genre_id, 'Unknown') for genre_id in genre_ids]

    return genre_names


data = pd.read_csv('MoviesTopRated.csv')
df = pd.DataFrame(data)
my_col = df["genre_ids"]


# print(my_col[1].strip("[ ]").replace(" ", "").split(","))
# print(get_genre_names((my_col[1].replace(" ", "").strip("[ ]").split(","))))


f_result = []
for i in my_col:
    f_result.append(get_genre_names(
        (i.replace(" ", "").strip("[ ]").split(","))))

f_df = pd.concat([df, pd.Series(f_result, name="genre_labels")],
                 axis=1)
f_df.to_csv("MoviesTopRated_Texted_genre.csv")
