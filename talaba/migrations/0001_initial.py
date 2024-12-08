# Generated by Django 5.1.4 on 2024-12-08 06:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestNatija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball', models.IntegerField()),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Test Natija',
                'verbose_name_plural': 'Test Natijalar',
            },
        ),
    ]