from fastapi import HTTPException

def require_permission(permission_name):

    def checker():
        return True

    return checker