from django.db import models
from django.urls import reverse

# Create your models here.

class Add_quests(models.Model):
    correct_answer = models.CharField(max_length=255)
    quest = models.TextField(blank=True)
    answers = models.CharField(max_length=255)

    def __repr__(self):
        return self.quest

    class Meta:
        verbose_name = 'Quest'
        verbose_name_plural = 'Quests'
