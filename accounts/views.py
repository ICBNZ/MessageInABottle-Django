from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, AddAdressForm, CustomUserChangeForm
from .models import User, Address
from blog.models import Post, Event
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import DetailView, TemplateView, ListView

def home_blogs(request):
    user = request.user
    postsAll = Post.objects.all()
    posts = reversed(postsAll)
    three_latest_post = []
    postCount = 0
    for post in posts:
        if (postCount<3):
            three_latest_post.append(post)
        postCount = postCount + 1

    context = {
        "three_latest_post":three_latest_post,
    }
    return render(request, "home.html", context )


# Signup
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# View Profile
@login_required(login_url="/accounts/login/")
def profile(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    events = Event.objects.filter(userId=user)
    return render(request, 'profile.html', {'user': user, 'posts': posts, 'events': events})

# Edit Profile
@login_required(login_url="/accounts/login/")
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            image = form.cleaned_data.get('image')
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'edit_profile.html', {'form':form})




# Edit Password
@login_required(login_url="/accounts/login/")
def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'edit_password.html', {'form': form})

# Edit Address
@login_required(login_url="/accounts/login/")
def add_address(request):
    if request.method == 'POST':
        form = AddAdressForm(request.POST)
        if form.is_valid():
            obj = form.save()
            addressLine1 = form.cleaned_data.get('addressLine1')
            addressLine2 = form.cleaned_data.get('addressLine2')
            suburbCity = form.cleaned_data.get('suburbCity')
            country = form.cleaned_data.get('country')
            stateProvince = form.cleaned_data.get('stateProvince')
            zipCode = form.cleaned_data.get('zipCode')
            latitude = form.cleaned_data.get('latitude')
            longitude = form.cleaned_data.get('longitude')
            add = obj.id    # Assign Address to User
            a = Address.objects.get(id=add)
            user = request.user
            user.address = a
            user.save()
            return redirect('profile')
    else:
        form = AddAdressForm()
    return render(request, 'add_address.html', {'form':form})
