# Generated by Django 5.0 on 2024-01-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('id_categoria', models.IntegerField()),
                ('id_marca', models.IntegerField()),
                ('precio', models.FloatField()),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion_corta', models.CharField(max_length=60)),
                ('descripcion_amplia', models.TextField(max_length=500)),
                ('id_usuario', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductosCategorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ProductosEvaluaciones',
            fields=[
                ('id_producto_comentario', models.AutoField(primary_key=True, serialize=False)),
                ('id_producto', models.IntegerField()),
                ('comentario', models.CharField(max_length=255)),
                ('calificacion', models.IntegerField()),
                ('id_usuario', models.IntegerField()),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductosEvaluacionesEstados',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductosImagenes',
            fields=[
                ('id_producto_imagen', models.AutoField(primary_key=True, serialize=False)),
                ('id_producto', models.IntegerField()),
                ('imagen', models.CharField(max_length=45)),
                ('orden', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductosMarcas',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ProductosTalles',
            fields=[
                ('id_talle', models.AutoField(primary_key=True, serialize=False)),
                ('talle', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductosTallesDiponibles',
            fields=[
                ('id_talle_diponilbe', models.AutoField(primary_key=True, serialize=False)),
                ('id_producto', models.IntegerField()),
                ('id_talle', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
