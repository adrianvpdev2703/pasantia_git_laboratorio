from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para tareas.

    Endpoints:
        GET    /api/tasks/          → listar
        POST   /api/tasks/          → crear
        GET    /api/tasks/{id}/     → obtener una
        PUT    /api/tasks/{id}/     → actualizar completa
        PATCH  /api/tasks/{id}/     → actualizar parcial
        DELETE /api/tasks/{id}/     → eliminar
        POST   /api/tasks/{id}/toggle/  → alternar completado
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=["post"])
    def toggle(self, request, pk=None):
        task = self.get_object()
        task.completed = not task.completed
        task.save()
        return Response(self.get_serializer(task).data)

    @action(detail=False, methods=["delete"])
    def delete_completed(self, request):
        """Elimina todas las tareas completadas."""
        count, _ = Task.objects.filter(completed=True).delete()
        return Response(
            {"deleted": count}, status=status.HTTP_200_OK
        )
