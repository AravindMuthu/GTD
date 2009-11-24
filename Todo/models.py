from django.db import models

# Create your models here.
PRIORITY_CHOICES=(
    ('H','High'),
    ('M','Medium'),
    ('L','Low'),
)


class Todo(models.Model):
    subject=models.CharField(max_length=50)
    date=models.DateField()
    priority=models.CharField(max_length=1,choices=PRIORITY_CHOICES)
   
    def __unicode__(self):
        return self.subject
    class Meta:
        db_table="todo"
    
