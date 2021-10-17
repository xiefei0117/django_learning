from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class NewShoppingListForm(forms.Form):
    item = forms.CharField(label = "Shopping Item")
    count = forms.IntegerField(label = "Counts")

def index(request):
    print(request.session)
    if "dict" not in request.session:
        request.session["dict"] = {}
    
    #request.session["dict"] = {"apple" : 1,}
    #print(request.session["dict"])
    return render(request, "shoppinglist/index.html", {
        "dict" : request.session["dict"],
    })

def add(request):
    if request.method == "POST":
        form = NewShoppingListForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            count = form.cleaned_data["count"]
            #print(item + " " + str(count))

            if item in request.session["dict"].keys():
                request.session["dict"][item] += count
            else:
                request.session["dict"][item] = count

            #print(request.session["dict"])
            request.session.modified = True
            return HttpResponseRedirect(reverse("shoppinglist:index"))
        
        else:
            return render(request, "shoppinglist/add.html", {
                "form" : form,
            })
    else:
        return render(request, "shoppinglist/add.html", {
            "form" : NewShoppingListForm(),
        })

