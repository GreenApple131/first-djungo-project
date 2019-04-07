# Generated by Django 2.1.5 on 2019-04-07 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_pizza_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Ім`я')),
                ('phone', models.CharField(max_length=30, verbose_name='Тулуфон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Pizza', verbose_name='Піца')),
            ],
        ),
    ]
