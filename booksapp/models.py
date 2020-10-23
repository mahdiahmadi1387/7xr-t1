
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=400)
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Ages(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Book(models.Model):
    # شماره کتاب
    number = models.IntegerField()
    # نام کتاب
    name = models.CharField(max_length=400)
    # نویسنده
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name="books",default=None)
    # موضوع
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name="books",default=None)
    # تعداد صفحات
    page_count = models.IntegerField()
    # رده سنی
    ages = models.ForeignKey(Ages,on_delete=models.CASCADE, related_name="books",default=None)
    # عکس
    image = models.ImageField(upload_to = 'pic_folder/booksapp/', default = 'pic_folder/booksapp/no-img.jpg')
    # کاربر
    # user = models.AutoField()
    def __str__(self):
        return f"{self.name} {self.author.name} ({self.topic.name})"

class Comment(models.Model): 
    post = models.ForeignKey(Book,on_delete=models.CASCADE, related_name ="comments")
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 