from django.db import models
import json

class Question(models.Model):
    question_text           = models.CharField(max_length=200)
    pub_date                = models.DateTimeField()

    def __str__(self):
        return self.question_text

    def info(self):
        info = {
            'ID': self.id,
            'Question': self.question_text,
            'Publication Date': self.pub_date.strftime("%m/%d/%Y, %H:%M:%S")
        }
        return json.dumps(info)




class Choice(models.Model):
    question                = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text             = models.CharField(max_length=200)
    votes                   = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

