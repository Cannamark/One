from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def send_email(request):
    import pdb; pdb.set_trace()
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        subject = "Message from {}".format(name)
        message = data.get('message', '')
        from_email = data.get('email', '')
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['support@smrkinc.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/contact/')
        else:
            return HttpResponse('Make sure all fields are accurate and complete')
