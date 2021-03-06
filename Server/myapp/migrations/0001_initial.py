# Generated by Django 2.2 on 2019-05-24 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=75, null=True)),
            ],
            options={
                'db_table': 'market',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('mname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ingredient', models.CharField(blank=True, max_length=500, null=True)),
                ('dimage', models.CharField(blank=True, max_length=75, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pw', models.CharField(blank=True, max_length=45, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('recipe_menu', models.ForeignKey(db_column='recipe_menu', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.Menu')),
                ('dirkey', models.IntegerField()),
                ('direction', models.CharField(blank=True, max_length=170, null=True)),
            ],
            options={
                'db_table': 'direction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DirImage',
            fields=[
                ('recipe_menu', models.ForeignKey(db_column='recipe_menu', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.Menu')),
                ('imgkey', models.IntegerField()),
                ('dir_image', models.CharField(blank=True, max_length=75, null=True)),
            ],
            options={
                'db_table': 'dir_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuInfo',
            fields=[
                ('recipe_menu', models.ForeignKey(db_column='recipe_menu', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.Menu')),
                ('how_make', models.CharField(blank=True, max_length=10, null=True)),
                ('sort', models.CharField(blank=True, max_length=10, null=True)),
                ('calorie', models.IntegerField(blank=True, null=True)),
                ('carbohydrate', models.IntegerField(blank=True, null=True)),
                ('protein', models.IntegerField(blank=True, null=True)),
                ('fat', models.IntegerField(blank=True, null=True)),
                ('salt', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserHasMenu',
            fields=[
                ('user', models.ForeignKey(db_column='USER_id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.User')),
            ],
            options={
                'db_table': 'user_has_menu',
                'managed': False,
            },
        ),
    ]
