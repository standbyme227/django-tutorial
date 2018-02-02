import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        '''
        이 Question의 게시일자가 현재시각에서 1일 전보다 이후인지를 리턴
            (Question을 게시한지 1일이 지나지 않았는지)
        :return:
        '''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #하루가 지나면 False가 되는 로직이란다...

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return '{} | {}'.format(
            self.question.question_text,
            self.choice_text,
        )