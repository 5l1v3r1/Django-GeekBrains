from django.shortcuts import redirect
from django.http import Http404

class AnonRequired:

    main_url = '/'

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect(self.main_url)

        return super(AnonRequired, self).dispatch(request, *args, **kwargs)

class StaffRequired:

    main_url= '/'

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_staff:
            raise Http404 

        return super(StaffRequired, self).dispatch(request, *args, **kwargs)
