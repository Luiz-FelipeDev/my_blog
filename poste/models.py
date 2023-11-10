from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        '''Esse método vai de encontro com o DRY, ou seja,
         não irei duplicar código qaundo precisar chamar uma url especifica para um objeto'''

        return reverse('detail-poste',  kwargs={'pk': self.pk})







