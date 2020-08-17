from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import Registration
from django.core.paginator import Paginator
from . import utils


# Create your views here.
def index(request):
	context = {}
	if(request.method == "POST"):
		form = Registration.UserInfoForm(request.POST)
		if(form.is_valid()):
			request.session['email'] = form.cleaned_data['email']
			form.save()
			return redirect('question')
	else:
		form = Registration.UserInfoForm()
	context['form'] = form
	return render(request,'UserInfo.html',context)

	

def question(request):
        if(request.session.get('email',False)):
                context = {}
                page_no = 0
                question_data = utils.get_question()
                paginator = Paginator(question_data,5) #This Line create pagination replace 5 with whatever question. You want to display
                if(request.method == "POST"):
                        all_answers = request.POST.getlist("Answer")
                        page_no = int(request.GET['page'])
                        res = utils.add_response_to_db((paginator.page(page_no).object_list),all_answers,request.session['email'])
                        if(paginator.page(page_no).has_next()):
                                page_no+=1
                                context['page_obj'] = paginator.page(page_no)
                        else:
                                result = utils.render_to_pdf("genPDF.html",request.session['email'])
                                del request.session['email']
                                if(result):
                                        return render(request,'thankyou.html')
                                else:
                                        return HttpResponse("<h1>Error</h1>")
                                
                else:
                        if(paginator.count):
                                page_no+=1
                                context['page_obj'] = paginator.page(page_no)
                        else:
                                return HttpResponse("<h1>Input Some Question</h1>")
                return render(request,"questions.html",context)
        else:
                return redirect("home")
