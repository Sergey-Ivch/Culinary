# Generated by Django 2.2.19 on 2025-02-05 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipt', '0010_comment_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estimation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimation', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='recipt.Estimation'),
        ),
    ]
