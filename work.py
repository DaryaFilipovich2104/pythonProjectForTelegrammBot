import requests


def make_request(endpoint, query=''):
    base_url = 'https://api.kinopoisk.dev/'
    headers = {'X-API-KEY': '20JSY3F-6FA4WZW-KG7Z6A6-KNY2902'}
    response = requests.get(url=f"{base_url}{endpoint}{query}",
                            headers=headers)
    return response


def make_request_by_genre_action(genre):
    endpoint = 'v1.3/movie'
    query = f'?genres.name={genre}'
    response = make_request(endpoint=endpoint, query=query)
    l = len(response.json()["docs"])
    movies_action = []
    for i in range(l):
        print(f"Название: {response.json()['docs'][i]['name']} \n"
              f"Год выпуска фильма: {response.json()['docs'][i]['year']} \n"
              f"Описание: {response.json()['docs'][i]['description']}\n"
              f"Постер: {response.json()['docs'][i]['poster']['url']}")
        movies_action.append(f"Название: {response.json()['docs'][i]['name']} \n"
                             f"Год выпуска фильма: {response.json()['docs'][i]['year']} \n"
                             f"Описание: {response.json()['docs'][i]['description']}\n"
                             f"Постер: {response.json()['docs'][i]['poster']['url']}")

    return movies_action


def make_request_by_genre_comedy(genre):
    endpoint = 'v1.3/movie'
    query = f'?genres.name={genre}'
    response = make_request(endpoint=endpoint, query=query)
    l = len(response.json()["docs"])
    movies_comedy = []
    for i in range(l):
        print(f"Название: {response.json()['docs'][i]['name']} \n"
              f"Год выпуска фильма: {response.json()['docs'][i]['year']} \n"
              f"Описание: {response.json()['docs'][i]['description']}\n"
              f"Постер: {response.json()['docs'][i]['poster']['url']}")
        movies_comedy.append(f"Название: {response.json()['docs'][i]['name']} \n"
                             f"Год выпуска фильма: {response.json()['docs'][i]['year']} \n"
                             f"Описание: {response.json()['docs'][i]['description']}\n"
                             f"Постер: {response.json()['docs'][i]['poster']['url']}")

    return movies_comedy


def make_request_by_genre_fantastic(genre):
    endpoint = 'v1.3/movie'
    query = f'?genres.name={genre}'
    response = make_request(endpoint=endpoint, query=query)
    l = len(response.json()["docs"])
    movies_fantastic = []
    for i in range(l):
        print(f"Название: {response.json()['docs'][i]['name']} \n"
              f"Год выпуска фильма: {response.json()['docs'][i]['year']} \n"
              f"Описание: {response.json()['docs'][i]['description']}\n"
              f"Постер: {response.json()['docs'][i]['poster']['url']}")
        movies_fantastic.append(f"Название: {response.json()['docs'][i]['name']} \n"
                                f"Год выпуска фильма: {response.json()['docs'][i]['year']} \n"
                                f"Описание: {response.json()['docs'][i]['description']}\n"
                                f"Постер: {response.json()['docs'][i]['poster']['url']}")

    return movies_fantastic


def make_request_by_genre_melodramas(genre):
    endpoint = 'v1.3/movie'
    query = f'?genres.name={genre}'
    response = make_request(endpoint=endpoint, query=query)
    l = len(response.json()["docs"])
    movies_melodramas = []
    for i in range(l):
        print(f"Название: {response.json()['docs'][i]['name']} \n"
              f"Год выпуска фильма: {response.json()['docs'][i]['year']} \n"
              f"Описание: {response.json()['docs'][i]['description']}\n"
              f"Постер: {response.json()['docs'][i]['poster']['url']}")
        movies_melodramas.append(f"Название: {response.json()['docs'][i]['name']} \n"
                                 f"Год выпуска фильма: {response.json()['docs'][i]['year']} \n"
                                 f"Описание: {response.json()['docs'][i]['description']}\n"
                                 f"Постер: {response.json()['docs'][i]['poster']['url']}")

    return movies_melodramas


genre = 'боевик'
response = make_request_by_genre_action(genre)
genre = 'комедия'
response = make_request_by_genre_comedy(genre)
genre = 'фантастика'
response = make_request_by_genre_fantastic(genre)
genre = 'мелодрама'
response = make_request_by_genre_melodramas(genre)
