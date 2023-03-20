from django.contrib import admin

from profil.models import Profile, SocialLink,Contact

# Register your models here.


# admin.site.register(Profile)
# admin.site.register(SocialLink)
# admin.site.register(Contact)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email','profile_name', 'location', 'num_of_social_links')
    list_filter = ('profile_name', 'location', 'career')
    # prepopulated_fields ={'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = ('release')
    # ordering = ('status', 'release')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('for_profile','link', 'link_name')
    # list_filter = ('profile_name', 'location', 'career')
    # prepopulated_fields ={'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = ('release')
    # ordering = ('status', 'release')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_from','user_to', 'created')
    # list_filter = ('profile_name', 'location', 'career')
    # prepopulated_fields ={'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = ('release')
    # ordering = ('status', 'release')