from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Authentication.authentication import SessionJWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import *
from ..serializers import *
from ..renderers import UserRenderer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Login & Logout"])
class LoginHistoryView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionJWTAuthentication]

    def get(self, request):

        user = request.user

        try:
            limit = int(
                request.query_params.get('limit', 10)
            )
        except ValueError:
            return Response(
                {
                    'error': 'Limit must be a number'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Clamp limit between 1 and 100
        limit = max(1, min(limit, 100))

        history = LoginHistory.objects.filter(
            user=user
        )[:limit]

        data = [
            {
                'ip_address': log.ip_address,
                'user_agent': log.user_agent,
                'login_time': log.login_time.isoformat(),
                'is_successful': log.is_successful,
                'failure_reason': log.failure_reason
            }
            for log in history
        ]

        return Response(
            data,
            status=status.HTTP_200_OK
        )


@extend_schema(tags=["Login & Logout"])
class ActiveSessionsView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionJWTAuthentication]

    def get(self, request):

        sessions = UserSession.objects.filter(
            user=request.user,
            is_active=True
        ).order_by('-last_activity')

        current_jti = request.auth.payload.get('jti')

        serializer = UserSessionSerializer(
            sessions,
            many=True,
            context={
                'current_jti': current_jti
            }
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )



# Logout from specific device
@extend_schema(tags=["Login & Logout"])
class DeleteSessionView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionJWTAuthentication]

    def delete(self, request, session_id):

        try:
            user = request.user

            current_jti = request.auth.payload.get('jti')

            # Find user's session
            session = UserSession.objects.get(
                id=session_id,
                user=user,
                is_active=True
            )

            # Prevent current session logout
            if session.session_jti == current_jti:
                return Response(
                    {
                        'error': 'You cannot logout your current session'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Blacklist refresh token
            token = RefreshToken(session.refresh_token)
            token.blacklist()

            # Mark session inactive
            session.is_active = False
            session.save()

            return Response(
                {
                    'msg': 'Session logged out successfully'
                },
                status=status.HTTP_200_OK
            )

        except UserSession.DoesNotExist:
            return Response(
                {
                    'error': 'Session not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception:
            return Response(
                {
                    'error': 'Failed to logout session'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
