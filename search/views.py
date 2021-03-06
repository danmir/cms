# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage

def search(request):
    query = request.GET.get('q', '')
    results = []
    keyword_results = []
    if query:
        #the keyword field on the related SearchKeyword model
        keyword_results = FlatPage.objects.filter(searchkeyord__keyword__in = query.split()).distinct()
        results = FlatPage.objects.filter(content__icontains=query)
    #template = get_template('search/search.html')
    #context = Context({'query': query, 'results': results})
    #response = template.render(context)
    #return HttpResponse(response)
    return render_to_response('search/search.html', {'query': query,
                                                     'results': results,
                                                     'keyword_results': keyword_results})