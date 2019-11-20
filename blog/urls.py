from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import all_blogs, add_comment, add_event, edit_comment, delete_comment, PostLikeRedirect, PostLikeAPI

# path: url, views file.profile function
urlpatterns = [
    path('', views.all_blogs, name='blog'),
    path('events/', views.events, name='events'),
    path('events/add_new_event', views.add_event, name='add_events'),
    path('whatcanbedone/', views.whatcanbedone, name='whatcanbedone'),
    path('post_blog/', views.get_new_post, name='new_post'),
    path('post_blog/<int:postid>', views.update_post, name='update_post'),
    path('<int:postid>', views.add_comment, name="comment_section"),
    path('<int:id>/like', PostLikeRedirect.as_view(), name="like-toggle"),
    path('api/<int:id>/like', PostLikeAPI.as_view(), name="like-api"),
    path('edit_comment/<int:commentid>', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:commentid>', views.delete_comment, name='delete_comment'),
    path('delete_blog/<int:postid>', views.delete_blog, name='delete_blog'),
    path('events/add_new_event', views.add_event, name='add_events'),
    url(r'^events/add_new_event/(?P<eventid>\d+)', views.add_address, name='add_event_address'),

]
