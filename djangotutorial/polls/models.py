from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model): 
    
    # let me guess: models is the file while Model is the class itself
    question_text = models.CharField(max_length=100, null=False, blank=False)

    pub_date = models.DateTimeField(auto_now=True) # the DateTimeField() this is a field that is used to manage date and time values. 
    # some of the arguments it can take are:

    def __str__(self):
        return self.question_text
    
    # function to return Questions(question_text)
    def display_questions(self):
        print(self.question_text)
    

    # function to display recent question
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # does comparisons
    """
    In django, we do not declare the constructor method as this is handled by django itself: 
        ``def __init__(self):``

    Note:
    ```py
    from django.utiles import timezone
    # the timezone is 
    ``timezone.now()`` #returns the current date time in UTC(Universal Coordinate Time) if UTC=true, USE_TZ = True
    This is a function from the datetime module that represents a duration, in this case, 1 day.
    The expression ``timezone.now() - timedelta(days=1)`` gives the datetime exactly 24 hours ago.


    CharField()
        max_length property is used to set the length of the field(remember it is by default always required)
    DateTimeField()
        auto_now=True (every time the object is saved or changed(updated) the time is saved )
        auto_now_add=True(This only saves the time when the object is created)
        The text passed is a verbose string/name, think of it as column header
        The verbose_name is a human-readable, descriptive name for the field. It is used in Django's admin interface, forms, and other places in the Django framework where the field needs to be displayed to users
    IntegerField() 
        does not have any required arguments
        It is used for setting the integer values
    """


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100, null=False, blank=False)
    votes = models.IntegerField(default=0)




question_instance = Question()
question_instance.display_questions()
