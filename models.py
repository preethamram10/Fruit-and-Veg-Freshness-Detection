from django.db import models

class FreshnessPrediction(models.Model):
    image = models.ImageField(upload_to='uploads/')
    predicted_class = models.CharField(max_length=100)
    confidence_score = models.FloatField()
    time_taken = models.FloatField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
