from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import PaymentDetails, AssignmentDetails, RequestedAssignment
import razorpay

client = razorpay.Client(auth = ("rzp_test_FiqCIVEIZriREW","zm5Q6yKVvM19FbG0egxN5RJm"))
        

# Create your views here.

def assignment_sol(request, sub_code):
    try:
        assignment = AssignmentDetails.objects.get(subject_code = sub_code)
        context = {}
        context['assigns']  = assignment
        if request.method == 'POST':
            print("post request")
            order_amount = 20000
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
            details = PaymentDetails.objects.create(username = request.user, amount = order_amount/100, currency = order_currency, receipt = order_receipt, orderid = order_id, status = order_status, subject_code = sub_code )
            details.save()
            if order_status=='created':

            # Server data for user convinience
            # data that'll be send to the razorpay for
                context['order_id'] = order_id

                context['assigns'] = assignment
                return render(request, 'assignment_sols.html', context)

        
        try:
            details = PaymentDetails.objects.all().filter(username = request.user)
            
            for pay_details in details:
                if pay_details.subject_code == sub_code and pay_details.username == request.user and pay_details.status == "created":
                    context['permission'] = "Allowed"
                    context['assigns'] = assignment
                    return render(request, "assignment_sols.html", context)
            return render(request, "assignment_sols.html", context)
        except:
            return render(request, "assignment_sols.html", {"assigns" : assignment})

    except:
        return render(request, "assignment_sols.html", {"assignNot" : "Not Found"})

def nmims(request):
    return render(request, "nmims.html")
 
def amity(request):
    return render(request, "amity.html")

def myprofile(request):
    return render(request, "myprofile.html")

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
    try:
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
    except:
        return render(request, "index.html")

def requested_assignment(request):
    try:
        if request.method == 'POST':
            obj = RequestedAssignment.objects.create(username = request.user, fullname = request.POST['fullname'], email = request.POST['email'], contact_no = request.POST['contact'], subject_name = request.POST['subject'], college = request.POST['college'], special_mention = request.POST['mention'])
            obj.save()
            return redirect('home')
        return render(request, 'requested_assignment.html')
    except:
        return render(request, 'requested_assignment.html')


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

        details = PaymentDetails.objects.create(username = request.user, amount = order_amount/100, currency = order_currency, receipt = order_receipt, orderid = order_id, status = order_status )
        details.save()
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
