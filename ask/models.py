from django.db import models


class QuestionManager(models.Manager):

    def best(self):
        return self.filter(rating__gt=10).order_by('-rating')

    def fresh(self):
        return self.order_by('-pk')

    def own_with_answers(self, for_user):
        return self.filter(author=for_user, answer_count__gt=0)


class Question(models.Model):
    objects = QuestionManager()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return '#{pk}: {title}'.format(pk=self.pk, title=self.title[:20])


class Tag(models.Model):
    name = models.CharField(max_length=64)
