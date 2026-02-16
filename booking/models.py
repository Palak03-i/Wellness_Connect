from django.db import models
from django.conf import settings

class Appointment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='student_appointments',
        on_delete=models.CASCADE
    )

    counsellor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='counsellor_appointments',
        on_delete=models.CASCADE
    )

    date = models.DateField()
    mode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.username} with {self.counsellor.username}"
