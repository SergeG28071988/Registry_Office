from django.db import models

# Модель браки 
class Marriage(models.Model):
    groom = models.CharField(max_length=100)
    bride = models.CharField(max_length=100)
    marriage_date = models.DateField()

    def __str__(self):
        return f'{self.groom} and {self.bride} ({self.marriage_date})'

# Модель Разводы 
class Divorce(models.Model):
    husband = models.CharField(max_length=100)
    wife = models.CharField(max_length=100)
    divorce_date = models.DateField()

    def __str__(self):
        return f'{self.husband} and {self.wife} ({self.divorce_date})'
