from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewEventForm, NewCommentForm,  AddAdressForm
from .models import Post, Comment, Event, Address
from django.views.generic import ListView, RedirectView
from django.contrib.auth import authenticate
from decimal import *
import datetime
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import redirect

degreesOfCloseness = Decimal('0.5') # this sets the range of closeness for near posts in degrees of the world


# Blog Page
def blog(request):
    return render(request, 'blog.html')


def events(request):
    eventListMazSize = 12 #number of event to be display on the page
    events_near = []
    events_faraway = []
    user = request.user
    eventsAll = Event.objects.all()
    reversedEventsAll = reversed(eventsAll)
    if (request.user.is_authenticated and not user.address == None):
        for event in reversedEventsAll:
            if (event.dateTime > datetime.datetime.now()): #only gets future eventt, using UTC time
                if (event.addressID!=None and user.is_authenticated):
                    if ((event.addressID.latitude - degreesOfCloseness < user.address.latitude) and (event.addressID.latitude + degreesOfCloseness > user.address.latitude) and
                            (event.addressID.longitude - degreesOfCloseness < user.address.longitude) and (event.addressID.longitude + degreesOfCloseness > user.address.longitude)):
                            if (len(events_near) < eventListMazSize):
                                events_near.append(event)
                    else:
                        if (len(events_faraway) < eventListMazSize):
                            events_faraway.append(event)
                else:
                    if (len(events_faraway) < eventListMazSize):
                        events_faraway.append(event)


    context = {
        "event_list_far": events_faraway,
        "event_list_local": events_near,
        "event_list_all": eventsAll,
    }
    return render(request, "events.html", context )

@login_required(login_url="/accounts/login/")
def add_event(request):
    if (request.user.is_authenticated):
        if (request.method == 'POST'):
            form = NewEventForm(request.POST, request.FILES)
            if form.is_valid():
                your_object = form.save(commit=False)
                your_object.userId = request.user
                title = form.cleaned_data.get('title'),
                details = form.cleaned_data.get('details'),
                dateTime = form.cleaned_data.get('dateTime'),
                image = form.cleaned_data.get('image')
                your_object.save()
                add_address_path =  'add_new_event/'+ str(your_object.id)
                #url = reverse('blog:event:eventid', kwargs={ 'eventid': your_object.id })
                return HttpResponseRedirect(add_address_path)
                #return redirect('events/add_event/<add_address_path>')
        else:
            form = NewEventForm(request.POST, request.FILES)
        return render(request, 'events/add_event.html', {'form':form})
    else:
        return render(request, 'events/login_to_add_event.html')


def add_address(request, eventid):
    event = Event.objects.get(id=eventid)
    if (event.userId == request.user):
        if request.method == 'POST':
            form = AddAdressForm(request.POST)
            if form.is_valid():
                addressLine1 = form.cleaned_data.get('addressLine1')
                addressLine2 = form.cleaned_data.get('addressLine2')
                suburbCity = form.cleaned_data.get('suburbCity')
                country = form.cleaned_data.get('country')
                stateProvince = form.cleaned_data.get('stateProvince')
                zipCode = form.cleaned_data.get('zipCode')
                latitude = form.cleaned_data.get('latitude')
                longitude = form.cleaned_data.get('longitude')
                obj = form.save()
                add = obj.id    # Assign Address to User
                a = Address.objects.get(id=add)
                event.addressID = a
                event.save()
                return redirect('events')
        else:
            form = AddAdressForm()
        return render(request, 'add_address.html', {'form':form})
    else:
        return render(request, 'events/what_are_you_doing_here.html')

# Post Blog
@login_required(login_url="/accounts/login/")
def get_new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            your_object = form.save(commit=False)
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            image = form.cleaned_data.get('image')
            your_object.user = request.user
            your_object.save()
            return redirect('blog')
    else:
        form = NewPostForm(request.POST, request.FILES)
    return render(request, 'post_blog.html', {'form':form})

# Edit Profile
@login_required(login_url="/accounts/login/")
def update_post(request, postid):
    post = Post.objects.get(pk=postid)
    if(post.user == request.user):
        if request.method == 'POST':
            form = NewPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                image = form.cleaned_data.get('image')
                form.save()
                return redirect('blog')
        else:
            form = NewPostForm(instance=post)
        return render(request, 'update_post.html', {'form':form, 'post': post})
    else:
        return render(request, 'events/what_are_you_doing_here.html')

