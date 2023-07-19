from django.contrib import admin

# Register your models here.
from .models import Profile,Trades, Symbol,  Strategies

admin.site.register(Profile)
admin.site.register(Trades)
admin.site.register(Strategies)
admin.site.register(Symbol)

