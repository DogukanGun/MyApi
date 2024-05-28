from enum import Enum


class UserScopes(Enum):
    ADMIN_REVIEW = "admin:review"
    ADMIN_EDIT = "admin:edit"
    USER_READ = "user:read"
    USER_WRITE = "user:write"
