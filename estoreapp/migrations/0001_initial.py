# Generated by Django 4.2.7 on 2023-11-29 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOKDETAILS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('Sellingprice', models.IntegerField(default=0)),
                ('Discountprice', models.IntegerField(default=0)),
                ('Discription', models.TextField(max_length=1000)),
                ('Language', models.CharField(choices=[('ENGLISH', 'EN'), ('MALAYALAM', 'ML')], max_length=100)),
                ('Product', models.CharField(max_length=100)),
                ('Category', models.CharField(choices=[('NV', 'NOVELS'), ('PT', 'POETRY'), ('SR', 'STORY'), ('CD', 'CHILDRENS'), ('SC', 'SCIENCE'), ('AT', 'AUTOBIOGRAPHY')], max_length=2)),
                ('Productimage', models.ImageField(upload_to='productimage')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('First_name', models.CharField(max_length=10)),
                ('Last_name', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=20, unique=True)),
                ('Phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'customerdetails',
            },
        ),
        migrations.CreateModel(
            name='Customerprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('Mobile', models.IntegerField(default=0)),
                ('Pincode', models.IntegerField(default=0)),
                ('State', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AS', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JH', 'Jharkhand'), ('JK', 'Jammu and Kashmir'), ('KA', 'Karnataka'), ('Kerala', 'KL'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PB', 'Punjab'), ('PY', 'Puducherry'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TR', 'Tripura'), ('TG', 'Telangana'), ('UP', 'Uttar Pradesh'), ('UT', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.customer')),
            ],
            options={
                'db_table': 'Customerprofile',
            },
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.bookdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='pending', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.customerprofile')),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='estoreapp.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.bookdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CODOrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('tracking_no', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='pending', max_length=100)),
                ('payment', models.CharField(max_length=250, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.bookdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.bookdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoreapp.customer')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]