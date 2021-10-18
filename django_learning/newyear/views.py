from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    newyear = datetime.datetime(now.year + 1, 1, 1)
    diff = newyear - now
    return render(request, "newyear/index1.html", {
        "newyear" : now.month == 1 and now.day == 1,
        "days_left" : diff.days})

