from django.shortcuts import render, redirect
from .models import List


# ================================  HOME ====================================


def home(request):
    return render(request, "home.html")



# ================================  LIST ====================================


def list(request):

    items = List.objects.all()

    unpurchased_items = items.filter(purchased = False)
    purchased_items = items.filter(purchased = True)

    context = {
        "items": unpurchased_items,
        "purchased_items": purchased_items
    }

    return render(request, "list.html", context)



# ================================== ADD LIST ====================================


def add_item(request):

    if request.method == "POST":

        item_name = request.POST.get("item")
        item_quantity = request.POST.get("quantity")

        new_item = List(
            item_name = item_name,
            quantity = item_quantity
        )

        new_item.save()

        return redirect("list")

    return render(request, "add_item.html")



# ================================== DELETE LIST ====================================


def delete_item(request, item_id):
    item = List.objects.get(id = item_id)

    item.delete()
    return redirect("list")




# ================================== UPDATE LIST ====================================
    


def update_item(request, item_id):

    old_item = List.objects.get(id = item_id)

    context = {
        "item": old_item
    }

    if request.method == "POST":

        new_item = request.POST.get("new_item")
        new_quantity = request.POST.get("new_quantity")

        old_item.item_name = new_item
        old_item.quantity = new_quantity

        old_item.save()

        return redirect("list")
        
    return render(request, "update_item.html", context)
    



# ================================== Purchased ====================================



def purchased(request, item_id):

    item = List.objects.get(id = item_id)

    item.purchased = True

    item.save()

    return redirect("list")





