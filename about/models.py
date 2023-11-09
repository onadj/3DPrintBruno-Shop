from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/images/', blank=True, null=True)
    content = models.TextField()
    video_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='about/images/')

    def __str__(self):
        return self.about.title
