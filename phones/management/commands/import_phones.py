import csv

from django.core.management.base import BaseCommand
from phones import models


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones_list = list(csv.DictReader(file, delimiter=';'))

        for phone in phones_list:
            item = models.Phone(
                id = phone['id'],
                name = phone['name'],
                price = phone['price'],
                image = phone['image'],
                release_date = phone['release_date'],
                lte_exists = phone['lte_exists']
            )
            item.save()
            
