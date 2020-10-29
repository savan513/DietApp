from django.urls import path,re_path
from . import  views
urlpatterns = [
    path("",views.index,name="Home"),

    path('login/',views.loginProcess,name="login"),
    path('logout/',views.logoutProcess,name="logout"),
    path('getplan/',views.getplan,name="getplan"),
    path('checkusername/',views.checkusername,name="checkusername"),
    path('checkemail/',views.checkemail,name="checkemail"),
    path('saveandpay/',views.save_and_pay,name="saveandpay"),
    path('filluserdata/',views.filluserdata,name="filluserdata"),
    path('contactus/',views.contactus,name="contactus"),
    path('sendrequest/',views.sendrequest,name="sendrequest"),
    path('updatedata/',views.updatedata,name="updatedata"),
    path('updateplan/<int:id>/',views.updateplan,name="updateplan"),

    path('userdashboard/',views.userdashboard,name="userdashboard"),
    path('dietitiandashboard/',views.dietitiandashboard,name="dietitiandashboard"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("handleplanchange/", views.handleplanchange, name="handleplanchange"),
    path("wholechange/", views.wholechange, name="wholechange"),
    path("acceptrequest/<int:id>/", views.acceptrequest, name="acceptrequest"),
    path("deleterequest/<int:id>/", views.deleterequest, name="deleterequest"),
    path("dietitiandashboard/senddietchart/", views.senddietchart, name="senddietchart"),
    path("feedback/", views.review, name="review"),
    path("checkrefferalcode/<str:code>", views.checkrefferalcode, name="checkrefferalcode"),
    path("updatewholeplan/", views.updatewholeplan, name="updatewholeplan"),
    path("checkfilleddata/", views.checkfilleddata, name="checkfilleddata"),
    path("create_room/<int:mid>", views.create_room, name="create_room"),
    path("/join_room/<int:id>", views.join_room, name="Join_room"),
    path("end_chat/<int:id>", views.end_chat, name="end_chat"),
    path("week_report/", views.week_report, name="week_report"),
    path("changepass/", views.changepass, name="changepass"),
    path("forgetpassword/",views.forgetpassword,name="forgetpassword"),
    path('getpassword/',views.getpassword,name="getpassword"),
    path('deletcinactive/',views.deletcinactive,name="deletcinactive"),
    path('checkmeetingstatus/',views.checkmeetingstatus,name="checkmeetingstatus"),

    path('endcall/<int:id>',views.endcall,name="endcall"),
]