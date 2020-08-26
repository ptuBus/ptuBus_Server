from rest_framework.exceptions import PermissionDenied

class ptuBusErrorExcpetion(PermissionDenied):
    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code