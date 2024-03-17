import csv
from datetime import datetime
from shop.models import Client


def import_clients_from_csv():
    with open('shop/dataset.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            birth_date = datetime.strptime(row['birthDate'], '%Y-%m-%d').date()

            client = Client(
                category=row['category'],
                first_name=row['firstname'],
                last_name=row['lastname'],
                email=row['email'],
                gender=row['gender'],
                birth_ate=birth_date
            )
            client.save()
