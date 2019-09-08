import logging
from functools import wraps
from django.db import IntegrityError
from rest_framework import status
from user.v1.serializers import AuthenticationSerializer
from admin_user.v1.serializers import AdminAuthenticationSerializer
from . responses import MetaDataResponse
from . exceptions import NotAcceptableError, NotAllowedException, NotFoundException


def session_authorize(user_id_key='pk', *args, **kwargs):
    def deco(f):
        def abstract_user_id(request):
            if request.method == 'GET':
                user_id = request.query_params.get(user_id_key)[0]
            else:
                user_id = request.data.get(user_id_key)
            return user_id

        def abstract_session_token(request):
            session_token_header_key = 'HTTP_SESSION_TOKEN'
            print ("session token is : " + str(request.META.get(session_token_header_key)))
            return request.META.get(session_token_header_key)

        @wraps(f)
        def decorated_function(*args, **kwargs):
            request = args[1]
            if kwargs.get(user_id_key):
                user_id = kwargs[user_id_key]
                print ("user id from kwargs is :" + str(user_id))
                kwargs.pop(user_id_key)
            else:
                user_id = abstract_user_id(request)
                print ("user id from abstract user is :" + str(user_id))
            auth_data = {
                'user_id': int(user_id) if user_id else None,
                'session_token': abstract_session_token(request)
            }
            auth_serializer = AuthenticationSerializer(data=auth_data)
            auth_data['authorized'] = auth_serializer.is_valid(
            ) and auth_serializer.verify_and_update_session()
            return f(auth_data=auth_data, *args, **kwargs)
        return decorated_function
    return deco

def admin_session_authorize(admin_user_id_key='pk', *args, **kwargs):
    def deco(f):
        def abstract_user_id(request):
            if request.method == 'GET':
                admin_user_id = request.query_params.get(admin_user_id_key)[0]
            else:
                admin_user_id = request.data.get(admin_user_id_key)
            return admin_user_id

        def abstract_session_token(request):
            session_token_header_key = 'HTTP_SESSION_TOKEN'
            return request.META.get(session_token_header_key)

        @wraps(f)
        def decorated_function(*args, **kwargs):
            request = args[1]
            if kwargs.get(admin_user_id_key):
                admin_user_id = kwargs[admin_user_id_key]
                kwargs.pop(admin_user_id_key)
            else:
                admin_user_id = abstract_user_id(request)
            auth_data = {
                'admin_user_id': int(admin_user_id) if admin_user_id else None,
                'session_token': abstract_session_token(request)
            }
            auth_serializer = AdminAuthenticationSerializer(data=auth_data)
            auth_data['authorized'] = auth_serializer.is_valid(
            ) and auth_serializer.verify_and_update_session()
            return f(auth_data=auth_data, *args, **kwargs)
        return decorated_function
    return deco

def default_logger():
    logger = logging.getLogger("From the Decorator file")
    return logger


def format_error(message):
    return {
        "error": [
            message,
        ]
    }


def catch_exception(LOGGER=default_logger()):
    def deco(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                return f(*args, **kwargs)

            except NotAcceptableError as e:
                LOGGER.exception("NotAcceptableError:%s" % str(e))
                return MetaDataResponse(format_error(e.response),
                                        e.meta, status=e.status)
            except NotAllowedException as e:
                LOGGER.exception("NotAllowedException:%s" % str(e))
                return MetaDataResponse(format_error(e.response),
                                        e.meta, status=e.status)

            except NotFoundException as e:
                LOGGER.exception("NotFoundException:%s" % str(e))
                return MetaDataResponse(format_error(e.response),
                                        e.meta, status=e.status)

            except IntegrityError as e:
                LOGGER.exception("IntegrityError:%s" % str(e))
                return MetaDataResponse({}, str(e),
                                        status=status.HTTP_409_CONFLICT)
            except Exception as e:
                LOGGER.exception("Encountered Exception%s" % str(e))
                return MetaDataResponse(
                    {}, str(e),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return decorated_function
    return deco


def meta_data_response(meta=""):
    def deco(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            vanilla_response = f(*args, **kwargs)
            return MetaDataResponse(
                vanilla_response.data,
                meta, status=vanilla_response.status_code)
        return decorated_function
    return deco
