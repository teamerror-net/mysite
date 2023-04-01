from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, username, password, **other_fields):
        user = self.model(username = username, **other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, password, **other_fields):
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        return self.create_user(username, password, **other_fields)