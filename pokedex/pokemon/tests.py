import json
from unittest.mock import patch

from django.test import TestCase

from pokemon.management.commands._private import Downloader


class MockResponse(object):
    def __init__(self, *args, **kwargs):
        self.lines = kwargs.get('lines', [])

    def iter_lines(self, *args, **kwargs):
        for line in self.lines:
            yield line


class DownloadPokemonTestCase(TestCase):

    def setUp(self):
        self.downloader = Downloader()

    def test_clean(self):
        data = {
            'id': '1',
            'identifier': 'bulbasaur',
            'species_id': '1',
            'height': '7',
            'weight': '69',
            'base_experience': '64',
            'order': '1',
            'is_default': '1',
        }
        cleaned = self.downloader._clean(data)
        self.assertEqual(cleaned['model'], 'pokemon.pokemon')
        self.assertEqual(type(cleaned['pk']), int)
        fields = cleaned['fields']
        self.assertEqual(type(fields['identifier']), str)
        self.assertEqual(type(fields['species_id']), int)
        self.assertEqual(type(fields['height']), int)
        self.assertEqual(type(fields['weight']), int)
        self.assertEqual(type(fields['base_experience']), int)
        self.assertEqual(type(fields['order']), int)
        self.assertEqual(type(fields['is_default']), bool)

    @patch('requests.get')
    def test_returns_json(self, mock_get):
        mock_get.return_value = MockResponse(lines=[
            'id,identifier,species_id,height,weight,base_experience,order,is_default',
            '1,bulbasaur,1,7,69,64,1,1',
            '2,ivysaur,2,10,130,142,2,1',
            '3,venusaur,3,20,1000,236,3,1',
        ])
        fields = {'identifier': 'bulbasaur', 'species_id': 1, 'height': 7,
                  'weight':  69, 'base_experience': 64, 'order': 1, 'is_default': True}
        item = {
            'model': 'pokemon.pokemon',
            'pk': 1,
            'fields': fields,
        }
        data = self.downloader.download()
        self.assertIn(item, data)
