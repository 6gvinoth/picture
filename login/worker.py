from .models import *
from django.contrib.auth.hashers import make_password

def user_validate_db(username,password):
	# encrypt_pass=make_password(password)
	fetch_user_details=User.objects.filter(user_name=username)
	if fetch_user_details.count()==0:
		return [False,'INVALID_USER_AUTHENTICATION']
	else:
		db_pass=fetch_user_details[0].password
		if db_pass == password:
			return [True,None]
		else:
			return [False,'INVALID_USER_AUTHENTICATION']
def user_create(username,password):
	fetch_user_details=User.objects.filter(user_name=username)
	if fetch_user_details.count()==0:
		user_obj=User()
		user_obj.user_name=username
		user_obj.password=password
		result=user_obj.save()
		return [True,None]
	else:
		return [False,'User Exists']

	
