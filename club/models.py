from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    """
    Create entity for categories like static, dyanmic, software etc.
    One to One model for Idea Submission

    """

    name = models.CharField(max_length=25, default="static", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Project(models.Model):
    """
    Entity for Idea Submission
    """

    DEPARTMENT_OPTIONS = (
        ('IT', 'IT'),
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('ME', 'ME'),
        ('EE', 'EE'),
        ('CE', 'CE')
    )

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    department = models.CharField(default='IT', choices=DEPARTMENT_OPTIONS, max_length=25)
    pass_year = models.IntegerField(default=2020)
    content = models.TextField(max_length=10000)
    picture = models.ImageField(upload_to='project_images', blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    slug = models.SlugField(default='', unique=True)  # add unique after migrations to avoid spcace

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def yearpublished(self):
        return self.created.strftime('%Y')

    def monthpublished(self):
        return self.created.strftime('%b')

    def daypublished(self):
        return self.created.strftime('%d')



class CFIProject(models.Model):
    """
    Entity for CFI Project
    """
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='CFIProject_images')
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'CFI Projects'



class Contactus(models.Model):
    """
    Entity for Contact us
    """
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " ---- " + self.email

    class Meta:
        verbose_name_plural = 'Contact us Records'








