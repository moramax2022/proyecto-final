# Generated by Django 4.1.4 on 2022-12-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0002_alumnos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('asignatura', models.CharField(max_length=50)),
                ('grado', models.IntegerField()),
            ],
        ),
    ]
