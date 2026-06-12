from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from rest_framework.permissions import AllowAny

from ..renderers import UserRenderer
from ..models import User, UserSession
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["Token"],
    summary="Refresh JWT Token",
    description="Generate a new access token using a valid refresh token."
)
class SessionTokenRefreshView(TokenRefreshView):
    renderer_classes = [UserRenderer]
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response(
                {'refresh': ['This field is required.']},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            refresh = RefreshToken(refresh_token)
            user_id = refresh['user_id']
            user = User.objects.get(id=user_id)
            user_session = UserSession.objects.get(
                user=user,
                refresh_token=refresh_token,
                is_active=True
            )
        except (TokenError, User.DoesNotExist, UserSession.DoesNotExist):
            return Response(
                {'detail': 'Token is invalid or expired'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        access = AccessToken(serializer.validated_data['access'])
        user_session.session_jti = str(access['jti'])

        if serializer.validated_data.get('refresh'):
            user_session.refresh_token = serializer.validated_data['refresh']

        user_session.save(
            update_fields=[
                'refresh_token',
                'session_jti',
                'last_activity',
            ]
        )

        return Response(serializer.validated_data, status=status.HTTP_200_OK)



@extend_schema(
    tags=["Token"],
    summary="Verify JWT Token",
    description="Verify whether a JWT token is valid."
)
class CustomTokenVerifyView(TokenVerifyView):
    pass