from django.conf.urls import url
from . import views 
from django.contrib.auth.views import login

app_name = 'shifts_app'

urlpatterns = [ 

    url(r'^$', views.selection_page, name= 'selection_page'),  
    url(r'^employee_main/$', views.employee_main, name= 'employee_main'),  
    url(r'^sup_main/$',views.sup_main, name='sup_main'), 
    url(r'^login/$', login, {'template_name':'shifts_app/login.html'}), 
    url(r'^add_shifts/$',views.add_shifts, name='add_shifts'),   

    url(r'^monday/$',views.monday, name='monday'), 
    url(r'^tuesday/$',views.tuesday, name='tuesday'),
    url(r'^wednesday/$',views.wednesday, name='wednesday'),
    url(r'^thursday/$',views.thursday, name='thursday'),
    url(r'^friday/$',views.friday, name='friday'),
    url(r'^saturday/$',views.saturday, name='saturday'),
    url(r'^sunday/$',views.sunday, name='sunday'),

    #url(r'^(?P<group_id>[0-9]+)/$',views.index, name='index'),


    url(r'^shift_cover/$',views.shift_cover, name='shift_cover'),
    url(r'^(?P<shift_id>[0-9]+)/$',views.detail, name='detail'),
    
    url(r'shift/(?P<pk>[0-9]+)/delete/$',views.ShiftDelete.as_view(),name='shift-delete'),
    url(r'^chat_room/$',views.chat_room, name='chat_room'),
]