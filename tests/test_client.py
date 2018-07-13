# import os
# from unittest import TestCase
# from predictivo_api.client import Client, ClientOauth
#
# class MailchimpTestCases(TestCase):
#     def setUp(self):
#         self.access_token=os.environ.get('token')
#         self.user=os.environ.get('user')
#         self.apikey=os.environ.get('apikey')
#
#         self.client=Client(access_token=self.access_token)
#
#     def test_get_lists(self):
#         response = self.client.get_lists()
#         self.assertIn('lists', response)
#
#     def test_get_list(self):
#         list= self.client.create_new_list(self._get_data_list())
#         response= self.client.get_list(list['id'])
#         self.client.remove_lists(list['id'])
#         self.assertIn('_links', response)
#
#     def _get_data_list(self):
#         data = {
#             "name": "My_list",
#             "contact":
#                 {
#                     "company": "my_company",
#                     "address1": "address",
#                     "city": "Bogotá",
#                     "state": "Cundinamarca",
#                     "zip": "11000",
#                     "country": "Colombia"
#                 },
#             "permission_reminder": "permission",
#             "campaign_defaults":
#                 {
#                     "from_name": "my_company",
#                     "from_email": "my_company@grplug.com",
#                     "subject": "list campaing",
#                     "language": "english"
#                 },
#             "email_type_option": True
#         }
#         return data
#
#     def _get_member(self):
#         data={
#             "email_address":"member50@gmail.com",
#             "status": "subscribed"
#         }
#         return data
#
#     def test_create_new_list(self):
#         data=self._get_data_list()
#         response = self.client.create_new_list(data)
#         name=response['name']
#         self.client.remove_lists(response['id'])
#         self.assertEqual(name, data['name'])
#
#     def test_remove_lists(self):
#         data=self._get_data_list()
#         list = self.client.create_new_list(data)
#         response = self.client.remove_lists(list['id'])
#         self.assertEqual(response.status_code, 204)
#
#     def test_get_list_members(self):
#         lists=self.client.create_new_list(self._get_data_list())
#         response = self.client.get_list_members(lists['id'])
#         self.client.remove_lists(lists['id'])
#         self.assertIn('_links', response)
#
#     def test_add_new_list_member(self):
#         list = self.client.create_new_list(self._get_data_list())
#         response=self.client.add_new_list_member(list['id'], self._get_member())
#         email=response['email_address']
#         self.client.remove_list_member(list['id'],email)
#         self.client.remove_lists(list['id'])
#         self.assertEqual(email,self._get_member()['email_address'])
#
#     def test_remove_list_member(self):
#         list = self.client.create_new_list(self._get_data_list())
#         member=self.client.add_new_list_member(list['id'], self._get_member())
#         response= self.client.remove_list_member(list['id'], member['email_address'])
#         self.assertEqual(response.status_code, 204)
#
#
#
#

import json
d = {
     'id': '3344',
     'status': 'New',
     'date_entered': '2018-07-04 14:26:37',
     'date_modified': '2018-07-04 10:26:37',
     'first_name': 'Joslito',
     'last_name': 'Carnaval',
     'phone_mobile': '3019987862',
     'Limpio': 'Si',
     'Ejecutada': '1',
     'IdTipo': '2',
     'Intentos': '4',
     'assigned_user_id': '456789-dfghjkl-45678i9',
     'idcall': 'dfghjkjh-98765',
     'TipoContac': '1',
     }
print(json.dumps(d))