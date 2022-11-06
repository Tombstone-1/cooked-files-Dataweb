from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #routes
     path('', views.home_view, name="home"),
     path('login', views.login_view, name="login"),
     path('logout', views.logout_user, name="logout"),
     path('dashboard', views.dashboard_view, name="dashboard"),
     path('register', views.register_view, name="register"),

     #tables
     path('artable', views.ar_table_view, name="artable"),
     path('sale', views.sale_table_view, name="sale"),
     path('purchase', views.purchase_table_view, name="purchase"),
     path('parties', views.parties_table_view, name="parties"),

     #password reset
     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
          name='password_change_done'),
     path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
          name='password_change'),
     path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
          name='password_reset_done'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm_form.html'), 
               name='password_reset_confirm'),
     path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'), 
               name='password_reset'),
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
          name='password_reset_complete'),


]