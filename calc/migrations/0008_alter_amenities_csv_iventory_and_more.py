# Generated by Django 4.1 on 2023-12-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_alter_amenities_csv_iventory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities_csv',
            name='iventory',
            field=models.CharField(default=100, max_length=200),
        ),
        migrations.AlterField(
            model_name='amenities_csv',
            name='reserved',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='amenity',
            name='special_occasion',
            field=models.CharField(blank=True, choices=[('Presidential', 'Presidential'), ('VIP 4 ME', '4ME'), ('VIP 3 ME', '3ME'), ('Small fruit', 'Small fruit')], max_length=300, null=True),
        ),
    ]
