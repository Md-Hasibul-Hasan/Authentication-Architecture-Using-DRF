from django.urls import include, path
from . import views


from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'permissions', views.PermissionViewSet, basename='permission')
router.register(r'groups', views.GroupViewSet, basename='group')
router.register(r"user-access",views.UserGroupPermissionViewSet,basename="user-access")


urlpatterns = [

    path('', include(router.urls)), 

    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify-email/<uid>/<token>/', views.VerifyEmailView.as_view(), name='verify-email'),
    path('verify-otp/', views.VerifyOTPView.as_view(), name='verify-otp'),
    path('resend-verification/', views.ResendVerificationEmailView.as_view(), name='resend-verification'),
    
    path('google-login/', views.GoogleLoginView.as_view(), name='google-login'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('2fa/verify/', views.Verify2FAView.as_view(), name='verify-2fa'),
    path('2fa/setup/', views.Setup2FAView.as_view(), name='setup-2fa'),
    path('2fa/enable/', views.Enable2FAView.as_view(), name='enable-2fa'),
    path('2fa/disable/', views.Disable2FAView.as_view(), name='disable-2fa'),
    path('2fa/status/', views.Get2FAStatusView.as_view(), name='2fa-status'),


    path('login-history/', views.LoginHistoryView.as_view(), name='login-history'),
    path('active-sessions/',views.ActiveSessionsView.as_view(),name='active-sessions'),
    path('delete-session/<session_id>/',views.DeleteSessionView.as_view(),name='delete-session'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout-all/', views.LogoutAllDevicesView.as_view(), name='logout-all'),


    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/request/', views.SendResetPasswordEmailView.as_view(), name='reset-password-request'),
    path('reset-password/by-link/<uid>/<token>/', views.ResetPasswordView.as_view(), name='reset-password-by-link'),
    path('reset-password/by-otp/', views.ResetPasswordWithOTPView.as_view(), name='reset-password-by-otp'),
    


    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('change-email/request/', views.ChangeEmailView.as_view(), name='request-change-email'),
    path('change-email/confirm/', views.ConfirmChangeEmailView.as_view(), name='confirm-change-email'),
    path('delete-account/', views.DeleteAccountView.as_view(), name='delete-account'),


    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', views.CustomTokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', views.SessionTokenRefreshView.as_view(), name='token_refresh'),


]
