import requests

from predictivo_api import exception
from predictivo_api.enumerator import ErrorEnum


class Client(object):
    def __init__(self, host=None, access_token=None):
        if access_token and host:
            self.access_token = access_token
            self.base_url = host[:-1] if host[:-1] == '/' else host
        else:
            raise exception.CredentialRequired("You must provide either access_token and hostname")

    def _get(self, endpoint):
        response = requests.get(self.base_url + endpoint)
        return self._parse(response).json()

    def _post(self, endpoint, data):
        response = requests.post(self.base_url + endpoint, json=data)
        return self._parse(response).json()

    def _parse(self, response):
        if not response.ok:
            data = response.json()
            if 'detail' in data and 'status' in data:
                code = data['status']
                message = data['detail']
                try:
                    error_enum = ErrorEnum(code)
                except Exception:
                    raise exception.UnexpectedError('Error: {}. Message {}'.format(code, message))
                if error_enum == ErrorEnum.BadRequest:
                    raise exception.BadRequest(message)
                if error_enum == ErrorEnum.APIKeyMissing:
                    raise exception.APIKeyMissing(message)
                if error_enum == ErrorEnum.Forbidden:
                    raise exception.Forbidden(message)
                if error_enum == ErrorEnum.ResourceNotFound:
                    raise exception.ResourceNotFound(message)
                if error_enum == ErrorEnum.MethodNotAllowed:
                    raise exception.MethodNotAllowed(message)
                if error_enum == ErrorEnum.ResourceNestingTooDeep:
                    raise exception.ResourceNestingTooDeep(message)
                if error_enum == ErrorEnum.InvalidMethodOverride:
                    raise exception.InvalidMethodOverride(message)
                if error_enum == ErrorEnum.TooManyRequests:
                    raise exception.TooManyRequests(message)
                if error_enum == ErrorEnum.InternalServerError:
                    raise exception.InternalServerError(message)
                if error_enum == ErrorEnum.ComplianceRelated:
                    raise exception.ComplianceRelated(message)
                else:
                    raise exception.BaseError('Error: {}. Message {}'.format(code, message))
            return data
        else:
            return response

    def _request(self, method, endpoint, params=None, data=None):
        headers = {
            'Authorization': 'Basic {}'.format(self.creds),
            'Content-Type': 'application/json'
        }
        try:
            url = self.base_url + endpoint
            response = requests.request(method=method, url=url, params=params, data=data, headers=headers)
            return self._parse(response)
        except Exception as e:
            print("Error while request: ", e)
            return False

    def describe_sugarcontacts(self):
        endpoint = '/sugarcontacts/describe'
        return self._request('GET', endpoint)

    def describe_agenda(self):
        endpoint = '/agenda/describe'
        return self._request('GET', endpoint)

    def create_agenda(self, id_call, status, date_start, date_exec, assigned_user_id, parent_id, parent_type,
                      first_name,
                      last_name, phone, prioridad_c):
        endpoint = '/agenda/crearAgenda'
        body = {
            "idcall": id_call,
            "status": status,
            "date_start": date_start,
            "date_exec": date_exec,
            "assigned_user_id": assigned_user_id,
            "parent_id": parent_id,
            "Parent_type": parent_type,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "prioridad_c": prioridad_c
        }
        return self._request('POST', endpoint, body)

    def create_contact(self, _id, status, date_entered, date_modified, first_name, last_name, phone_mobile, limpio,
                       id_tipo, ejecutada, intentos, assigned_user_id, id_call, tipo_contac):
        endpoint = '/contacto/crearContacto'
        body = {
            "id": _id,
            "status": status,
            "date_entered": date_entered,
            "date_modified": date_modified,
            "first_name": first_name,
            "last_name": last_name,
            "phone_mobile": phone_mobile,
            "Limpio": limpio,
            "Ejecutada": ejecutada,
            "IdTipo": id_tipo,
            "Intentos": intentos,
            "assigned_user_id": assigned_user_id,
            "idcall": id_call,
            "TipoContac": tipo_contac
        }
        return self._request('POST', endpoint, body)
