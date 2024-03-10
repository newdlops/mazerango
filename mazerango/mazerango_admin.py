from django.contrib import admin
from functools import update_wrapper
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse
from django.urls import path, re_path

csrf_protect_m = method_decorator(csrf_protect)


class ModelAdmin(admin.ModelAdmin):
    # Admin에 추가할 URL과 뷰 함수 매핑
    def get_urls(self):
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        info = self.opts.app_label, self.opts.model_name
        urls = super().get_urls()
        my_urls = [
            path("ajax/", wrap(self.ajax_data_view), name="%s_%s_changelist" % info),
        ]
        return my_urls + urls

    def ajax_data_view(self, request):
        """
        The 'change list' admin view for this model.
        """

        import json
        query = request.GET.copy()
        self.list_per_page = int(query["len"])

        if 'len' in query:
            del query["len"]
        del query["_"]

        request.GET = query

        context = super().changelist_view(request).context_data
        results = context['cl'].result_list
        json_results = list(results.values(*self.list_display))
        return HttpResponse(json.dumps({'recordsTotal': context['cl'].result_count,'recordsFiltered': context['cl'].result_count, 'data': json_results}))
