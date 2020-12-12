
from django.contrib import admin
from django.urls import include, path

# Error Pages form game.views
handler404 = 'game.views.handler404'
handler500 = 'game.views.handler500'

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),
    # Our game
    path('', include('game.urls')),
]
