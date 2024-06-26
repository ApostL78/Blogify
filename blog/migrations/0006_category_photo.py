# Generated by Django 5.0.4 on 2024-04-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_category_about"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="photo",
            field=models.ImageField(
                default="No photo",
                upload_to="categories/%Y/%m/%d/",
                verbose_name="Фото",
            ),
        ),
    ]
