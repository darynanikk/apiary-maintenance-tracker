from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from knox.auth import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


@database_sync_to_async
def get_user(token):
    try:
        print('token', token)
        knox_auth = TokenAuthentication()
        user, token = knox_auth.authenticate_credentials(token)
        print(f"user:{user}")
    except AuthenticationFailed:
        print('Token is invalid or expired.')
        return AnonymousUser()
    return user


class TokenAuthMiddleware(BaseMiddleware):

    async def __call__(self, scope, receive, send):
        close_old_connections()
        try:
            print(scope)
            token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
        except ValueError:
            token_key = None

        scope['user'] = await get_user(token_key)
        print('auth middleware')
        print('user', scope['user'])
        return await super().__call__(scope, receive, send)


def KnoxAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(inner)
