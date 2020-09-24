from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import razorpay
client = razorpay.Client(auth = ("rzp_test_FiqCIVEIZriREW","zm5Q6yKVvM19FbG0egxN5RJm"))
        

# Create your views here.
def signin(request):

    if request.user.is_authenticated:
        return render(request, "dashboard.html", {"name" : request.user})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "dashboard.html", {"name" : request.user})
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')

def index(request):
    if request.method == 'POST':

        if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"name" : request.user})
        else:
            obj = User.objects.create_user(username = request.POST['username'], email = request.POST['email'], password = request.POST['password'])
            obj.save()
            login(request, obj)
            return render(request, "index.html", {"name" : request.user})
    return render(request, "index.html")
def payment(request):
    context = {}
    if request.method == 'POST':
        order_amount = 100
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {
        'Shipping address':'Noida' 
        }
        response = client.order.create(dict(
                                            amount = order_amount,
                                            currency = order_currency,
                                            receipt = order_receipt,
                                            notes = notes,
                                            payment_capture = '0'))
        order_id = response['id']
        order_status = response['status']

        if order_status=='created':

            # Server data for user convinience
            # data that'll be send to the razorpay for
            context['order_id'] = order_id


            return render(request, 'index.html', context)
    return render(request, "course-single.html")
    
    #if request.user.is_authenticated:
     #   return render(request, "dashboard.html", {"name" : request.user})
    #else:
     #   return render(request, "index.html")
