# Generated by Django 2.2 on 2019-04-21 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20190422_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='fifth',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_fifth', to='board.Racer'),
        ),
        migrations.AlterField(
            model_name='race',
            name='first',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_first', to='board.Racer'),
        ),
        migrations.AlterField(
            model_name='race',
            name='fourth',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_fourth', to='board.Racer'),
        ),
        migrations.AlterField(
            model_name='race',
            name='second',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_second', to='board.Racer'),
        ),
        migrations.AlterField(
            model_name='race',
            name='third',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='racer_third', to='board.Racer'),
        ),
    ]
