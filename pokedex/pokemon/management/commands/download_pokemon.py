import json
import sys

from django.core.management.base import BaseCommand

from ._private import Downloader

downloader = Downloader()


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = downloader.download()
        sys.stdout.write(json.dumps(data))
