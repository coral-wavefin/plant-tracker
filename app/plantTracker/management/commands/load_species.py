import csv
from django.core.management.base import BaseCommand
from app.plantTracker.models import Species


class Command(BaseCommand):
    help = "Load species data from a CSV file into the Species model"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="The path to the CSV file to be loaded",
        )

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs["csv_file"]

        try:
            with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Check if the species already exists
                    if not Species.objects.filter(
                        generic_name=row["generic_name"],
                        specific_name=row["specific_name"],
                    ).exists():
                        Species.objects.create(
                            generic_name=row["generic_name"],
                            specific_name=row["specific_name"],
                            common_name=row["common_name"],
                            light_requirements=row["light_requirements"],
                            watering_frequency=row["watering_frequency"],
                            soil_type=row["soil_type"],
                            temperature_range=row["temperature_range"],
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Added species: {row['generic_name']} {row['specific_name']}"
                            )
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Species already exists: {row['generic_name']} {row['specific_name']}"
                            )
                        )
            self.stdout.write(self.style.SUCCESS("Data loading completed!"))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {csv_file_path}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {str(e)}"))