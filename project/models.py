from django.db import models

# Create your models here.
class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    cate_name = models.TextField()
    cate_img = models.CharField(max_length=255)
    cate_status = models.IntegerField()
    cate_detail = models.TextField()
    cate_img1 = models.CharField(max_length=255)
    cate_img2 = models.CharField(max_length=255)
    cate_img3 = models.CharField(max_length=255)
    cate_img4 = models.CharField(max_length=255)
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
