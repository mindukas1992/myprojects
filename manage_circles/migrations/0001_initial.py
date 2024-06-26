# Generated by Django 5.0.4 on 2024-04-11 08:19

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
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Vaiko_vardas')),
                ('last_name', models.CharField(max_length=50, verbose_name='Vaiko_pavardė')),
                ('child_age', models.IntegerField(verbose_name='Vaiko_metai')),
                ('school', models.CharField(max_length=100, verbose_name='Mokykla')),
                ('classroom', models.CharField(max_length=50, verbose_name='Klasė/grupė')),
            ],
        ),
        migrations.CreateModel(
            name='Circles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('children', models.ManyToManyField(related_name='circles', to='manage_circles.child')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Vardas')),
                ('last_name', models.CharField(max_length=50, verbose_name='Pavardė')),
                ('email', models.CharField(max_length=50, verbose_name='El_paštas')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Telefono_numeris')),
                ('address', models.CharField(max_length=200, verbose_name='Adresas')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='manage_circles.parent'),
        ),
    ]
