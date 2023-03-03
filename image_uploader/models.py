from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, User, UserManager
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
import uuid



BUILT_IN_TIERS = (
    ('basic', 'Basic'),
    ('premium', 'Premium'),
    ('enterprise', 'Enterprise')
)

class ArbitaryTier(models.Model):

    tier_name = models.CharField(max_length=255)
    thumbnail_size = models.IntegerField()
    is_original_link = models.BooleanField(default=False)
    is_generate_link = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tier_name}-{self.thumbnail_size}"


class User(AbstractUser, PermissionsMixin):

    build_in_tier = models.CharField(max_length=10, choices=BUILT_IN_TIERS, default='basic', null=True, blank=True)
    arbitary_tier = models.OneToOneField(ArbitaryTier, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.username



def upload_to(instance, filename):
    extencion = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extencion}'
    return f'images/{filename}'

class FileUpload(models.Model):

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.ImageField(upload_to=upload_to, validators=[FileExtensionValidator(['jpg', 'png'])])

    def __str__(self):
        return f'{self.title} - {self.id}' 


class GenerateLink(models.Model):

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(FileUpload, on_delete=models.CASCADE)
    create_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    link_duration = models.IntegerField(default=300, validators=[MaxValueValidator(30000), MinValueValidator(300)])

    def __str__(self):
        return f'{self.image.image_url} - {self.create_at}'