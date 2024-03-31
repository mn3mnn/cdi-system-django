from django.urls import path
from welly import welly_views
app_name='welly'
urlpatterns = [
    path('',welly_views.index,name="index"),
    path('index/',welly_views.index,name="index"),
    path('work-list/',welly_views.work_list,name="work-list"),

    path('assign/',welly_views.assign,name="assign"),

    path('details/<work_list_id>/',welly_views.details,name="details"),
    path('notifications/',welly_views.notifications,name="notifications"),

    path('page-login/',welly_views.page_login,name="page-login"),
    path('page-logout/',welly_views.page_logout,name="page-logout"),
    path('page-register/',welly_views.page_register,name="page-register"),
    path('page-forgot-password/',welly_views.page_forgot_password,name="page-forgot-password"),
    path('page-lock-screen/',welly_views.page_lock_screen,name="page-lock-screen"),
    path('page-empty/',welly_views.page_empty,name="page-empty"),
    path('page-error-400/',welly_views.page_error_400,name="page-error-400"),
    path('page-error-403/',welly_views.page_error_403,name="page-error-403"),
    path('page-error-404/',welly_views.page_error_404,name="page-error-404"),
    path('page-error-500/',welly_views.page_error_500,name="page-error-500"),
    path('page-error-503/',welly_views.page_error_503,name="page-error-503"),

]