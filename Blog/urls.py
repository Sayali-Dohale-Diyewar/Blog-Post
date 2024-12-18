from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
    path('',Blogpost, name="Blog"),
    path('comment/<int:id>/',CommentBlogPost, name="Comment"),
    path('delete/<int:id>',ReplyBlogPost, name="Reply"),
    path('register/',Register, name="Register"),
    path('login/',Login, name='login'),


]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )