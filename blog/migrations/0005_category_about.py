# Generated by Django 5.0.4 on 2024-04-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_rename_categories_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="about",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="О категории"
            ),
        ),
    ]