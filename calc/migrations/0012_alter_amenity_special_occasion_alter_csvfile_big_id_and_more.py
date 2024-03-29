# Generated by Django 4.1 on 2024-02-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0011_remove_csvfile_id_csvfile_big_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='special_occasion',
            field=models.CharField(blank=True, choices=[('VIP2', 'VIP2'), ('VIP4', 'VIP4'), ('VIP4ME', 'VIP4ME'), ('VIP3', 'VIP3'), ('None', 'None'), ('VIP1', 'VIP1'), ('VIP3ME', 'VIP3ME'), ('VIP6', 'VIP6'), ('VIP5', 'VIP5'), ('VIP5ME', 'VIP5ME'), ('Presidential', 'Presidential')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='big_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spacial_amenities',
            name='amenity_code',
            field=models.CharField(blank=True, choices=[('VIP2', 'VIP2'), ('VIP4', 'VIP4'), ('VIP4ME', 'VIP4ME'), ('VIP3', 'VIP3'), ('None', 'None'), ('VIP1', 'VIP1'), ('VIP3ME', 'VIP3ME'), ('VIP6', 'VIP6'), ('VIP5', 'VIP5'), ('VIP5ME', 'VIP5ME'), ('Presidential', 'Presidential')], max_length=150),
        ),
        migrations.AlterField(
            model_name='spacial_amenities',
            name='amenity_type',
            field=models.CharField(blank=True, choices=[('Sliced fruit platter', 'Sliced fruit platter'), ('Celebration cake', 'Celebration cake'), ('Birthady cake', 'Birthady cake'), ('Canapes', 'Canapes'), ('Aniversary cake', 'Aniversary cake'), ('8" cake', '8" cake'), ('Special amenities', 'Special amenities'), ('6" cake', '6" cake'), ('Honeymoon cake', 'Honeymoon cake')], max_length=250),
        ),
        migrations.AlterField(
            model_name='spacial_amenities',
            name='day_of_week',
            field=models.CharField(blank=True, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday'), ('Tuesday', 'Tuesday'), ('Saturday', 'Saturday'), ('Friday', 'Friday'), ('Thursday', 'Thursday')], max_length=200),
        ),
    ]
