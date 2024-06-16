from django.contrib import admin
from .models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("email", "ratings", "verify", "date")
    list_filter = ("date",)
