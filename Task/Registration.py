from django import forms
from . import models


class UserInfoForm(forms.ModelForm):
	"""docstring for User"""

	class  Meta(object):
		"""docstring for  Meta"""
		model = models.UserInfo
		fields = '__all__'
