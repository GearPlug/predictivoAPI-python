class BaseError(Exception):
    pass


class BadRequest(BaseError):
    pass


class APIKeyMissing(BaseError):
    pass


class Forbidden(BaseError):
    pass


class ResourceNotFound(BaseError):
    pass


class MethodNotAllowed(BaseError):
    pass


class ResourceNestingTooDeep(BaseError):
    pass


class InvalidMethodOverride(BaseError):
    pass


class TooManyRequests(BaseError):
    pass


class InternalServerError(BaseError):
    pass


class ComplianceRelated(BaseError):
    pass


class UnexpectedError(BaseError):
    pass


class CredentialRequired(BaseError):
    pass


class InvalidToken(BaseError):
    pass
