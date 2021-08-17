from django.db import models

class Session(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    next = models.DateField(blank=True, null=True, verbose_name="Next Term Begins")
    head = models.CharField(max_length=40, blank=True, null=True, verbose_name="Headmaster's Name")
    school = models.ImageField(upload_to='stamp_img/%Y/%m/%d', null=True, blank=True, verbose_name="School's Stamp with Head of Schools Signature")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.name)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
