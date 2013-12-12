from mailer.models import *

def compose(request, mail_id=None):
    if mail_id:
        mail = get_object_or_404(Mail, id=mail_id)
    else:
        mail = Mail()

    if request.method == 'POST':
        form = MailForm(request.POST, instance=mail)
    else:
        form = MailForm(instance=mail);

    c = {
        'form':form,
    }
    c.update(csrf(request))
    return render_to_response('mailer/index.html', c,
                              context_instance=RequestContext(request))
