# Generated by Django 2.0.6 on 2018-07-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180719_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='product.Category'),
        ),
    ]
