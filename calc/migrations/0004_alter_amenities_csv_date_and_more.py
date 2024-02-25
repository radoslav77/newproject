# Generated by Django 4.1 on 2023-12-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_amenities_csv_alter_amenity_special_occasion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities_csv',
            name='date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='amenity',
            name='special_occasion',
            field=models.CharField(blank=True, choices=[('Small fruit', 'Small fruit'), ('VIP 4 ME', '4ME'), ('VIP 3 ME', '3ME'), ('Presidential', 'Presidential')], max_length=300, null=True),
        ),
    ]
