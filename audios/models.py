from django.db import models
from django.conf import settings

class Category(models.Model):
<<<<<<< HEAD
    category = models.CharField(max_length=25, db_index=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category',)
=======
    type = models.CharField(max_length=25, db_index=True)

    class Meta:
        ordering = ('type',)
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
<<<<<<< HEAD
        return str(self.category)
=======
        return str(self.type)
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9

class Audio(models.Model):
    title = models.CharField(max_length=30, db_index=True, unique=True)
    audio = models.FileField(upload_to='audios/%Y/%m/%d', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='audios')
    home_page = models.BooleanField(max_length=5, default = False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        # verbose_name = 'Background Nasheed'
        # verbose_name_plural = 'Background Nasheeds'
    def __str__(self):
        return str(self.title)

    @property
    def audioURL(self):
        try:
            url = self.audio.url
        except:
            url = ''
        return url
