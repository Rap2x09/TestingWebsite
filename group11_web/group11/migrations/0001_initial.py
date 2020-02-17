# Generated by Django 2.2.10 on 2020-02-14 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problemID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('problemInfo', models.TextField(verbose_name='Problem Details')),
                ('evaluationCode', models.TextField(verbose_name='Evaluation Code')),
                ('isValid', models.BooleanField(default=False, verbose_name='Valid?')),
                ('isReleased', models.BooleanField(default=False, verbose_name='Released?')),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('dataID', models.AutoField(primary_key=True, serialize=False)),
                ('dataset', models.FileField(upload_to='datasets/')),
                ('datasetDesc', models.CharField(max_length=100, verbose_name='Dataset Short Description')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group11.Problem')),
            ],
        ),
    ]
