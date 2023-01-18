# Generated by Django 4.0.1 on 2023-01-12 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='issue_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_description', models.TextField()),
                ('date_created', models.DateField()),
                ('created_by', models.CharField(max_length=15)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=20)),
                ('created_by', models.CharField(max_length=100)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_number', models.CharField(max_length=15)),
                ('lr_number', models.CharField(max_length=15)),
                ('parcel_active_status', models.CharField(max_length=15)),
                ('survey_parcel_no', models.CharField(max_length=15)),
                ('survey_status', models.BooleanField(default=False)),
                ('survey_comment', models.TextField()),
                ('land_admin_parcel_no', models.CharField(max_length=15)),
                ('land_admin_parcel_status', models.BooleanField(default=False)),
                ('land_admin_comment', models.TextField()),
                ('land_reg_parcel_no', models.CharField(max_length=15)),
                ('land_reg_status', models.BooleanField(default=False)),
                ('land_reg_comment', models.TextField()),
                ('registered', models.BooleanField(default=False)),
                ('tenure', models.BooleanField(default=False)),
                ('ownership', models.BooleanField(default=False)),
                ('waterfall', models.BooleanField(default=False)),
                ('post_2015_comment', models.TextField()),
                ('date_created', models.DateField()),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='issue_remarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField()),
                ('created_by', models.CharField(max_length=100)),
                ('date_created', models.DateField()),
                ('issue_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annomalies.issue_details')),
            ],
        ),
        migrations.AddField(
            model_name='issue_details',
            name='issue_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annomalies.issues'),
        ),
        migrations.AddField(
            model_name='issue_details',
            name='parcel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annomalies.parcel'),
        ),
    ]