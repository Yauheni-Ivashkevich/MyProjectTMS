# from os import urandom
# from typing import Dict
# from typing import Optional
#
# from django.contrib.auth import get_user_model
# from django.test import Client
# from rest_framework import status
#
# from apps.authorization.models import AuthProfile
# from apps.authorization.models import Profile
# from project.utils.date import utcnow
#
# User = get_user_model()
#
#
# class UserTestMixin:
#     def create_user(
#             self,
#             placeholder: Optional[str] = None,
#             user_kw: Optional[Dict] = None,
#             verified=False,
#     ) -> User:
#         placeholder = placeholder or urandom(4).hex()
#         form_data = {
#             "username": f"{placeholder}",
#             "email": f"email_{placeholder}@test.com",
#             "password": placeholder,
#         }
#
#         user_kw = (user_kw or {}).copy()
#         user_kw.update(form_data)
#
#         user = User.objects.create_user(**user_kw)
#         user.save()
#
#         if verified:
#             self.create_auth_profile(user)
#
#         self.create_profile(user)
#
#         return user
#
#     @staticmethod
#     def create_auth_profile(user: User) -> AuthProfile:
#         auth = AuthProfile(
#             user=user, verification_code=user.username, verified_at=utcnow(),
#         )
#         auth.save()
#
#         return auth
#
#     @staticmethod
#     def create_profile(user) -> Profile:
#         profile = Profile(user=user, name=f"name_{user.username}")
#         profile.save()
#         return profile
#
#     def create_auth_token(self, user, client: Optional[Client] = None) -> str:
#         cli = client or self.client
#
#         credentials = {"username": user.username, "password": user.username}
#
#         resp = cli.post("/api/obtain_auth_token/", credentials)
#         self.assertEqual(status.HTTP_200_OK, resp.status_code)
#
#         payload = resp.json()
#         self.assertEqual(1, len(payload))
#         self.assertIsInstance(payload, dict)
#         self.assertIn("token", payload)
#
#         token = payload["token"]
#         self.assertTrue(token)
#
#         return token