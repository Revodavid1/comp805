from django.db import models

# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=100,null=False, blank=False)
    location = models.CharField(max_length=100,null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    institution_name = models.CharField(max_length=100,null=False, blank=False)
    location = models.CharField(max_length=100,null=False, blank=False)
    degree = models.CharField(max_length=20,null=False, blank=False)
    major = models.CharField(max_length=100,null=False, blank=False)
    gpa = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.degree

class Resume(models.Model):
    First_name = models.CharField(max_length=40,null=False,blank=False)
    Last_name = models.CharField(max_length=40,null=False,blank=False)

    def __str__(self):
       return self.Last_name
    
    def get_full_name(self):
        """
        should return full name"
        """
        return"{} {}".format(self.First_name, self.Last_name)

    def get_last_name_first_name(self):
        """
        should return last name then first name
        """
        return"{} {}".format(self.Last_name, self.First_name)
    def get_experiece(self):
        """
        return all foreign key related Experience objects
        """
        pass
    def get_education(self):
        """
        return all foreign key related Education objects
        """
        pass