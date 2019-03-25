from django.db import models

# Create your models here.


class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Піцерія')
    description = models.TextField(verbose_name='Опис')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Інтернет-адреса піцерії')

    class Meta:
        verbose_name = 'Піцерія'
        verbose_name_plural = 'Піцерії'

    def __str__(self):
        return self.name


class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Назва піци')
    short_description = models.CharField(max_length=30, verbose_name='Короткий опис')
    price = models.IntegerField(default=0, verbose_name='Ціна')

    class Meta:
        verbose_name = 'Піца'
        verbose_name_plural = 'Піци'
        ordering = ['price']

    def __str__(self):
        return self.name