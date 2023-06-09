# Generated by Django 4.2.1 on 2023-06-02 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_alter_conference_updated_at'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='conference',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='conferences.conference'),
            preserve_default=False,
        ),
    ]
