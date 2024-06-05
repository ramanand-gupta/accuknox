from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True 
        
    def update(self, details):
        for key in details:
            setattr(self, key, details[key])
        self.save()
        return self