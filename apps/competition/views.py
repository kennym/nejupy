from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    redirect,
    render_to_response,
)


@login_required
def index(request):
    user = request.user
    if user.is_superuser:
        return redirect('/admin')
    else:
        return render_to_response("competition/index.html")

