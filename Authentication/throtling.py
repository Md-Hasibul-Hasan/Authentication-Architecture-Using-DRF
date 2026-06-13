from rest_framework.throttling import UserRateThrottle


class MyRateThrottle(UserRateThrottle):
    scope = 'custom_user_1'