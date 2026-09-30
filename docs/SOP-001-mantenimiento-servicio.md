# SOP-001: Mantenimiento y Reinicio del Backend de Tareas

## 1. Alcance
Procedimiento estándar para la intervención del servicio API Tasks ante degradación operativa.

## 2. Diagnóstico
Verificar el estado del proceso en el sistema:
```bash
systemctl is-active todo-backend
```

## 3. Accion en Mantenimiento

```bash
curl -f -s http://localhost:8000/api/tasks/ > /dev/null || echo "ALERTA: Endpoint no disponible"
```



