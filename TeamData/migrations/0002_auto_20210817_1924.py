# Generated by Django 3.2.6 on 2021-08-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='Picture',
            new_name='picture',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Team',
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='team',
            field=models.ManyToManyField(to='TeamData.Team'),
        ),
    ]
