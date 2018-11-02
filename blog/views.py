from django.shortcuts import render
import os

# Create your views here.

def testpage(request):
    thepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('BASE_DIR is: ', thepath)
    return render(request, 'testpage.html')
