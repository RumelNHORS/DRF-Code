from rest_framework.throttling import UserRateThrottle

class RumelRateThrottle(UserRateThrottle):
    scope = 'rumel'