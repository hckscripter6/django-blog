# Generated by Django 2.0.1 on 2018-12-12 01:33

from django.db import migrations, models
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(bucket='hckrieger-app'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
