# Generated by Django 3.0.4 on 2020-03-28 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fishbytes', '0016_merge_20200328_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='catch',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='catch',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='fish',
            name='img',
            field=models.ImageField(upload_to='fish/'),
        ),
    ]