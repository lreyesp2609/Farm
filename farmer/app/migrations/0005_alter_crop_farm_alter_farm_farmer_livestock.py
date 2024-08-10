# Generated by Django 5.0.2 on 2024-02-28 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_farm_id_crop_farm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crops', to='app.farm'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farms', to='app.farmer'),
        ),
        migrations.CreateModel(
            name='Livestock',
            fields=[
                ('livestock_id', models.AutoField(primary_key=True, serialize=False)),
                ('livestock_type', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('health_status', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.farm')),
            ],
        ),
    ]
