# Generated by Django 2.2 on 2019-04-21 21:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Racer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name_r', models.CharField(max_length=200)),
                ('name_t', models.CharField(max_length=200)),
                ('desc_c', models.CharField(max_length=1000)),
                ('desc_r', models.CharField(max_length=1000)),
                ('exp_r', models.CharField(choices=[('b', 'Beginner'), ('i', 'Intermediate'), ('e', 'Experienced'), ('p', 'Professional')], default='b', max_length=1)),
                ('class_r', models.CharField(choices=[('fo', 'Fourth'), ('th', 'Third'), ('sc', 'Second'), ('fi', 'First')], default='fo', max_length=2)),
            ],
            options={
                'ordering': ['name_t'],
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('fifth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_fifth', to='board.Racer')),
                ('first', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_first', to='board.Racer')),
                ('fouth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_fourth', to='board.Racer')),
                ('second', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_second', to='board.Racer')),
                ('third', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_third', to='board.Racer')),
            ],
        ),
    ]