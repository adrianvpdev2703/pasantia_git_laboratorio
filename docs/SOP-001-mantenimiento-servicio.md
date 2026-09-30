# SOP-001: Mantenimiento y Reinicio del Backend de Tareas

## 1. Alcance
Procedimiento estándar para la intervención del servicio API Tasks ante degradación operativa.

## 2. Diagnóstico
Verificar el estado del proceso en el sistema:
```bash
systemctl is-active todo-backend

## 3. Accion de Mantenimiento
```bash
sudo systemctl restart todo-backend
sudo systemctl status todo-backend --no-pager