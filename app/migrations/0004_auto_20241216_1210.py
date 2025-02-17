# Generated by Django 3.1.4 on 2024-12-16 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_book_coustomer_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coustomer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.coustomer'),
        ),
        migrations.AlterField(
            model_name='book',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.room'),
        ),
        migrations.AlterField(
            model_name='coustomer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hotel'),
        ),
    ]
