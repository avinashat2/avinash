from enum import auto
from django.db import models

# Create your models here.

class ContactUsmodel(models.Model):
    name  = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    contact_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    repl=models.CharField(default=0,max_length=50,null=True,blank=True)


    def __str__(self):
        return f"{self.subject} ... by {self.name}"


class ReplyModel(models.Model):
    contactus=models.ForeignKey(ContactUsmodel,on_delete=models.CASCADE)
    email = models.CharField(max_length=50,null=True,blank=True)
    reply=models.TextField(null=True,blank=True)
    reply_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"  Subject : {self.contactus.subject}  Reply: {self.reply}"