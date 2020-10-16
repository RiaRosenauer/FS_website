# Generated by Django 3.1.2 on 2020-10-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSapp', '0007_auto_20201016_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='preview',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='difficulty',
            field=models.CharField(choices=[('&#x1F534; &#x26AA; &#x26AA;', 'einfach'), ('&#x1F534; &#x1F534; &#x26AA;', 'mittel'), ('&#x1F534; &#x1F534; &#x1F534;', 'schwer')], default='e', max_length=40),
        ),
    ]