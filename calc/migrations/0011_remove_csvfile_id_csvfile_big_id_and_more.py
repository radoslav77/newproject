# Generated by Django 4.1 on 2024-02-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0010_replenishment_alter_amenity_special_occasion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfile',
            name='id',
        ),
        migrations.AddField(
            model_name='csvfile',
            name='big_id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='amenity',
            name='special_occasion',
            field=models.CharField(blank=True, choices=[('VIP4ME', 'VIP4ME'), ('VIP6', 'VIP6'), ('None', 'None'), ('VIP4', 'VIP4'), ('VIP2', 'VIP2'), ('VIP5', 'VIP5'), ('VIP5ME', 'VIP5ME'), ('VIP1', 'VIP1'), ('Presidential', 'Presidential'), ('VIP3ME', 'VIP3ME'), ('VIP3', 'VIP3')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='spacial_amenities',
            name='amenity_code',
            field=models.CharField(blank=True, choices=[('VIP4ME', 'VIP4ME'), ('VIP6', 'VIP6'), ('None', 'None'), ('VIP4', 'VIP4'), ('VIP2', 'VIP2'), ('VIP5', 'VIP5'), ('VIP5ME', 'VIP5ME'), ('VIP1', 'VIP1'), ('Presidential', 'Presidential'), ('VIP3ME', 'VIP3ME'), ('VIP3', 'VIP3')], max_length=150),
        ),
        migrations.AlterField(
            model_name='spacial_amenities',
            name='amenity_type',
            field=models.CharField(blank=True, choices=[('8" cake', '8" cake'), ('Honeymoon cake', 'Honeymoon cake'), ('6" cake', '6" cake'), ('Special amenities', 'Special amenities'), ('Sliced fruit platter', 'Sliced fruit platter'), ('Birthady cake', 'Birthady cake'), ('Celebration cake', 'Celebration cake'), ('Canapes', 'Canapes'), ('Aniversary cake', 'Aniversary cake')], max_length=250),
        ),
        migrations.AlterField(
            model_name='spacial_amenities',
            name='day_of_week',
            field=models.CharField(blank=True, choices=[('Tuesday', 'Tuesday'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Friday', 'Friday'), ('Thursday', 'Thursday'), ('Saturday', 'Saturday'), ('Wednesday', 'Wednesday')], max_length=200),
        ),
    ]
