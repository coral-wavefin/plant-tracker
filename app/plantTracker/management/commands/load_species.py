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
                    # Split the Botanical Name into generic_name and specific_name
                    botanical_name = row["Botanical Name"]
                    name_parts = botanical_name.split(" ", 1)
                    generic_name = name_parts[0]
                    specific_name = name_parts[1] if len(name_parts) > 1 else ""

                    # Check if the species already exists
                    if not Species.objects.filter(
                        generic_name=generic_name,
                        specific_name=specific_name,
                    ).exists():
                        Species.objects.create(
                            generic_name=generic_name,
                            specific_name=specific_name,
                            common_name=row["Common Name"],
                            light_requirements=row["Light Requirements"],
                            watering_frequency=row["Watering Frequency"],
                            soil_type=row["Soil Type"],
                            temperature_range=row["Temperature Range"],
                        )
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Added species: {generic_name} {specific_name}"
                            )
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Species already exists: {generic_name} {specific_name}"
                            )
                        )
            self.stdout.write(self.style.SUCCESS("Data loading completed!"))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {csv_file_path}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {str(e)}"))
