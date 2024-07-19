# Generated by Django 5.0.3 on 2024-07-15 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Darslar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan_nomi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Xonalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Oqtuvchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=40)),
                ('oylik', models.CharField(max_length=100)),
                ('oquvchilar', models.IntegerField()),
                ('fani', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oqtuvchilar_fani', to='blog.darslar')),
                ('xonasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.xonalar')),
            ],
        ),
        migrations.CreateModel(
            name='Oquvchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=40)),
                ('davomati', models.CharField(max_length=50)),
                ('tolov', models.CharField(max_length=100)),
                ('fani', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.darslar')),
            ],
        ),
        migrations.CreateModel(
            name='Davomat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.CharField(max_length=100)),
                ('oqtuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='davomat_oqtuvchi', to='blog.oqtuvchilar')),
                ('oquvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='davomat_oquvchi', to='blog.oquvchilar')),
            ],
        ),
        migrations.CreateModel(
            name='Oylik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oquvchilar_soni', models.CharField(max_length=100)),
                ('oqtuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oylik_oqtuvchi', to='blog.oqtuvchilar')),
                ('tolov_miqdori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oylik_tolov_miqdori', to='blog.davomat')),
            ],
        ),
        migrations.CreateModel(
            name='Qabulxona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelgan_oquvchi', models.CharField(max_length=100)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qabulxona_admin', to='blog.oqtuvchilar')),
                ('royxat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qabulxona_royxat', to='blog.oquvchilar')),
            ],
        ),
        migrations.CreateModel(
            name='Tolovlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tolov_miqdori', models.CharField(max_length=100)),
                ('tolovgan_miqdor', models.CharField(max_length=50)),
                ('oquvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.oquvchilar')),
            ],
        ),
        migrations.AddField(
            model_name='davomat',
            name='keldi_kelmadi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='davomat_keldi_kelmadi', to='blog.tolovlar'),
        ),
    ]
