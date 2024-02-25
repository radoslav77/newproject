# Generated by Django 4.1 on 2023-12-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('big_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('date_of_arrival', models.CharField(max_length=100)),
                ('date_of_departure', models.CharField(max_length=100)),
                ('num_of_fruit', models.IntegerField(blank=True, default=1, null=True)),
                ('day_of_week', models.CharField(max_length=200)),
                ('item_code', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('special_occasion', models.CharField(blank=True, choices=[('VIP 4 ME', '4ME'), ('VIP 3 ME', '3ME'), ('Small fruit', 'Small fruit'), ('Presidential', 'Presidential')], max_length=300, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
