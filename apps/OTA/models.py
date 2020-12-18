from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=20, primary_key=True, verbose_name="你的名字")
    address = models.CharField(max_length=20, verbose_name="地址")
    email = models.EmailField(verbose_name="你的邮箱")
    message = models.TextField(verbose_name="留言")

    class Meta:
        verbose_name = "留言板"
        verbose_name_plural = verbose_name
        db_table = "message"
