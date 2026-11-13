from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=1000)
    about_text = models.TextField()
    link_text = models.TextField(blank=True)
    notes = models.TextField(
        blank=True,
        help_text="The text in this field will not be displayed. Use for notes."
    )
    resume = models.FileField(upload_to='resume', blank=True)
    resume_update = models.DateField(null=True)
    contact = models.CharField(max_length=1000, null=True)
    last_modified = models.DateTimeField(auto_now=True)

class Writing(models.Model):
    class Category(models.TextChoices):
        PUB = "Publications"
        MAN = "Manuscripts"
        OTH = "Other"
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(choices=Category, max_length=1000)
    link = models.URLField(max_length=1000, blank=True)
    file = models.FileField(upload_to='writing', blank=True)
    date_published = models.DateField(null=True)

    @property
    def url(self):
        return self.link or self.file.url

    def __str__(self):
        return self.title
