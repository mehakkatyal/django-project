# Generated by Django 3.1.4 on 2024-12-16 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20241205_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(unique=True)),
                ('room_type', models.CharField(max_length=100)),
                ('price_per_night', models.DecimalField(decimal_places=10, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='coustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('Adress', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('number_of_guest', models.IntegerField()),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('coustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coustomer')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
            ],
        ),
    ]
