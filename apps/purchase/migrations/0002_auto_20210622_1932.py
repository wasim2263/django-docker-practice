# Generated by Django 3.1.12 on 2021-06-22 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0002_auto_20210618_1535'),
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='customer.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='purchase.invoice'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='product.product'),
        ),
    ]
