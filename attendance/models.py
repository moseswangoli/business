from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('employee', 'date')

    def save(self, *args, **kwargs):
        if self.opening_time and self.closing_time:
            duration = (
                self.closing_time.hour + self.closing_time.minute/60
                - self.opening_time.hour - self.opening_time.minute/60
            )
            self.hours_worked = duration
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"