import logging

# Configure logging
logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        # Log request details
        logger.info(f"Request Method: {request.method}")
        logger.info(f"Request Path: {request.get_full_path()}")

        # Process the request
        response = self.get_response(request)

        # Log response details
        logger.info(f"Response Status Code: {response.status_code}")

        return response
