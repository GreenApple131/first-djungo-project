# Generated by Django 2.1.5 on 2019-04-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Телефон'),
        ),
    ]