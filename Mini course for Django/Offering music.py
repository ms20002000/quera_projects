all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, album_name: list, all_users: dict, all_albums: dict):
    all_users.update({username: [age, city, album_name, all_albums]})


def add_album(album_name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums.update({album_name: [artist_name, genre, tracks, all_users]})


def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    d = all_users[username]
    counter =0
    for i in d[2]:
        if artist_name in all_albums[i]:
            counter += all_albums[i][2]
    return counter




def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    d = all_users[username][2]
    counter =0
    for i in d:
        if genre in all_albums[i]:
            counter += all_albums[i][2]
    return counter


def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
    counter =0
    for i in all_users.keys():
        if age in all_users[i]:
            d = all_users[i][2]
            for j in d:
                if artist_name in all_albums[j]:
                    counter += all_albums[j][2]
    return counter


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    counter = 0
    for i in all_users.keys():
        if age in all_users[i]:
            d = all_users[i][2]
            for j in d:
                if genre in all_albums[j]:
                    counter += all_albums[j][2]
    return counter


def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    counter = 0
    for i in all_users.keys():
        if city in all_users[i]:
            d = all_users[i][2]
            for j in d:
                if artist_name in all_albums[j]:
                    counter += all_albums[j][2]
    return counter


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    counter = 0
    for i in all_users.keys():
        if city in all_users[i]:
            d = all_users[i][2]
            for j in d:
                if genre in all_albums[j]:
                    counter += all_albums[j][2]
    return counter