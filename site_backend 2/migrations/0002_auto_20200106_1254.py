# Generated by Django 2.2.2 on 2020-01-06 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_backend', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AllTransfer',
        ),
        migrations.DeleteModel(
            name='AnswerMessage',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='CommisionTimer',
        ),
        migrations.DeleteModel(
            name='Config',
        ),
        migrations.DeleteModel(
            name='DealQuestions',
        ),
        migrations.DeleteModel(
            name='Deals',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='EmployeesWorkType',
        ),
        migrations.DeleteModel(
            name='Executor',
        ),
        migrations.DeleteModel(
            name='FieldOfActivity',
        ),
        migrations.DeleteModel(
            name='IdDealsMessage',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='NewUsersWithSales',
        ),
        migrations.DeleteModel(
            name='Operators',
        ),
        migrations.DeleteModel(
            name='PropedDeals',
        ),
        migrations.DeleteModel(
            name='StatusDeal',
        ),
        migrations.DeleteModel(
            name='StatusUser',
        ),
        migrations.DeleteModel(
            name='TopTimetable',
        ),
        migrations.RemoveField(
            model_name='usersessionhistory',
            name='id',
        ),
        migrations.DeleteModel(
            name='UsersHistory',
        ),
        migrations.DeleteModel(
            name='UsersTransfers',
        ),
        migrations.DeleteModel(
            name='VeryFirst',
        ),
        migrations.DeleteModel(
            name='WorkType',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.DeleteModel(
            name='UserSessionHistory',
        ),
    ]