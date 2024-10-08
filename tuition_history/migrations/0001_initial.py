# Generated by Django 5.0.6 on 2024-09-11 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tuitions', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTuitionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Selected', 'Selected')], default='Pending', max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('tuition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuitions.tuitions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usermodel')),
            ],
        ),
    ]
