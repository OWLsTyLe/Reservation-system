# Generated by Django 5.1.4 on 2025-01-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(max_length=500)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=5)),
            ],
        ),
    ]
