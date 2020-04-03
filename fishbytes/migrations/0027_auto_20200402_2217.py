# Generated by Django 3.0.5 on 2020-04-02 22:17

from django.db import migrations, models
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('fishbytes', '0026_auto_20200402_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catch',
            name='location',
        ),
        migrations.AddField(
            model_name='catch',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='catch',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='lake',
            name='location',
            field=mapbox_location_field.models.LocationField(blank=True, map_attrs={'center': [0, 0], 'marker_color': 'pink'}, null=True),
        ),
    ]