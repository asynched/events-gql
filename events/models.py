from django.db import models
from uuid import uuid4

class Stage(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Keynote(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=255)
    schedule = models.CharField(max_length=64)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Speaker(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    bio = models.TextField()
    image_url = models.URLField(max_length=512)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class KeynoteSpeaker(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)

    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    keynote = models.ForeignKey(Keynote, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.speaker} - {self.keynote}"

class SpeakerSocialMedia(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)

    twitter = models.URLField(max_length=255)
    github = models.URLField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    speaker = models.OneToOneField(Speaker, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
