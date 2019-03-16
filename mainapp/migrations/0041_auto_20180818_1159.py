# Generated by Django 2.1 on 2018-08-18 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0040_auto_20180818_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescuecamp',
            name='data_entry_user',
            field=models.ForeignKey(blank=True, help_text="This camp's coordinator page will be visible only to this user", null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
