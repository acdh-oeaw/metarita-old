from apis.urls import *

urlpatterns.insert(0, url(r'images/', include('images.urls', namespace='images')))
