# Generated by Django 4.2 on 2024-07-16 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_alter_milage_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milage',
            name='moto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milage', to='vehicle.moto', verbose_name='мотоцикл'),
        ),
    ]
