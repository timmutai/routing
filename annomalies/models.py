from django.db import models

# Create your models here.

class parcel(models.Model):
    plot_number=                models.CharField(max_length=15)
    lr_number=                  models.CharField(max_length=15)
    parcel_active_status=       models.CharField(max_length=15)
    survey_parcel_no=           models.CharField(max_length=30)
    survey_status=              models.BooleanField(default=False)
    survey_comment=             models.TextField()
    land_admin_parcel_no=       models.CharField(max_length=15)
    land_admin_parcel_status=   models.BooleanField(default=False)
    land_admin_comment=         models.TextField()
    land_reg_parcel_no=         models.CharField(max_length=15)
    land_reg_status=            models.BooleanField(default=False)
    land_reg_comment=           models.TextField()
    registered=                 models.BooleanField(default=False)
    tenure=                     models.BooleanField(default=False)
    ownership=                  models.BooleanField(default=False)
    waterfall=                  models.BooleanField(default=False)
    post_2015_comment=          models.TextField(null=True)
    date_created=               models.DateField()
    created_by=                 models.CharField(max_length=100)


class issues(models.Model):
    issue=          models.CharField(max_length=100)
    department=     models.CharField(max_length=20)
    created_by=     models.CharField(max_length=100)
    date_created=   models.DateField()

class issue_details(models.Model):
    parcel_id=          models.ForeignKey(to=parcel, on_delete=models.CASCADE)
    issue_id=           models.ForeignKey(to=issues, on_delete=models.CASCADE)
    issue_description=  models.TextField()
    date_created=       models.DateField()
    created_by=         models.CharField(max_length=15)
    status=             models.BooleanField(default=False)      

class issue_remarks(models.Model):    
    issue_details_id=   models.ForeignKey(to=issue_details, on_delete=models.CASCADE)
    remarks=            models.TextField()
    created_by=         models.CharField(max_length=100)
    date_created=       models.DateField()











