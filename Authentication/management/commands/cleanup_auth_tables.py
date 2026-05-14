from datetime import timedelta

from django.conf import settings
from django.core.management import BaseCommand, call_command
from django.core.management.base import BaseCommand
from django.utils import timezone
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from Authentication.models import LoginHistory, TwoFALog, UserSession


class Command(BaseCommand):
    help = (
        'Clean old authentication audit rows, inactive sessions, and expired '
        'SimpleJWT outstanding/blacklisted tokens.'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--login-history-days',
            type=int,
            default=settings.LOGIN_HISTORY_RETENTION_DAYS,
            help='Delete LoginHistory rows older than this many days.',
        )
        parser.add_argument(
            '--inactive-session-days',
            type=int,
            default=settings.INACTIVE_SESSION_RETENTION_DAYS,
            help='Delete inactive UserSession rows older than this many days.',
        )
        parser.add_argument(
            '--two-fa-log-days',
            type=int,
            default=settings.TWO_FA_LOG_RETENTION_DAYS,
            help='Delete TwoFALog rows older than this many days.',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without deleting anything.',
        )

    def handle(self, *args, **options):
        now = timezone.now()
        dry_run = options['dry_run']

        login_history_cutoff = now - timedelta(
            days=options['login_history_days']
        )
        inactive_session_cutoff = now - timedelta(
            days=options['inactive_session_days']
        )
        two_fa_log_cutoff = now - timedelta(
            days=options['two_fa_log_days']
        )

        cleanup_targets = [
            (
                'LoginHistory',
                LoginHistory.objects.filter(
                    login_time__lt=login_history_cutoff
                ),
            ),
            (
                'Inactive UserSession',
                UserSession.objects.filter(
                    is_active=False,
                    last_activity__lt=inactive_session_cutoff,
                ),
            ),
            (
                'TwoFALog',
                TwoFALog.objects.filter(
                    timestamp__lt=two_fa_log_cutoff
                ),
            ),
        ]

        for label, queryset in cleanup_targets:
            count = queryset.count()
            if dry_run:
                self.stdout.write(f'{label}: {count} row(s) would be deleted.')
                continue

            deleted_count, _ = queryset.delete()
            self.stdout.write(f'{label}: {deleted_count} row(s) deleted.')

        expired_token_count = OutstandingToken.objects.filter(
            expires_at__lt=now
        ).count()

        if dry_run:
            self.stdout.write(
                'Expired SimpleJWT OutstandingToken/BlacklistedToken: '
                f'{expired_token_count} token(s) would be cleaned.'
            )
        else:
            call_command('flushexpiredtokens', verbosity=0)
            self.stdout.write(
                'Expired SimpleJWT OutstandingToken/BlacklistedToken: '
                f'{expired_token_count} token(s) cleaned.'
            )

        self.stdout.write(self.style.SUCCESS('Auth cleanup completed.'))
