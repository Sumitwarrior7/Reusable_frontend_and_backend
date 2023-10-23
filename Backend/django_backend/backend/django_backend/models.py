from django.db import models

# using get_user_model(), you ensure that the relation points to the currently specified custom user model in your
# project's settings, regardless of whether it's the default User model or a custom model you have defined.
from django.contrib.auth import get_user_model



class Note(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  #auto_now means to take the current time
    created = models.DateTimeField(auto_now_add=True) #auto_now_add means to take that time when actuallt the model instance was created

    def _str_(self):
        return self.body[0:50]


