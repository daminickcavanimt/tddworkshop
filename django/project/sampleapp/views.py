from django.views.generic import View
from django.http import HttpResponse
from sampleapp.named_entity import NamedEntityClient
import spacy
import json
# Create your views here.
class GetNamedEnts(View):
    def post(self, request):
        ner = spacy.load('en_core_web_sm')
        client = NamedEntityClient(ner)
        result = client.get(ents(request.POST['sentence']))
        response = {'entities': result.get('ents')}
        return HttpResponse(json.dumps(response))