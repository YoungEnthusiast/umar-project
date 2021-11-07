from django.db import models

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

class Video(models.Model):
    title = models.CharField(max_length=200, db_index=True, unique=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='videos')
    home_page = models.BooleanField(max_length=5, default = False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return str(self.title)

    @property
    def videoURL(self):
        try:
            url = self.video.url
        except:
            url = ''
        return url
