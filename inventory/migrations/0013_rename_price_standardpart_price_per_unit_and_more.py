# Generated by Django 4.0.4 on 2022-05-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_processcost_primary_cost_processcost_secondary_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standardpart',
            old_name='price',
            new_name='price_per_unit',
        ),
        migrations.AddField(
            model_name='standardpart',
            name='leadtime',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='standardpart',
            name='moq',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='standardpart',
            name='remarks',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='standardpart',
            name='update',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
