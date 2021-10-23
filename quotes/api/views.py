from rest_framework import generics, pagination
from rest_framework import permissions

from quotes.models          import Quote
from quotes.api.pagination  import SmallSetPagination
from quotes.api.serializers import QuoteSerializer
from quotes.api.permissions import IsAdminUserOrReadOnly


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset         = Quote.objects.all()
    serializer_class = QuoteSerializer
    permissions      = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination