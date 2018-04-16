from io import StringIO
import json

import requests


class Downloader(object):
    """ Download pokemon data and convert to JSON """
    url = 'https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/csv/pokemon.csv'

    def download(self):
        response = requests.get(self.url)
        columns = {}
        delimiter = ','
        pokemon = []
        for i, line in enumerate(response.iter_lines(decode_unicode=True)):
            if i == 0:
                for j, col in enumerate(line.split(delimiter)):
                    columns[j] = col
            else:
                data = {}
                for j, col in enumerate(line.split(delimiter)):
                    data[columns[j]] = col
                pokemon.append(self._clean(data))
        return pokemon

    def _clean(self, data):
        cleaned = {
            'model': 'pokemon.pokemon',
            'fields': {}
        }
        for k, v in data.items():
            if k in ['id']:
                cleaned['pk'] = int(v)
            elif k in ['species_id', 'height', 'weight', 'base_experience', 'order', ]:
                cleaned['fields'][k] = int(v)
            elif k in ['is_default']:
                cleaned['fields'][k] = bool(v)
            elif k in ['identifier']:
                cleaned['fields'][k] = v
        return cleaned
