# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import requests


API = 'https://api.sumanjay.cf/watch/'


def info(movie):
    info = f"Title: {movie['title']}\n"
    info += f"Type: {movie['type']}\n"
    if movie['providers']:
        providers = movie['providers']
        info += f"Providers:"
        try:
            providers = movie['providers']
            for provider in providers:
                info += f" [{provider}]({providers[provider]})"
            info += "\n"
    try:
        info += f"Release Date: {str(movie['release_date'])}\n"
    except:
        pass
    try:
        info += f"Release Year: {movie['release_year']}\n"
    except:
        pass
    try:
        if movie['score']:
            scores = movie['score']
            info += "Score:"
            for score in scores:
                info += f" {score} - {str(scores[score])}"
    except:
        pass
    return info