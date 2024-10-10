import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from caves.models import Cave

class Command(BaseCommand):
    help = 'Importa dados de cavernas de um arquivo CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV.')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                print(row.keys())

                cave_name = row.get('cave_name', 'Nome não encontrado')

                if cave_name == 'Nome não encontrado':
                    print("Cave name não encontrado, verifique o cabeçalho do CSV.")
                    continue

                # Verifica se o usuário existe
                username = row.get('user')
                user = None
                if username:
                    try:
                        user = User.objects.get(username=username)
                    except User.DoesNotExist:
                        print(f"Usuário '{username}' não encontrado, caverna '{cave_name}' não será inserida.")
                        continue

                # Converte 'Yes'/'No' para 1/0
                relevance_surveyed_value = row.get('relevance_surveyed')
                if relevance_surveyed_value == 'Yes':
                    relevance_surveyed = 1
                elif relevance_surveyed_value == 'No':
                    relevance_surveyed = 0
                else:
                    print(f"Valor inválido para relevance_surveyed: {relevance_surveyed_value} para a caverna '{cave_name}'.")
                    continue

                # Tratar o campo relevance_factor
                relevance_factor_value = row.get('relevance_factor')
                try:
                    relevance_factor = float(relevance_factor_value)
                except ValueError:
                    print(f"Valor inválido para relevance_factor: {relevance_factor_value} para a caverna '{cave_name}'. Usando 0 como valor padrão.")
                    relevance_factor = 0  # ou escolha outro valor padrão

                # Insira os dados no banco de dados
                Cave.objects.create(
                    cave_name=cave_name,
                    longitude=row.get('Longitude'),
                    latitude=row.get('Latitude'),
                    elevation=row.get('elevation'),
                    length=row.get('length'),
                    depth=row.get('depth'),
                    area=row.get('area'),
                    volume=row.get('volume'),
                    lithology=row.get('lithology'),
                    relevance_surveyed=relevance_surveyed,
                    relevance_factor=relevance_factor,  # Atribui o valor tratado
                    geomorph_unit=row.get('geomorph_unit'),
                    description=row.get('description'),
                    user=user
                )