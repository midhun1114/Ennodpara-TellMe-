from django.shortcuts import render
from .models import cart
from .forms import RawCartForm
from django.contrib import messages
#
def cart_create_view(request):
    message = 'NONE'
    form = RawCartForm()
    if request.method == 'POST':
        form = RawCartForm(request.POST)
        if form.is_valid():

            cart.objects.create(**form.cleaned_data)
            form = RawCartForm()
            message='Kitty Bodichu!!'


        else:
            print(form.errors)



    return render(request, 'contacts/contact.html', {'form': form, 'message':message})



def cart_detail_view(request):
    obj=cart.objects.all()

    dic={
        'obj':obj
    }
    return render(request,"contacts/forms.html", dic)

def search(request):
    searchq = request.POST.get('search', False)
    dic={}
    if searchq != '' and searchq != False:
        searched=searchq.split()[0]
        print(searched)
        # searched1 = searched[0].upper() + searched[1:].lower()

        obj2 = cart.objects.filter(title__icontains=searched)
        dic = {
            'obj': obj2
        }
        print(obj2)







    return render(request,"contacts/searched.html", dic)
