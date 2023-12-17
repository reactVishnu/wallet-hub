from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.


def base_view(request):
    return render(request, 'operations/login.html')


def home_view(request):
    return render(request, 'operations/home.html')


def login_view(request):
    print("request is coming")
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('operations:success'))
        else:
            messages.error(request, 'Email or Password is incorrect. Please try again')
            return render(request, 'operations/login.html', {'current_page': 'login'})
    return render(request, 'operations/login.html', {'current_page': 'login'})


@login_required()
def success_view(request):
    return render(request, 'operations/success.html')


def signup_view(request):
    try:
        User = get_user_model()
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            name = request.POST['name']
            my_group = Group.objects.get(name='Customer')
            print("collection succesfull")
            # Checking if email already exists
            if User.objects.filter(email=email).exists():
                # Add an error message for email already registered
                messages.error(request, 'Email address is already registered.')
                messages.error(request, 'SignUp Unsuccessful')
                print('email filter')
                return render(request, 'operations/signup.html', {'current_page': 'signup'})

            # Password Length
            if len(password) < 8:
                # Add an error message for a too short password
                messages.error(request, 'Password is too short. It should be at least 8 characters.')
                messages.error(request, 'SignUp Unsuccessful')
                print('pass run')
                return render(request, 'operations/signup.html', {'current_page': 'signup'})

            print("Validation run succesfull")
            user = get_user_model().objects.create_user(name=name, email=email, password=password)
            my_group.user_set.add(user)
            print("created succesfull")
            return render(request, 'operations/login.html', {'current_page': 'signup'})

    except Exception as e:
        messages.error(request, 'Exception Ocurred')
        return render(request, 'operations/signup.html', {'current_page': 'signup'})

    return render(request, 'operations/signup.html', {'current_page': 'signup'})
