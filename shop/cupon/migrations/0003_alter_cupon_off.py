# Generated by Django 3.2.5 on 2021-08-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupon', '0002_cupon_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupon',
            name='off',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
