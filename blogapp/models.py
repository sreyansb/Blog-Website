from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.TextField()
    content=models.TextField()
    slug=models.CharField(max_length=130,default="")#url for a post
    author=models.CharField(max_length=250)
    timestamp=models.DateTimeField(blank=True)
    views=models.IntegerField(default=0)
    def __str__(self):
        return str(self.sno)+". "+self.title+" - "+self.author

class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey("blogapp.POST", on_delete=models.CASCADE)
    parent=models.ForeignKey("self", on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now )

    def __str__(self):
        return self.comment[:13]+" by "+self.user.username

