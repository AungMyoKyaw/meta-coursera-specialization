from restaurant.models import Menu


Menu.objects.create(name="Pizza", price=12.99, menu_item_description="A delicious pizza")
Menu.objects.create(name="Burger", price=8.99, menu_item_description="A juicy burger")
Menu.objects.create(name="Salad", price=6.99, menu_item_description="A healthy salad")