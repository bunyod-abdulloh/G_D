# Generated by Django 3.2.8 on 2024-05-28 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0010_auto_20240529_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='table_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_number', models.IntegerField(unique=True, verbose_name='Dars tartib raqami')),
                ('file_id', models.CharField(max_length=50, verbose_name='File ID')),
                ('file_name', models.CharField(max_length=150, null=True, verbose_name='File Name')),
                ('file_type', models.CharField(max_length=10, null=True, verbose_name='File Type')),
                ('caption', models.CharField(max_length=4000, null=True, verbose_name='Caption')),
            ],
            options={
                'verbose_name': 'Psixoterapiya va psixologiya asoslari',
                'verbose_name_plural': 'Psixoterapiya va psixologiya asoslari',
            },
        ),
        migrations.CreateModel(
            name='table_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_number', models.IntegerField(null=True, unique=True, verbose_name='Dars tartib raqami')),
                ('file_id', models.CharField(max_length=50, verbose_name='File ID')),
                ('file_name', models.CharField(max_length=150, null=True, verbose_name='File Name')),
                ('file_type', models.CharField(max_length=10, null=True, verbose_name='File Type')),
                ('caption', models.CharField(max_length=4000, null=True, verbose_name='Caption')),
            ],
            options={
                'verbose_name': 'Tabobat va tibbiyotda mijoz va tepmerament ilmi',
                'verbose_name_plural': 'Tabobat va tibbiyotda mijoz va tepmerament ilmi',
            },
        ),
        migrations.DeleteModel(
            name='Psixoterapiya_Psixologiya',
        ),
        migrations.DeleteModel(
            name='Tabobat_Tibbiyot',
        ),
        migrations.AlterModelOptions(
            name='farzandim_jigarbandim',
            options={'verbose_name': 'Farzandim va jigarbandim', 'verbose_name_plural': 'Farzandim va jigarbandim'},
        ),
        migrations.AddField(
            model_name='farzandim_jigarbandim',
            name='lesson_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Dars tartib raqami'),
        ),
        migrations.AddField(
            model_name='miya_neyroplastik',
            name='lesson_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Dars tartib raqami'),
        ),
        migrations.AddField(
            model_name='nafs_diagnostikasi',
            name='lesson_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Dars tartib raqami'),
        ),
        migrations.AddField(
            model_name='ruhiy_salomatlik',
            name='lesson_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Dars tartib raqami'),
        ),
        migrations.AddField(
            model_name='sharq_psixologiyasi',
            name='lesson_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Dars tartib raqami'),
        ),
        migrations.AddField(
            model_name='talim_ruhiyat',
            name='lesson_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Dars tartib raqami'),
        ),
        migrations.AlterField(
            model_name='farzandim_jigarbandim',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='File ID'),
        ),
        migrations.AlterField(
            model_name='farzandim_jigarbandim',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='File Type'),
        ),
        migrations.AlterField(
            model_name='farzandim_jigarbandim',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='miya_neyroplastik',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='File ID'),
        ),
        migrations.AlterField(
            model_name='miya_neyroplastik',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='File Type'),
        ),
        migrations.AlterField(
            model_name='miya_neyroplastik',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='nafs_diagnostikasi',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='File ID'),
        ),
        migrations.AlterField(
            model_name='nafs_diagnostikasi',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='File Type'),
        ),
        migrations.AlterField(
            model_name='nafs_diagnostikasi',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ruhiy_salomatlik',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='File ID'),
        ),
        migrations.AlterField(
            model_name='ruhiy_salomatlik',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='File Type'),
        ),
        migrations.AlterField(
            model_name='ruhiy_salomatlik',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sharq_psixologiyasi',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='File ID'),
        ),
        migrations.AlterField(
            model_name='sharq_psixologiyasi',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='File Type'),
        ),
        migrations.AlterField(
            model_name='sharq_psixologiyasi',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='talim_ruhiyat',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='File ID'),
        ),
        migrations.AlterField(
            model_name='talim_ruhiyat',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='File Type'),
        ),
        migrations.AlterField(
            model_name='talim_ruhiyat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
