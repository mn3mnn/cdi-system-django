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
    MANUAL_CHOICES = [
        ('', 'Choose Priority'),
        ('high', 'High'),
        ('med', 'Medium'),
        ('low', 'Low')
    ]

    AUTO_CHOICES = [
        ('0', 'Ok'),
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'),
        ('4', 'Very High')
    ]

    REV_CHOICES = [
        ('ok', 'Ok'),
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('re-reviewed', 'Re-Review'),
        ('closed', 'Closed')
    ]

    work_list_id = models.AutoField(primary_key=True)
    patient_id = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=100)
    assigned_specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, null=True, blank=True)
    encounter_date = models.DateField()
    assignment_date = models.DateField(null=True, blank=True)
    open_queries = models.IntegerField()
    status = models.CharField(max_length=20, null=True, blank=True, choices=REV_CHOICES, default='P')
    physician = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    facility = models.CharField(max_length=100)
    sys_priority = models.CharField(
        blank=True, max_length=1000, choices=AUTO_CHOICES)
    manual_priority = models.CharField(
        blank=True, max_length=1000, choices=MANUAL_CHOICES)

    # notes = models.TextField(blank=True, null=True)
    # medications = ArrayField(models.JSONField(default=dict, null=True), null=True)
    # diagnosis = ArrayField(models.JSONField(default=dict, null=True), null=True)
    # services = ArrayField(models.JSONField(default=dict, null=True), null=True)






