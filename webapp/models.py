from django.contrib.auth.models import User
from django.db import models

ACCESS_CHOICES = (
    ('0', 'Public'),
    ('1', 'Hidden'),
    ('2', 'Private'),
)


class File(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name="files",
                               verbose_name="Автор")
    file = models.FileField(upload_to='images', verbose_name="File")
    caption = models.CharField(max_length=50, verbose_name="Caption")
    access = models.CharField(max_length=20, choices=ACCESS_CHOICES, default=ACCESS_CHOICES[0][0],
                              verbose_name='Access')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    def __str__(self):
        return f'{self.caption[:10]}'
