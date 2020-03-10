#!/usr/bin/python
# -*- coding:utf-8 -*-

class CustomException(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class NotInitializedException(CustomException):
    def __init__(self, message = None):
        super().__init__(message)

    def __str__(self):
        return super().__str__()


class ApiException(CustomException):
    """Exception raised for REST API call errors.

    Attributes:
        statusCode -- HTTP status code
        message -- explanation of the error
    """

    def __init__(self, statusCode, message = None):
        super().__init__(message)
        self.statusCode = statusCode

    def __str__(self):
        if(self.message == None):
            return "StatusCode: '{0}'".format(self.statusCode)
        else:
            return "StatusCode: '{0}', '{1}'".format(self.statusCode, super().__str__())


class MissingConfigurationException(CustomException):
    def __init__(self, missingConfig, message = None):
        super().__init__(message)
        self.missingConfig = missingConfig

    def __str__(self):
        if(self.message == None):
            return "MissingConfig: '{0}'".format(self.missingConfig)
        else:
            return "MissingConfig: '{0}', '{1}'".format(self.missingConfig, super().__str__())
