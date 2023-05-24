from rest_framework.exceptions import APIException

class NoProductException(APIException):
    status_code = 406
    default_detail = "No Products to be listed."

class NoNameProductException(APIException):
    status_code = 406
    default_detail = "No Product with such name."

class MissingContentException(APIException):
    status_code = 406
    default_detail = "The new Product is missing content."

class MissingDeletableProductException(APIException):
    status_code = 406
    default_detail = "The Product to be deleted is missing."

