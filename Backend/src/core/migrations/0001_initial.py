# Generated by Django 2.1.4 on 2020-04-11 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NA', max_length=100, verbose_name='name')),
                ('amount', models.FloatField(default=0.0, verbose_name='amount')),
                ('cashflow', models.CharField(default='NA', max_length=2, verbose_name='cashflow')),
                ('category', models.CharField(default='NA', max_length=2, verbose_name='category')),
                ('interval', models.CharField(default='N', max_length=2, verbose_name='interval')),
                ('description', models.TextField(default='NA', verbose_name='description')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
