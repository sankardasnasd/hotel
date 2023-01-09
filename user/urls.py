from django.urls import path
from .import views 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
   path('user',views.user),  

   path('homepage',views.homepage,name='homepage'),
   
   path('signup',views.signup,name='signup'),
   path('hotel-detail<uid>/' ,views.hotel_detail , name="hotel_detail"),
   path('signin',views.signin, name='signin'),
   path('check_booking/' ,views.check_booking),
   path('',views.login_page1,name='login_page')
  
  

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
