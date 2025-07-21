from django.contrib import admin
from .models import CustomUser,Category,Advert,ExchangeProposal
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'slug', 'parent') # Fields to display in the list view
    list_display = ('name', 'parent') # Fields to display in the list view
    # prepopulated_fields = {'slug': ('name',)} # Automatically populate slug from name
    # prepopulated_fields = {'slug': ('name',)} # Automatically populate slug from name
    # search_fields = 'name'  # Enable searching by these fields
    list_filter = ('parent',) # Enable filtering by parent category

# admin.site.register(Ad)
# @admin.register(Advert)
# class AdAdmin(admin.ModelAdmin):
#     list_display = ('user_id','category_id','title')

@admin.register(ExchangeProposal)
class ExchangeProposalAdmin(admin.ModelAdmin):
    list_display = ('sender_id','status','comment')

