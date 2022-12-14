# Generated by Django 4.0.6 on 2022-07-27 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("url_shortener_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unshortenlink",
            name="original_link",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="unshortenlink",
            name="shortened_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
