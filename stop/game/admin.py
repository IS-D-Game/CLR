from django.contrib import admin

# Register your models here.
from .models import Answer
from .models import Player
from .models import Settings
from .models import Evaluation
# Register your models here.
admin.site.register(Answer)
admin.site.register(Player)
admin.site.register(Settings)
admin.site.register(Evaluation)