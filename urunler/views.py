from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    markalar=Marka.objects.all()
    context={
        'markalar':markalar,
    }
    return render(request,'index.html',context)
def urunler(request):
    kategoriler=Kategori.objects.all()
    altkategori=AltKategori.objects.all()
    urunler=Urun.objects.all()
    
    
    search=''
    if request.GET.get('search'): 
        search=request.GET.get('search')
        urunler=Urun.objects.filter(
            Q (isim__icontains=search) |
            Q(kategori__isim__icontains=search) |
            Q(sub_category__isim__icontains=search) |
            Q(marka__isim__icontains=search)
            
        )
    context={
        
        'urunler':urunler,
        'search':search,
        'kategoriler':kategoriler,
        'altkategori':altkategori
    }
    return render(request,'urunler.html',context)

def iletisim(request):
    return render(request,'iletisim.html')
def sepet(request):
    return render(request,'sepet.html')
def uyegiris(request):
    return render(request,'uyegiris.html')

def view_404(request,exception):
    return redirect('/')