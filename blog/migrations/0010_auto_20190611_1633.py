# Generated by Django 2.2.1 on 2019-06-11 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_postpages_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpages',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
