from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other customer-related fields
    def __str__(self):
        return self.user.username
    
class SupportRep(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other support representative-related fields
    def __str__(self):
        return self.user.username
class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    support_rep = models.ForeignKey(SupportRep, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/%Y/%m/%d')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"Request by {self.customer.user.username} - {self.request_type}"
    
    class Meta:
        ordering = ['-submitted_at']  # Orders by most recent requests
        