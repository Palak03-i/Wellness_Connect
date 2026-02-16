from django.db import models
from accounts.models import User    
# Create your models here.
class PHQ9(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    q1 = models.IntegerField()
    ...
    q9 = models.IntegerField()

    def total_score(self):
        return self.q1 + self.q2 + ... + self.q9
