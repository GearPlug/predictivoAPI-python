from enum import Enum

class ErrorEnum(Enum):
    BadRequest=400
    APIKeyMissing=401
    Forbidden=403
    ResourceNotFound=404
    MethodNotAllowed=405
    ResourceNestingTooDeep=414
    InvalidMethodOverride=422
    TooManyRequests=429
    InternalServerError=500
    ComplianceRelated=503