# Add Blog Comment
def add_comment(request, postid):
    post = Post.objects.get(pk=postid)
    comments = post.comment_set.all()
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            your_object = form.save(commit=False)
            comment = form.cleaned_data.get('comment')
            your_object.userId = request.user
            your_object.postId = Post.objects.get(pk=postid)
            your_object.save()
            return HttpResponseRedirect('/blog', {'form':form, 'post':post, 'comments':comments})
    else:
        form = NewCommentForm(request.POST, request.FILES)
    return render(request, 'blog/add_comment.html', {'form':form, 'post':post, 'comments':comments})

# Change or delete you comment
@login_required(login_url="/accounts/login/")
def edit_comment(request, commentid):
    comment = Comment.objects.get(pk=commentid)
    #comment.comment.placeholder = comment.comment
    if (comment.userId == request.user):
        if request.method == "POST":
            form = NewCommentForm(request.POST or None, instance=comment)
            if form.is_valid():
                your_object = form.save(commit=False)
                comment = form.cleaned_data.get('comment')
                your_object.save()
                form = NewCommentForm(request.POST)
                post = Comment.objects.get(pk=commentid).postId
                comments = post.comment_set.all()
                return render(request, "blog/add_comment.html", {'form':form, 'post':post, 'comments':comments})
        else:
            form = NewCommentForm(request.POST, request.FILES)
        return render(request, 'blog/edit_comment.html', {'form':form, 'comment':comment})
    else:
        return render(request, 'events/what_are_you_doing_here.html')

# deletes a comment
@login_required(login_url="/accounts/login/")
def delete_comment(request, commentid, template_name='blog/comment_confirm_delete.html'):
    comment = get_object_or_404(Comment, pk=commentid)
    if (comment.userId == request.user):
        if request.method=='POST':
            post = Comment.objects.get(pk=commentid).postId
            comment.delete()
            form = NewCommentForm(request.POST)
            comments = post.comment_set.all()
            return render(request, "blog/add_comment.html", {'form':form, 'post':post, 'comments':comments})
        return render(request, template_name, {'comment':comment})
    else:
        return render(request, 'events/what_are_you_doing_here.html')

# Delete a blog
@login_required(login_url="/accounts/login/")
def delete_blog(request, postid, template_name='blog/confirm_delete.html'):
    post = get_object_or_404(Post, pk=postid)
    if (post.user == request.user):
        if request.method=='POST':
            post.delete()
            return render(request, "blog.html")
        return render(request, template_name, {'post': post})
    else:
        return render(request, 'events/what_are_you_doing_here.html')

# View Blogs
def all_blogs(request):
    blogListMaxSize = 12 #number of blogs to be display on the page
    posts2 = []
    posts3 = []
    user = request.user
    postsAll = Post.objects.all()
    postsAllR = reversed(postsAll)

    if (request.user.is_authenticated and not user.address == None):
        for post in postsAllR:
            if (not post.user.address==None):
                if (post.user.address.latitude - degreesOfCloseness< user.address.latitude and post.user.address.latitude + degreesOfCloseness > user.address.latitude and
                    post.user.address.longitude-degreesOfCloseness< user.address.longitude and post.user.address.longitude+degreesOfCloseness > user.address.longitude):
                    if (len(posts2) < blogListMaxSize):
                        posts2.append(post)
                else:
                    if (len(posts3) < blogListMaxSize):
                        posts3.append(post)

            else:
                if (len(posts3) < blogListMaxSize):
                    posts3.append(post)

    commentsof3 = []
    postCount = 0
    comments = Comment.objects.all()
    for post in postsAll:
        postCount = 0
        commentsForThisPost = reversed(Comment.objects.filter(postId_id= post.id))
        for comment in commentsForThisPost:
            if postCount < 3: #set number of comments to appear here
                commentsof3.append(comment)
                postCount = postCount + 1

    context = {
        "post_list": posts3,
        "post_list2": posts2,
        "post_notloggedin": postsAllR,
        "comment_list": commentsof3,
    }
    return render(request, "blog.html", context )



# LIKES

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class PostLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id = self.kwargs.get("id")
        post = get_object_or_404(Post, id=id)
        post_url = post.get_absolute_url()
        user = self.request.user
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        return post_url

class PostLikeAPI(APIView):
    authentication_classes = [authentication.SessionAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, id=None, format=None):
        #id = self.kwargs.get("id")
        post = get_object_or_404(Post, id=id)
        post_url = post.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False

        if user in post.likes.all():
            liked = False
            post.likes.remove(user)
        else:
            liked = True
            post.likes.add(user)
        updated= True
        total = post.likes.count()
        data = {
            "updated": updated,
            "liked": liked,
            "total": total,
        }
        return Response(data)

# What Can Be Done Page
def whatcanbedone(request):
    return render(request, 'whatcanbedone.html')
