from account.models import Users
def absent_count():
  for user in Users:
    user.is_signin = False
    user.save()