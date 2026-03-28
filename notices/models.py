from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Notice(models.Model):
    NOTICE_TYPE = (
        ('general', 'General'),
        ('important', 'Important'),
    )

    title = models.CharField(max_length=255)
    message = models.TextField()

    notice_type = models.CharField(max_length=20, choices=NOTICE_TYPE, default='general')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    expiry_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title