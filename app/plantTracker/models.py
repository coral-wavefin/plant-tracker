from django.db import models


class Species(models.Model):
    generic_name = models.CharField(max_length=100, blank=True, default="")
    specific_name = models.CharField(max_length=100, blank=True, default="")
    common_name = models.CharField(max_length=100, blank=True, default="")

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
    next_owner = models.CharField(max_length=100, blank=True, default="")
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
