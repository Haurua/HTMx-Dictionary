from django.shortcuts import render
from django.views.generic import View
from .functions.dict_api_request import dict_api_request


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'htmx_dictionary/index.html')

    def post(self, request, *args, **kwargs):
        search_word = request.POST["search"]
        response = dict_api_request(search_word)
        if response.status_code == 200:
            context = {
                "result": response.json()
            }
            return render(request, 'htmx_dictionary/search_results.html', context)
        else:
            context = {
                "search": search_word
            }
            return render(request, 'htmx_dictionary/not_found.html', context)
