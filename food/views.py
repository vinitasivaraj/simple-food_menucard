from django.shortcuts import render,redirect
from django.http import HttpResponse
from food.models import items
from .forms import ItemForm
from django.views.generic import CreateView
# Create your views here.


def index(request):
    item_list=items.objects.all()

    return render(request,"food/index.html", {'item_list':item_list})

def item(request):
    return HttpResponse("THIS IS ITEM")

def detail(request,pk):
        item_id=items.objects.get(pk=pk)
        return render(request,"food/detail.html",{'item_id':item_id})

def create_item(request):

    # if request.method == 'POST':
        form=ItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('food:index')
        return render(request,'food/item-form.html',{'form':form})


class CreateItem(CreateView):
    model =items
    fields=['item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)




def update_item(request,pk):
    item=items.objects.get(pk=pk)
    form=ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')


    return render(request,'food/item-form.html',{'form':form,'item':item})


def delete_item(request,pk):

    item=items.objects.get(pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/delete.html', {'item': item})

