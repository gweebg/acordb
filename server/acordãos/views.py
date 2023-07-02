from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Account
from records.models import Record,ChangeRequest
from favorites.models import Favorites
from django.utils import timezone
from datetime import timedelta
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class Statistics(APIView):
    permission_classes=[permissions.AllowAny]
    @swagger_auto_schema(
        operation_description="Retrieves the global  statistics",
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "Processos": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "Processos24horas": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "Users": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "Administradores": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "Consumidores": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "RecordsMes": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_INTEGER),
                        ),
                    },
                ),
            ),
        },
    )
    def get(self,request):
        last_1_days = timezone.now() - timedelta(days=1)
        current_date = timezone.now()
        interval_start = current_date - timedelta(days=30)
        interval_end = current_date
        record_counts = []
        while interval_start > current_date - timedelta(days=90):
            count = Record.objects.filter(added_at__range=(interval_start, interval_end)).count()
            record_counts.append(count)
            interval_start -= timedelta(days=30)
            interval_end -= timedelta(days=30)
        return Response({
            "Processos":Record.objects.all().count(),
            "Processos24horas":Record.objects.filter(added_at__gte=last_1_days).count(),
            "Users":Account.objects.all().count(),
            "Administradores":Account.objects.filter(is_administrator=True).count(),
            "Consumidores":Account.objects.filter(is_administrator=False).count(),
            "RecordsMes":record_counts
            },status=status.HTTP_200_OK)