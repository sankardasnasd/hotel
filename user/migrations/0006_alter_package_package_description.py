# Generated by Django 4.1.2 on 2023-01-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_package"),
    ]

    operations = [
        migrations.AlterField(
            model_name="package",
            name="Package_description",
            field=models.CharField(max_length=100),
        ),
    ]
