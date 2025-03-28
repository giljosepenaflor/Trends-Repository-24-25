from django.shortcuts import render
from .models import Member  # ✅ Import your model

def members(request):
    mymembers = Member.objects.all()  # ✅ Fetch all members
    return render(request, 'index.html', {'mymembers': mymembers})  # ✅ Use render()
