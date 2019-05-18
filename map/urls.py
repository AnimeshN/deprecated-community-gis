from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

# from communitygis.core import views as core_views


urlpatterns = [
	path('',views.front,name = 'front'),
    path('home/',views.home,name= 'home'),
    path('login/',views.login_user, name = 'login'),
    path('logout/',views.logout_user, name = 'logoutU'),
    path('signup/',views.signup_user, name = 'signup'),
    
    path('change_password/',views.change_password, name = 'changepass'),
    # path(r'^signup/$', core_views.signup, name='signup'),)

    path('demo/',views.demo,name='demo'),
    path('home/swm/',views.solidWasteManagement,name = 'swm'),
    path('home/census/',views.census,name = 'census'),
    path('home/iitbombay/',views.iitBombay,name = 'iit'),
    path('home/education/',views.education,name = 'edu'),
    path('test/',views.test,name = 'test'),
    path('home/health/',views.health,name = 'health'),
    path('home/water/',views.water,name = 'water'),
    path('home/transport/',views.transport,name = 'transport'),

    path('uploadlayer/',views.upload_layers,name='upload_layers'),
    path('showupload/',views.show_upload,name='show_upload'),
    path('deleteupload/<int:pk>/',views.delete_upload,name='delete_upload'),
    path('showallupload/',views.show_all_upload,name='show_all_upload'),
    url(r'^auth/', include('social_django.urls', namespace='social'))


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

