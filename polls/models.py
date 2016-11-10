import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def highest_value(self):
        """
        Outputs the highest number of votes
        """
        amount_of_votes = []
        for choice in self.choice_set.all():
            amount_of_votes.append(choice.votes)

        return max(amount_of_votes)

    def all_votes(self):
        """
        Outputs the total amount of votes
        """
        total_votes = 0
        for choice in self.choice_set.all():
            total_votes += choice.votes

        return total_votes

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def vote_percent(self):
        total_votes = self.question.all_votes()
        return ((self.votes * 100) / total_votes)
