# Generated by Django 2.0.4 on 2018-06-03 18:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kochbuch', '0002_recipe_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='like',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
