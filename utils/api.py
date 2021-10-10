
from typing import Dict, Optional, Union

from django.http import JsonResponse
from rest_framework import status


class CustomJsonResponse(JsonResponse):
    def __init__(
            self,
            data: Dict,
            errors: Optional[Union[Dict, str]] = None,
            error_code: int = status.HTTP_404_NOT_FOUND,
            success_code: int = status.HTTP_200_OK,
            **kwargs
    ):
        if errors is not None:
            resp_data = {
                "success": False,
                "message": None,
                "error": errors,
            }
            code = error_code
        else:
            resp_data = {
                "success": True,
                "message": data,
                "error": None,
            }
            code = success_code
        super().__init__(resp_data, status=code, **kwargs)