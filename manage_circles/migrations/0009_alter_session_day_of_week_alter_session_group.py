# Generated by Django 5.0.4 on 2024-04-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_circles', '0008_club_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='day_of_week',
            field=models.CharField(choices=[('Pirmadienis', 'Pirmadienis'), ('Antradienis', 'Antradienis'), ('Trečiadienis', 'Trečiadienis'), ('Ketvirtadienis', 'Ketvirtadienis'), ('Penktadienis', 'Penktadienis'), ('Šeštadienis', 'Šeštadienis'), ('Sekmadienis', 'Sekmadienis')], max_length=20, verbose_name='Savaitės diena'),
        ),
        migrations.AlterField(
            model_name='session',
            name='group',
            field=models.CharField(choices=[('Priešmokyklinukai', 'Priešmokyklinukai'), ('Pirmokai – septintokai', 'Pirmokai – septintokai'), ('Priešmokyklinukai - pirmokai', 'Priešmokyklinukai - pirmokai'), ('Antrokai – septintokai', 'Antrokai – septintokai'), ('Pirmokai – šeštokai', 'Pirmokai – šeštokai'), ('Antrokai – ketvirtokai', 'Antrokai – ketvirtokai'), ('Pirmokai – ketvirtokai', 'Pirmokai – ketvirtokai'), ('Penktokai – septintokai', 'Penktokai – septintokai'), ('Penktokai – aštuntokai', 'Penktokai – aštuntokai'), ('Priešmokyklinukai - aštuntokai', 'Priešmokyklinukai - aštuntokai'), ('Naujokai ir oranžiniai diržai', 'Naujokai ir oranžiniai diržai'), ('Pažengę (nuo mėlynų juostelių) ir vyresni naujokai (9+ metų)', 'Pažengę (nuo mėlynų juostelių) ir vyresni naujokai (9+ metų)'), ('Trijų – keturių metų', 'Trijų – keturių metų'), ('Penkių – šešių metų', 'Penkių – šešių metų'), ('Septynių – dešimties metų', 'Septynių – dešimties metų'), ('Priešmokyklinukai (1 grupė)', 'Priešmokyklinukai (1 grupė)'), ('Priešmokyklinukai (2 grupė)', 'Priešmokyklinukai (2 grupė)')], max_length=100),
        ),
    ]
