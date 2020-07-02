from django.shortcuts import render
from .models import destination
# Create your views here.
def index(request):
    dest=destination()
    dest.name='kollegala'
    dest.price=560



    '''dest2 = destination()
    dest2.name = 'mysore'
    dest2.price = 560

    dest3=destination()
    dest3.name='bnglore'
    dest3.price=730

    dest4 = destination()
    dest4.name = 'ramapura'
    dest4.price = 700

    dests=[dest1,dest2,dest3,dest4]'''

    return render(request,'index.html',{'dest':dest});