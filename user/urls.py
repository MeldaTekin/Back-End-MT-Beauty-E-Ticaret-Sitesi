from django.urls import path
from .views import*

urlpatterns = [
   path('uyegiris/',userUyegiris,name='uyegiris'),
   path('cikis/',userCikis,name='cikis'),
   path('iletisim/',iletisim,name='iletisim'),
  
]
