from django.db import models


"""
a Reporter can be associated wtih many article objects
but Article will have only one Reporter.
"""
class Reporter(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
class Article(models.Model):
    headline=models.CharField(max_length=100)
    pub_date=models.DateField()
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.headline}"