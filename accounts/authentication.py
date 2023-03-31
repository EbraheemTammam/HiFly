from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuth(BaseTokenAuth):
    keyword = 'Bearer'