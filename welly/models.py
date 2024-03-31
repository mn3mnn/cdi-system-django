from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.

class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Call the original save() method
        super().save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='specialist')
        group.user_set.add(self.user)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Call the original save() method
        super().save(*args, **kwargs)
        group, created = Group.objects.get_or_create(name='manager')
        group.user_set.add(self.user)

class WorkList(models.Model):
    work_list_id = models.AutoField(primary_key=True)
    patient_id = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=100)
    assigned_specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, null=True, blank=True)
    encounter_date = models.DateField()
    assignment_date = models.DateField(null=True, blank=True)
    open_queries = models.IntegerField()
    sys_priority = models.IntegerField()
    manual_priority = models.IntegerField()
    status = models.CharField(max_length=20, null=True)
    physician = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    facility = models.CharField(max_length=100)




