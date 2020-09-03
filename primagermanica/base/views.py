# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class ArtistView(APIView):
    # serializer_class = serializers.HelloSerializer

    def get(self, request, artist):
        cache_qs = request.GET.get('cache')
        cache = not (cache_qs and cache_qs.lower() == 'false')

        best_10 = [
            'asdf1',
            'asdf2',
            'asdf3',
            'asdf4',
            'asdf5',
            'asdf6',
            'asdf7',
            'asdf8',
            'asdf9',
            'asdf10',
        ]
        return Response({'artist': artist, 'songs': best_10, 'cache': cache})
