from django.db import models

class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "Products"


class Crop(models.Model):
    crop_id = models.BigAutoField(primary_key=True)

    # FK externas, obtenidas por endpoint
    user_id = models.BigIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    start_date = models.DateField()
    harvest_date = models.DateField()
    area = models.FloatField()

    class Meta:
        db_table = "Crop"
