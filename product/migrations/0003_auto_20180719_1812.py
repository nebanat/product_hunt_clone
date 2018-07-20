# Generated by Django 2.0.6 on 2018-07-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180719_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='product.Category'),
        ),
    ]
