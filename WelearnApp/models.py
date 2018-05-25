from django.db import models

# Create your models here.
#----------------------models for tutor page------------------------------------------------
class Topic(models.Model):
    post_text = models.TextField(default='')
    detail = models.TextField(default='')    
    '''def __str__(self):
        return self.comment'''
class Comment(models.Model):
    cm = models.TextField(default='')
    comment = models.ForeignKey(Topic,default=None, on_delete=models.CASCADE)


#----------------------model for examination page-----------------------------------------
class TopicExam(models.Model):
	topic_exam = models.TextField(default='')
	detail_exam = models.TextField(default='')
class Comment_Exam(models.Model):
	cm_exam = models.TextField(default='')
	comment_exam = models.ForeignKey(TopicExam,default=None, on_delete=models.CASCADE)




#----------------------------------test uplode picture---------------------------------------
class Profile(models.Model):
    #title = models.CharField(max_length=50)
    filePic = models.ImageField(upload_to = 'uplode')

    class Meta:
        db_table = "profile"