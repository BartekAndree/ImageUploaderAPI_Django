from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import FileUpload, ArbitaryTier, GenerateLink


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('Tier info',
            {'fields': 
                ('build_in_tier', 'arbitary_tier')
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,
            {'fields': 
                ('build_in_tier', 'arbitary_tier')
            }
        ),
    )

    list_display = ('username', 'email', 'is_active', 'build_in_tier', 'arbitary_tier')
    list_filter = ('build_in_tier', 'arbitary_tier')
    search_fields = ('username', 'email')





@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('creator', 'title', 'image_url')

@admin.register(ArbitaryTier)
class ArbitaryTierAdmin(admin.ModelAdmin):
    list_display = ('tier_name', 'thumbnail_size', 'is_original_link', 'is_generate_link')

@admin.register(GenerateLink)
class GenerateLinkAdmin(admin.ModelAdmin):
    list_display = ('creator', 'create_at', 'link_duration')
    list_filter = ('create_at',)