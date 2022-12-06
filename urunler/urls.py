from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='anasayfa'),
    path('urunler/',urunler,name='urunler'),
    path('iletisim/',iletisim,name='iletisim'),
    path('sepet/',sepet,name='sepet'),
    path('uyegiris/',uyegiris,name='uyegiris')
]
