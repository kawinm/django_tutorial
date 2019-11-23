from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Coffeehouse admin'
admin.site.site_title = 'Coffeehouse admin'
admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = 'Coffeehouse administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
