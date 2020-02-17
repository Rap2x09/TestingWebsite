from django.db import models
from django.urls import reverse
from .validators import validate_file
# Create your models here.

from django.db.models.signals import pre_delete, post_delete
from django.dispatch.dispatcher import receiver

class Problem(models.Model):
	problemID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100, verbose_name= 'Title')
	problemInfo = models.TextField(verbose_name= 'Problem Details') # max_length=4000
	evaluationCode = models.TextField(verbose_name='Evaluation Code')
	isValid = models.BooleanField(default=False, verbose_name= 'Valid?')
	isReleased = models.BooleanField(default=False, verbose_name= 'Released?')

	# class Meta:
	# 	verbose_name = "Problem"
	# 	verbose_name = "Problems"

	def __str__(self):
		return f"'{self.title}', '{self.problemInfo}', '{self.evaluationCode}', '{self.isValid}', '{self.isReleased}')"

	def get_absolute_url(self):
		return reverse('problem_detail', kwargs={'pk': self.pk})
		# return reverse('problem_detail', args=[str(self.id)])

class Dataset(models.Model):
	dataID = models.AutoField(primary_key=True)
	dataset = models.FileField(upload_to='datasets/', validators=[validate_file])
	datasetDesc = models.CharField(max_length=100, verbose_name= 'Dataset Short Description')
	problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

	# class Meta:
	# 	verbose_name = 'Dataset'
	# 	verbose_name_plural = 'Datasets'

	def __str__(self):
		return f"'{self.dataset}', '{self.datasetDesc}'"

	def filename(self):
		return os.path.basename(self.dataset.name)

# @receiver(pre_delete, sender=Dataset)
# def mymodel_delete(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     instance.file.delete(False)

# Deletes dataset file in the path folder
@receiver(post_delete, sender=Dataset)
def photo_post_delete_handler(sender, **kwargs):
    file = kwargs['instance']
    storage, path = file.dataset.storage, file.dataset.path
    storage.delete(path)