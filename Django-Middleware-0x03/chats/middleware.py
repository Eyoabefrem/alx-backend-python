# chats/middleware.py

import logging
from datetime import datetime

# Configure logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler('requests.log')
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logger.info(log_message)

        response = self.get_response(request)
        return response

from datetime import datetime
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current hour (24-hour format)
        current_hour = datetime.now().hour

        # Allow access only between 18:00 (6PM) and 21:00 (9PM)
        if not (18 <= current_hour < 21):
            return HttpResponseForbidden(
                "<h1>403 Forbidden</h1><p>Access to the messaging app is only allowed between 6PM and 9PM.</p>"
            )

        response = self.get_response(request)
        return response

import time
from django.http import JsonResponse

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to store message timestamps per IP
        self.message_log = {}

    def __call__(self, request):
        if request.method == 'POST' and request.path.startswith('/api/messages/'):
            ip = self.get_client_ip(request)
            current_time = time.time()

            if ip not in self.message_log:
                self.message_log[ip] = []

            # Remove timestamps older than 60 seconds
            self.message_log[ip] = [
                timestamp for timestamp in self.message_log[ip]
                if current_time - timestamp < 60
            ]

            if len(self.message_log[ip]) >= 5:
                return JsonResponse({
                    'detail': 'Message limit exceeded. Max 5 messages per minute allowed.'
                }, status=429)  # 429 Too Many Requests

            self.message_log[ip].append(current_time)

        return self.get_response(request)

    def get_client_ip(self, request):
        """Extract the IP address from the request headers"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')

from django.http import HttpResponseForbidden

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Assuming your user model has a 'role' attribute:
        user = request.user

        # Allow anonymous users to pass or you can deny here if needed
        if not user.is_authenticated:
            return HttpResponseForbidden("Authentication required")

        # Check user role for restricted paths, e.g., chat actions:
        restricted_paths = [
            '/api/messages/',        # Adjust paths based on your app routes
            '/api/conversations/'
        ]

        # If request path starts with any restricted path, check role
        if any(request.path.startswith(path) for path in restricted_paths):
            if user.role not in ['admin', 'moderator']:
                return HttpResponseForbidden("You do not have permission to perform this action.")

        return self.get_response(request)
