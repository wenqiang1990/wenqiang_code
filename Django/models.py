# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CsbUserInfo(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=3)
    user_name = models.CharField(max_length=20)
    user_passwd = models.CharField(max_length=20)
    user_email = models.CharField(max_length=30)
    isdelete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'csb_user_info'


class CsbWorkingHoursStat(models.Model):
    project = models.CharField(max_length=20, blank=True, null=True)
    task_name = models.CharField(max_length=6, blank=True, null=True)
    work_order = models.CharField(max_length=10, blank=True, null=True)
    user_name = models.CharField(max_length=5, blank=True, null=True)
    times = models.CharField(max_length=5, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    create_data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'csb_working_hours_stat'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RedminBugdata(models.Model):
    id = models.CharField(max_length=500, blank=True, null=True)
    project = models.CharField(max_length=500, blank=True, null=True)
    task_name = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    conner = models.CharField(max_length=500, blank=True, null=True)
    developer = models.CharField(max_length=500, blank=True, null=True)
    createdate = models.CharField(max_length=500, blank=True, null=True)
    test1 = models.CharField(max_length=500, blank=True, null=True)
    test2 = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redmin_bugdata'


class RedminStatisticaldata(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    project = models.CharField(max_length=500, blank=True, null=True)
    task_name = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    conner = models.CharField(max_length=500, blank=True, null=True)
    developer = models.CharField(max_length=500, blank=True, null=True)
    createdate = models.CharField(max_length=500, blank=True, null=True)
    writetime = models.CharField(max_length=500, blank=True, null=True)
    test = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redmin_statisticaldata'


class StatisticalData(models.Model):
    tester_name = models.CharField(max_length=10, blank=True, null=True)
    module_name = models.CharField(max_length=255, blank=True, null=True)
    version_numbers = models.CharField(max_length=30, blank=True, null=True)
    task_numbers = models.CharField(max_length=20, blank=True, null=True)
    develop_name = models.CharField(max_length=10, blank=True, null=True)
    bug_sum = models.IntegerField(blank=True, null=True)
    reopen_bug_sum = models.IntegerField(blank=True, null=True)
    close_bug_sum = models.IntegerField(blank=True, null=True)
    close_function_usm = models.IntegerField(blank=True, null=True)
    extension = models.CharField(max_length=2000, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistical_data'
    def __str__(self): # 在Python3中使用
        return self.name