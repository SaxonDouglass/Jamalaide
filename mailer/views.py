from django import forms

def send_mail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = EmailForm()
    
    c = {'form': form}
    c.update(csrf(request))
    
    return render_to_response('mailer/send_mail.html', c)
