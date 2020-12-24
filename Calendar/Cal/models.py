from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    event_text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Cal:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('Cal:event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)