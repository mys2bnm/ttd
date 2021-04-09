# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

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
    first_name = models.CharField(max_length=150)
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


class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    cate_name = models.TextField()
    cate_img = models.FileField(max_length=255)
    cate_detail = models.TextField()
    cate_img1 = models.FileField(max_length=255)
    cate_img2 = models.FileField(max_length=255)
    cate_img3 = models.FileField(max_length=255)
    cate_img4 = models.FileField(max_length=255)
    cate_description = models.TextField()
    cate_body = models.TextField()
    def __str__(self):
        return self.cate_name

    class Meta:
        managed = False
        db_table = 'category'


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=50)
    client_image = models.FileField(max_length=255)
    client_logo_image = models.FileField(max_length=255)
    client_detail = models.TextField()
    client_link = models.CharField(max_length=255)
    def __str__(self):
        return self.client_name

    class Meta:
        managed = False
        db_table = 'client'


class ContactContactform(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=254)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'contact_contactform'


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


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    cate_id = models.IntegerField()
    product_name = models.IntegerField()
    product_image = models.CharField(max_length=255)
    product_detail = models.TextField()
    product_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_image = models.FileField(max_length=255)
    project_image1 = models.FileField(max_length=255)
    project_image2 = models.FileField(max_length=255)
    project_image3 = models.FileField(max_length=255)
    project_date = models.CharField(max_length=50)
    project_detail = models.TextField()
    project_body = models.TextField()
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')
    project_name = models.CharField(max_length=50)
    project_address = models.CharField(max_length=50)
    project_status = models.CharField(max_length=50)
    def __str__(self):
        return '%s %s' %(self.project_name, self.project_address)

    class Meta:
        managed = False
        db_table = 'project'


class Showroom(models.Model):
    showroom_id = models.IntegerField()
    showroom_name = models.TextField()
    showroom_address = models.TextField()
    showroom_image = models.CharField(max_length=255)
    showroom_detail = models.TextField()

    class Meta:
        managed = False
        db_table = 'showroom'

#a
class Subscriber(models.Model):
    email = models.TextField()
    date_added = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'subscriber'
