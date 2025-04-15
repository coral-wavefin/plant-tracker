from django.db import models
import requests

class Species(models.Model):
    generic_name = models.CharField(max_length=100, blank=True, default="")
    specific_name = models.CharField(max_length=100, blank=True, default="")
    common_name = models.CharField(max_length=100, blank=True, default="")
    light_requirements = models.CharField(max_length=100, blank=True, default="")
    watering_frequency = models.CharField(max_length=100, blank=True, default="")
    soil_type = models.CharField(max_length=100, blank=True, default="")
    temperature_range = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ["generic_name"]

    def __str__(self):
        return self.common_name


class Plant(models.Model):
    alias = models.CharField(max_length=100, blank=True, default="")
    price = models.FloatField()
    date_obtained = models.DateField()
    date_died = models.DateField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, default="")
    parent = models.ForeignKey(
        "self",
        related_name="children",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    species = models.ForeignKey(
        Species,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ["date_obtained"]

    def __str__(self):
        return self.alias

    # @property
    # def external_api_data(self):
    #     """
    #     Fetch data from unsplash
    #     """
    #     ACCESS_KEY = "YohVBmJIXZSS6J5zJPjiXLRxkk__787zSrs4ngWvsKg"
    #     SECRET_KEY = "2Pvtpou1boMqtzcJRo_yFEClwZXzMzh8Yf5qjSqnyv4"
    #     APPLICATION_ID = "734593"
    #     url = f"https://api.unsplash.com/photos/random?client_id={ACCESS_KEY}&query=plant&count=1"
    #     try:
    #         response = requests.get(
    #             url,
    #             # params={"query": self.id}
    #         )
    #         response.raise_for_status()
    #         return response.json()  # Return the API response as JSON
    #     except requests.RequestException as e:
    #         return {"error": str(e)}  # Handle errors gracefully

    
class Transfers(models.Model):
    plant_id = models.ForeignKey(
        Plant, on_delete=models.SET_DEFAULT, default=1, related_name="transfer"
    )
    date = models.DateField()
    price = models.FloatField()
    new_owner = models.CharField(max_length=100, blank=True, default="")
