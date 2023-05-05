# Generated by Django 3.2.18 on 2023-05-05 13:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='type name')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create time')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='update time')),
            ],
            options={
                'verbose_name': 'product brand',
                'verbose_name_plural': 'product brand',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('describe', models.TextField(verbose_name='describe')),
                ('inventory', models.IntegerField(default=0, verbose_name='inventory')),
                ('price', models.IntegerField(default=0, verbose_name='inventory')),
                ('image', models.FileField(upload_to='good_image', verbose_name='image')),
                ('Gender', models.CharField(default='', max_length=100, verbose_name='Gender')),
                ('Description', models.TextField(default='', verbose_name='Description')),
                ('PrimaryColor', models.CharField(default='', max_length=100, verbose_name='PrimaryColor')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create time')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='update time')),
                ('product_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='product.productbrand', verbose_name='product_brand')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'product',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=100, verbose_name='order_num')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('number', models.IntegerField(default=0, verbose_name='number')),
                ('image', models.FileField(upload_to='good_image', verbose_name='image')),
                ('total_price', models.IntegerField(default=0, verbose_name='total_price')),
                ('status', models.CharField(max_length=100, verbose_name='status')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create time')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='update time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user.user', verbose_name='user')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'order',
            },
        ),
    ]
