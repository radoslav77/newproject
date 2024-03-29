# Generated by Django 4.1 on 2024-02-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_alter_amenities_csv_iventory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spacial_Amenities',
            fields=[
                ('big_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('arrival_date', models.DateField()),
                ('day_of_week', models.CharField(blank=True, choices=[('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Tuesday', 'Tuesday'), ('Monday', 'Monday')], max_length=200)),
                ('amenity_type', models.CharField(blank=True, choices=[('Canapes', 'Canapes'), ('6" cake', '6" cake'), ('8" cake', '8" cake'), ('Aniversary cake', 'Aniversary cake'), ('Honeymoon cake', 'Honeymoon cake'), ('Sliced fruit platter', 'Sliced fruit platter'), ('Celebration cake', 'Celebration cake'), ('Birthady cake', 'Birthady cake'), ('Special amenities', 'Special amenities')], max_length=250)),
                ('amenity_code', models.CharField(blank=True, choices=[('VIP2', 'VIP2'), ('VIP1', 'VIP1'), ('VIP6', 'VIP6'), ('VIP4ME', 'VIP4ME'), ('VIP3', 'VIP3'), ('VIP4', 'VIP4'), ('None', 'None'), ('VIP5ME', 'VIP5ME'), ('Presidential', 'Presidential'), ('VIP3ME', 'VIP3ME'), ('VIP5', 'VIP5')], max_length=150)),
                ('amenity_amount', models.IntegerField(default=0)),
                ('date_of_input', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='amenity',
            name='special_occasion',
            field=models.CharField(blank=True, choices=[('VIP2', 'VIP2'), ('VIP1', 'VIP1'), ('VIP6', 'VIP6'), ('VIP4ME', 'VIP4ME'), ('VIP3', 'VIP3'), ('VIP4', 'VIP4'), ('None', 'None'), ('VIP5ME', 'VIP5ME'), ('Presidential', 'Presidential'), ('VIP3ME', 'VIP3ME'), ('VIP5', 'VIP5')], max_length=300, null=True),
        ),
    ]
