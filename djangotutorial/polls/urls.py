from django.urls import path
from .views import detail, results, vote, index
urlpatterns = [
    path("", index, name="polls"), # polls show all questions: /polls
    path("<int:question_id>/",  detail, name="detail"), # polls/5 
    path("<int:question_id>/results/", results, name="result"), # polls/5/results/
    path('<int:question_id>/vote/', vote, name="vote") # polls/5/vote
]

"""
the path() is a django urls configuration method that is used to match the url to the given view. 

# <'int:question_id'>/
The brackets indicate a captured variable. 
The int(datatypeKeyworld) specifies the datatype of the captured value: e.g string
The next statement: question_id is the variable that will be passed to the view
this is the captured variable. 

name="string"
the string passed in the name property is used for navlinks

**Note**
Instead of using ``path("url", view)`` we should use the include method
The include method is acquired from  django.urls
```
from django.urls import path, include
# syntax:path("polls/", include('appName/urls'));
path("polls/", include('polls.urls))

also after defining polls in main_project/urls.py file e.g
```py
path("polls/", view_name, name="polls")
```
never declare the again in polls/urls.py the ``path("polls/")``
just pass: ``path("", view_name)``


When passing viariables to a path it depends:
example: 

for the urlpatthern
path(<int:question_id>/) # polls/1
path(<int:question_id>/results/) # polls/question_id/results/
# we integer
"""