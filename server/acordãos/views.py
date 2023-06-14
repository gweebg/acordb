from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Account
from records.models import Record,ChangeRequest
from favorites.models import Favorites
from django.utils import timezone
from datetime import timedelta



class Statistics(APIView):
    permission_classes=[permissions.AllowAny]
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