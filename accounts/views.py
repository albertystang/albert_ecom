from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from .forms import RegistrationForm
from .models import Account


def register_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have registered successfully...')            
            # user authentication
            # current_site = get_current_site(request)
            # mail_subject = 'Please activate your account'
            # message = render_to_string('accounts/account_verification_email.html', {
            #     'user': user,
            #     'domain': current_site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            # to_email = email
            # send_email = EmailMessage(mail_subject, message, to=[to_email])
            # send_email.send()
            # messages.success(request, 'You have registered successfully...')
            return redirect('store')
    return render(request, 'accounts/register.html', {'form': form})


# def activate(request, uidb64, token):
#     return HttpResponse('ok')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            user.is_active = True
            login(request, user)
            messages.success(request, 'You have logged in successfully...')
            return redirect('dashboard')
    return render(request, 'accounts/login.html')


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out successfully...')
    return redirect('home')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')