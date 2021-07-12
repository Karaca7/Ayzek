from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView

from oz import views
from oz.views import ana,giris,kayıt,deneme,matematiks,mantıks,mantıkdeneme,baslangıc,baslangıcdeneme,felsefes,felsefedeneme,yazılıms,yazılımdeneme,iletisim
from django.urls import include
from django.contrib.auth.views import LogoutView, PasswordChangeView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("",ana,name='ana'),
    path('giris/', views.giris, name='giris'),

    path('ev/', include('ev.urls')),
    path('kayıt/',kayıt,name='kayıt' ),
    path('captcha/', include('captcha.urls')),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='oz/registration/password_reset_form.html'),name='password_reset_form'),
    path('reset-password/done/',auth_views.PasswordResetDoneView.as_view(template_name='oz/registration/password_reset_done.html'),name='password_reset_done'),

    path('reset-password/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='oz/registration/password_reset_confirm.html')
         ,name='password_reset_confirm'),
    path('reset-password/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='oz/registration/password_reset_complete.html')),
    path('deneme/<int:id>/',deneme,name='deneme'),
    path('matematiks/',matematiks,name='matematiks'),
    path('mantıks/',mantıks,name='mantıks'),
    path('mantıkdeneme/<int:id>/', mantıkdeneme, name='mantıkdeneme'),
    path('baslangıc/', baslangıc, name='baslangıc'),
    path('baslangıcdeneme/<int:id>/', baslangıcdeneme, name='baslangıcdeneme'),
    path('felsefes/', felsefes, name='felsefes'),
    path('felsefedeneme/<int:id>/', felsefedeneme, name='felsefedeneme'),
    path('yazılıms/', yazılıms, name='yazılıms'),
    path('yazılımdeneme/<int:id>/', yazılımdeneme, name='yazılımdeneme'),
    path('iletisim/', iletisim, name='iletisim'),






]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





