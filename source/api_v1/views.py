from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import QuoteSerializer
from webapp.models import Quote, QUOTE_APPROVED


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.none()
    serializer_class = QuoteSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Quote.objects.all()
        return Quote.objects.filter(status=QUOTE_APPROVED)

    # доступ к изменению и удалению цитат
    # только для вошедших пользователей
    # ...
