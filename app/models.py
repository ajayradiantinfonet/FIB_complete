from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=300, null=True)
    name = models.CharField(max_length=20, null=True)
    Currect_ans = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.question


class all_activity(models.Model):
    question =  models.ForeignKey(Question,on_delete=models.CASCADE)
    full = models.CharField(max_length=500)

    def __str__(self):
        return self.full

class Permission(models.Model):
    visible = models.BooleanField(default=False)

    def __bool__(self):
        return self.visible