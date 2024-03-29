# Generated by Django 4.1 on 2023-12-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_alter_amenities_csv_iventory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities_csv',
            name='iventory',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='amenities_csv',
            name='reserved',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='amenity',
            name='special_occasion',
            field=models.CharField(blank=True, choices=[('VIP 3 ME', '3ME'), ('Presidential', 'Presidential'), ('Small fruit', 'Small fruit'), ('VIP 4 ME', '4ME')], max_length=300, null=True),
        ),
    ]
