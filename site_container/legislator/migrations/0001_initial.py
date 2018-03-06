# Generated by Django 2.0.2 on 2018-03-05 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('industry', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lawmaker',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('party', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=2)),
                ('body', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('disclosure_url', models.URLField(null=True)),
                ('lawmaker_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cpi_2015', models.BooleanField(default=False)),
                ('non_standard_FI', models.TextField(default='')),
                ('non_standard_IN', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='OpenCorps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('company_number', models.CharField(max_length=25)),
                ('company_type', models.CharField(max_length=25, null=True)),
                ('incorporation_date', models.CharField(max_length=25, null=True)),
                ('opencorporates_url', models.URLField(null=True)),
                ('alternative_names', models.TextField(null=True)),
                ('registered_address_in_full', models.TextField(null=True)),
                ('registry_url', models.URLField(null=True)),
                ('ultimate_beneficial_owners', models.TextField(null=True)),
                ('finterest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislator.FinancialInterest')),
            ],
        ),
        migrations.AddField(
            model_name='financialinterest',
            name='lawmaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislator.Lawmaker'),
        ),
    ]