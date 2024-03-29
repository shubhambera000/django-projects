# Generated by Django 2.2.6 on 2019-10-02 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('adress', models.CharField(max_length=250)),
                ('Email_id', models.EmailField(blank=True, default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CGPA', models.IntegerField()),
                ('Roll_no', models.CharField(max_length=30)),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friend.Details')),
            ],
        ),
    ]
