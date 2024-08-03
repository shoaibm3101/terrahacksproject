from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=500)
    score_worth = models.IntegerField(default=0)

    def __str__(self):
        return self.question

class Company(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.score}"