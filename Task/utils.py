from . import models
from django.shortcuts import get_object_or_404
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import EmailMessage
from django.conf import settings


def get_question():
	data = models.Question.objects.all()
	return data

def get_user_data(email=None):
	data = get_object_or_404(models.UserInfo,email=email)
	return data


def get_user_response(email=None):
	user_info = get_user_data(email)
	user_response = models.UserResponse.objects.filter(user=user_info)
	return user_response


def add_response_to_db(question=None,answer=None,email=None):
	user_data = get_user_data(email)
	for resp in zip(question,answer):
		user_response_model,created = models.UserResponse.objects.get_or_create(user=user_data,question=resp[0],answer=resp[1])
		user_response_model.save()


def send_pdf_to_mail(pdf):
        try:
                email = EmailMessage('Report','User Response',settings.EMAIL_HOST_USER,['vs0032532@gmail.com'])
                email.attach('response.pdf', pdf.getvalue() , 'application/pdf')
                email.send()
                return True
        except Exception as e:
                print(str(e))
                return False

def render_to_pdf(template_src="genPDF.html",email=None):
        user_data = get_user_data(email)
        user_response = get_user_response(email)
        context_dict = {
                'user_data':user_data,
                'user_response_data':user_response,
                }
        template = get_template(template_src)
        html  = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
        if not pdf.err:
                return send_pdf_to_mail(result)
        return None
