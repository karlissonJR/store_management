from django.db import models
from django.contrib.auth import get_user_model

class Product(models.Model):
    name = models.CharField('nome', max_length=50)
    description = models.CharField('descrição', max_length=300)
    price = models.DecimalField('preço', max_digits=9, decimal_places=2)
    quantity = models.IntegerField('quantidade')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name