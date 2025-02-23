from django.shortcuts import render, get_object_or_404
from .models import MenuItem

# Create your views here.
def menu_list(request):
    items = MenuItem.objects.all().order_by('name')
    return render(request, 'menu/menu_list.html', {'items': items})

def menu_item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'menu/menu_item_detail.html', {'item': item})
