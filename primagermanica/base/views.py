# Create your views here.
import requests
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

from primagermanica.base.models import Transaction


class ArtistView(APIView):

    def get(self, request):
        cache_qs = request.GET.get('cache')
        name_qs = request.GET.get('q')
        if cache_qs and cache_qs.lower() == 'false':
            payload = search_songs(name_qs)
            return Response(payload)

        payload = cache.get(name_qs)
        if not payload:
            payload = search_songs(name_qs)
            cache.set(name_qs, payload)

        return Response(payload)


# todo treat the status code, can't just pass the same.
def search_songs(name: str):
    # todo extract to .env
    ACCESS_TOKEN = 'C4j5H3PjWLdZmwtj1caAIFjcAj_IXpUlwOJyo9ZI9GW9P_KGaetVnlwCkuqszLMq'
    r = requests.get('https://api.genius.com/search', params={'q': name},
                     headers={'Authorization': f'Bearer {ACCESS_TOKEN}'})
    t = Transaction(name)
    t.save()
    return r.json()
