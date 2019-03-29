# Generated by Django 2.1.7 on 2019-03-26 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('link', models.TextField()),
                ('comment', models.TextField()),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.Topic')),
            ],
        ),
    ]
