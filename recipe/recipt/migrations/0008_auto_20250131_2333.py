# Generated by Django 2.2.19 on 2025-01-31 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipt', '0007_auto_20250131_0314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe_ingredient',
            old_name='amount',
            new_name='Quantity_in_grams',
        ),
    ]
