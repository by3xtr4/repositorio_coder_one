# Generated by Django 3.2.13 on 2022-06-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCoder', '0003_delete_integrantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Integrantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha', models.TimeField()),
            ],
        ),
    ]