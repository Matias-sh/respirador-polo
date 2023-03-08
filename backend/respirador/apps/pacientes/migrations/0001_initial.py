# Generated by Django 4.1.7 on 2023-03-06 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('sintomas', models.CharField(max_length=200)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.personas')),
            ],
        ),
    ]
