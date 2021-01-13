from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class MyRateThrotteler(UserRateThrottle):
    scope = 'newthrottel'