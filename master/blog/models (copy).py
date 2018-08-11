from django.db import models

class Post(models.Model):

#blog_ad
    blog_h1 = models.CharField(max_length = 140)
    blog_h2 = models.CharField(max_length = 140)
    blog_snipp = models.CharField(max_length = 140)

#main
    main_title = models.CharField(max_length = 140) 
     #blog_h1 and bog_h2 can be used also
    main_body = models.TextField()
    date = models.DateTimeField()

def __str__(self):
    template = '{0.blog_h1} {0.self.blog_h2} {0.self.blog_snipp} {0.self.main_title} {0.self.main_body}{0.self.date}'
    return template.format(self)

class Slider1(models.Model):
#first slide_content
    slide_headline1 = models.CharField(max_length = 140)
    slide_content1 = models.TextField()
    
    def __str__(self):
        return self.name

class Slider2(models.Model):
#first slide_content
    slide_headline2 = models.CharField(max_length = 140)
    slide_content2 = models.TextField()
    
    def __str__(self):
        return self.name

class Slider3(models.Model):
#first slide_content
    slide_headline3 = models.CharField(max_length = 140)
    slide_content3 = models.TextField()
    
    def __str__(self):
        return self.name

class Comment(models.Model):
#first slide_content
    comment_text = models.TextField()
    
    def __str__(self):
        return self.name


class Moto(models.Model):
#first slide_content
    moto_text = models.CharField(max_length = 140)
    
    def __str__(self):
        return self.name
