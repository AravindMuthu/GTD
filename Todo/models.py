from django.db import models
PRIORITY_CHOICES=(
    ('H','High'),
    ('M','Medium'),
    ('L','Low'),
)

class User(models.Model):
    user_key=models.IntegerField(primary_key=True)
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.user
    class Meta:
        db_table="uservalidate"

class Todo(models.Model):
    item_id=models.IntegerField(primary_key=True)
    user_id=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    date=models.DateField()
    priority=models.CharField(max_length=1,choices=PRIORITY_CHOICES)
   
    def __unicode__(self):
        return self.user
    class Meta:
        db_table="todo"
