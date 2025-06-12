from django.db import models



class Car(models.Model):
    name = models.CharField(max_length=200)
    brend = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'car'

    def __str__(self):
        return self.name
