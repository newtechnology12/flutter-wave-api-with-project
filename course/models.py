from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=10, blank=False)
    course_name = models.CharField(max_length=222,blank=False)
    credit = models.IntegerField(default=0)
    fees = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.course_name

	   
    @property	
    def get_total(self):
        total = 0
        for course in Course:
            total+= self.credit * self.fees
            return total

    def totalPayment(self):
         fees = 0
         for course in Course:
             fees = sum([course.get_total])
             return fees
        

        
    
      
       


        
    
        
		
		
