from account.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Topic(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, default='userNotFound', on_delete=models.SET_DEFAULT)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=155)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('-updated', '-created')

    def __str__(self):
        return f'{self.name} - {self.host}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Room, self).save()

    def get_absolute_url(self):
        return reverse('core:room-detail', kwargs={'pk': self.pk, 'slug': self.slug})


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='message')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('-updated', '-created')

    def __str__(self):
        return f'{self.user}|{self.room}--{self.text[:25]}'
