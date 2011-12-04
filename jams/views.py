from jams.models import Jam

from django.shortcuts import render_to_response, get_list_or_404

def index(request):
    jams = get_list_or_404(Jam, )
    return render_to_response('jams/index.html', {'jams': jams})

