from django.contrib import admin

# Register your models here.
from .models import * 

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(CarImage)
admin.site.register(Review)
admin.site.register(Enquiry)