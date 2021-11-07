from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Person(AbstractUser):
=======
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from records.models import Class

class Person(models.Model):
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
<<<<<<< HEAD
        ('Student', 'Student'),
		('Staff', 'Staff'),
        ('A---n', 'A---n'),
    ]
    phone_number = models.CharField(max_length=20, unique=False, null=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    classe = models.ForeignKey('management.Class', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Class")
    address = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student', null=True)
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Class(es) and Subject(s) I teach")
    photograph = models.ImageField(upload_to='pupil_img/%Y/%m/%d', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        try:
            return str(self.username) + " | " + str(self.first_name) + " " + str(self.last_name)
        except:
            return str(self.id)

    @property
    def photographURL(self):
        try:
            url = self.photograph.url
        except:
            url = ''
        return url

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
=======
        ('Pupil', 'Pupil'),
        ('Student', 'Student'),
		('Staff', 'Staff'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    classe = models.ForeignKey(Class, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Class")
    address = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Pupil', null=True)
    photograph = models.ImageField(upload_to='person_img/%Y/%m/%d', null=True, blank=True, verbose_name="Person's Photograph")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Person.objects.create(user=instance)
            instance.person.save()

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Person'
        verbose_name_plural = 'People'
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
