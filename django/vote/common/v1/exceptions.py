from rest_framework import status


class ErrorMessage(Exception):

    def __init__(self, msg):
        self.value = msg

    def __str__(self):
        return repr(self.value)


class NotAllowedException(Exception):

    def __init__(self, meta="", response="", status=403):
        self.response = response
        self.status = status
        self.meta = meta
        super(Exception, self).__init__(
            meta + ". Status Code: " + str(status))

    def __str__(self):
        return ("Response: {response}, Meta: {meta}, Status: {status}".format(response=self.response, meta=self.meta, status=self.status))


class NotFoundException(Exception):

    def __init__(self, meta="", response="", status=404):
        self.response = response
        self.status = status
        self.meta = meta
        super(Exception, self).__init__(
            meta + ". Status Code: " + str(status))

    def __str__(self):
        return ("Response: {response}, Meta: {meta}, Status: {status}".format(response=self.response, meta=self.meta, status=self.status))


class NotAcceptableError(Exception):

    def __init__(self, meta="", response="", status=400):
        self.response = response
        self.status = status
        self.meta = meta
        super(Exception, self).__init__(
            meta + ". Status Code: " + str(status))

    def __str__(self):
        return ("Response: {response}, Meta: {meta}, Status: {status}".format(response=self.response, meta=self.meta, status=self.status))


class DBEntryError(Exception):

    def __init__(self, meta="", response="", status=500):
        self.response = response
        self.status = status
        self.meta = meta
        super(Exception, self).__init__(
            meta + ". Status Code: " + str(status))

    def __str__(self):
        return ("Response: {response}, Meta: {meta}, Status: {status}".format(response=self.response, meta=self.meta, status=self.status))


class ResponseException(Exception):

    def __init__(self, meta, response, status):
        self.response = response
        self.status = status
        self.meta = meta
        super(Exception, self).__init__(
            meta + ". Status Code: " + str(status))

    def __str__(self):
        return ("Response: {response}, Meta: {meta}, Status: {status}".format(response=self.response, meta=self.meta, status=self.status))


# class NotAcceptableError(ResponseException):

#     def __init__(self, param, param_value, response={}):
#         meta = '%s : %s Not Found' % (str(param), str(param_value))
#         super(NotAcceptableError, self).__init__(
#             meta, response, status.HTTP_406_NOT_ACCEPTABLE)


class ConflictError(ResponseException):

    def __init__(self, param, param_value, response={}):
        meta = '%s : %s Already Exists in Database' % (
            str(param), str(param_value))
        super(ConflictError, self).__init__(
            meta, response, status.HTTP_409_CONFLICT)
