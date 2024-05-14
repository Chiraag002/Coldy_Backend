from django.db import models


class CommonFields(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    deletion_date = models.DateTimeField(null=True)
    create_by = models.IntegerField(null=True)
    update_by = models.IntegerField(null=True)
    delete_by = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
