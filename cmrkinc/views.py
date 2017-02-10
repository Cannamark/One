from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def send_email(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        subject = "Message from {}".format(name)
        message = data.get('message', '')
        from_email = data.get('email', '')
        if subject and message and from_email:
            try:
                send_mail(subject, """from:{} \ {}""".format(from_email, message), from_email, ['support@cmrkinc.com'])
                messages.success(request, 'Email Recieved!')
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/contact/')
        else:
            return HttpResponse('Make sure all fields are accurate and complete')
