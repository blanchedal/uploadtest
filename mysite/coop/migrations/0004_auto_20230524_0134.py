# Generated by Django 3.1.3 on 2023-05-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0003_alter_coop_id_coopanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coop',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='coopanswer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
