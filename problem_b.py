import json
from multiprocessing.sharedctypes import Value
from pprint import pprint


def movie_info(movie, genres):
    genre_ids = movie['genre_ids']
    genre_names = []

    for genre in genres:
        if genre['id'] in genre_ids:
            genre_names.append(genre['name'])

    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']

    movie_info_dict = {}
    for key in key_list:
        movie_info_dict[key] = movie[key]
        movie_info_dict['gerne_names'] = genre_names
    return movie_info_dict
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))