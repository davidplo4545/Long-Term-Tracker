# Generated by Django 3.2.4 on 2021-07-23 11:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_shared', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('started_at', models.DateField(blank=True, null=True)),
                ('realized_gain', models.FloatField(default=0)),
                ('total_value', models.FloatField(blank=True, default=0, editable=False)),
                ('total_cost', models.FloatField(blank=True, default=0, editable=False)),
            ],
            options={
                'ordering': ('started_at',),
            },
        ),
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.asset')),
                ('symbol', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('last_price', models.FloatField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
            bases=('api.asset',),
        ),
        migrations.CreateModel(
            name='IsraelPaper',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.asset')),
                ('paper_id', models.IntegerField()),
                ('type', models.CharField(choices=[('ETF', 'ETF'), ('STOCK', 'STOCK')], default='STOCK', max_length=9)),
                ('name', models.CharField(max_length=120)),
                ('symbol', models.CharField(blank=True, max_length=30, null=True)),
                ('last_price', models.FloatField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
            bases=('api.asset',),
        ),
        migrations.CreateModel(
            name='USPaper',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.asset')),
                ('type', models.CharField(choices=[('ETF', 'ETF'), ('STOCK', 'STOCK')], default='STOCK', max_length=9)),
                ('name', models.CharField(max_length=120)),
                ('symbol', models.CharField(max_length=6)),
                ('last_price', models.FloatField(blank=True, null=True)),
                ('sector', models.CharField(blank=True, max_length=200, null=True)),
                ('industry', models.CharField(blank=True, max_length=200, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
            bases=('api.asset',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=125)),
                ('last_name', models.CharField(blank=True, max_length=125)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.portfolio')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='PortfolioComparison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comparisons', to='api.asset')),
                ('asset_portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_comparisons', to='api.portfolio')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_comparisons', to='api.portfolio')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_comparisons', to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], default='BUY', max_length=4)),
                ('quantity', models.FloatField(default=0)),
                ('share_price', models.FloatField(default=0)),
                ('total_cost', models.FloatField(blank=True, default=0, editable=False)),
                ('completed_at', models.DateField(default=datetime.date.today)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='api.asset')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='api.portfolio')),
            ],
            options={
                'ordering': ('completed_at',),
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to='api.profile'),
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('cost_basis', models.FloatField(blank=True)),
                ('total_cost', models.FloatField(blank=True, default=0)),
                ('total_value', models.FloatField(blank=True, default=0, editable=False)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holdings', to='api.asset')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holdings', to='api.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='AssetRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.asset')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
