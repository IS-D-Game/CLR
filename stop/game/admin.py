from django.contrib import admin

# Register your models here.
from .models import Answer
from .models import Player
from .models import Settings
# Register your models here.
admin.site.register(Answer)
admin.site.register(Player)
admin.site.register(Settings)