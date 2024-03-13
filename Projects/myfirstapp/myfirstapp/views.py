from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import PrimeForm
from .primeTest import isPrime

def hello_world(request):
    return HttpResponse('''
                        
                        <h1 style="background-color:aqua;color:blue;border: 1px solid black;text-align:center;width: 300px;">Hello from Django</h1>
                        
                        ''')
@csrf_exempt    
def addxy(request):
    if (request.method=='POST'):
        x=int(request.POST.get('first'))
        y=int(request.POST.get('second'))
        z=x+y
        return HttpResponse('Result=' +str(z))
    else:
        return HttpResponse('''
                            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="add" method="post">
        <p>
            <label for="first">Enter First Number</label>
            <input type="text" name="first" id="first">
        </p>
        <p>
            <label for="second">Enter Second Number</label>
            <input type="text" name="second" id="second">
        </p>
        <button type="submit">ADD</button>
    </form>
</body>
</html>
                            
                            ''')

        
from .forms import  InputForm    
@csrf_exempt     
def ad2(request):
    z=0
    form=InputForm()
    if request.method=='POST':
        form=InputForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            x=cd['x']
            y=cd['y']
            z=x+y
            
    return render(request,'pages/addition.html',{'form':form,'output':z})

def performarithmetic(request):
    x=1
    y=1
    form=InputForm()
    if request.method=='POST':
        form=InputForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            x=cd['x']
            y=cd['y']
           
            
    return render(request,'pages/arithmetic.html',{'form':form,
    'x':x,
    'y':y,
    'r1':x+y,
    'r2':x-y,
    'r3':x*y,
    'r4':x/y,
    'r5':x%y,
    })
    
    
def prime(request):
    b=False
    form=PrimeForm()
    if request.method=='POST':
        form=PrimeForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            x=cd['x']
            b=isPrime(x)
           
    if b==False:
        m="This Number is not Prime"    
    else:
         m="This Number is  Prime"         
    return render(request,'page2/prime.html',{'form':form,'output':m})