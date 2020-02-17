from django.db import models
from django.urls import reverse
# Create your models here.

class Problems(models.Model):
	problemID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	problemInfo = models.TextField() # max_length=4000
	evaluationCode = models.TextField()
	isValid = models.BooleanField(default=False)
	isReleased = models.BooleanField(default=False)

	def __str__(self):
		return f"Problems('{self.title}', '{self.problemInfo}', '{self.evaluationCode}', '{self.isValid}', '{self.isReleased}')"

	def get_absolute_url(self):
		return reverse('problem_detail', kwargs={'pk': self.pk})
		# return reverse('problem_detail', args=[str(self.id)])