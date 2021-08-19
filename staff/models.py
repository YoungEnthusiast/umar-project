from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Teacher(models.Model):
    GENDER_CHOICES = [
		('Male','Male'),
		('Female', 'Female')
	]
    ROLE_CHOICES = [
        ('Pupil', 'Pupil'),
		('Staff', 'Staff'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Pupil', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            if self.gender == "Male":
                return "Mr " + str(self.user.first_name) + " " + str(self.user.last_name)
            else:
                return "Mrs " + str(self.user.last_name)
        except:
            return str(self.id)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
