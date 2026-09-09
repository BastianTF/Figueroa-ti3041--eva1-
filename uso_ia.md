# Uso de IA y entrega final

## Proyecto
Ferretería El Tornillo

## Objetivo
Desarrollar una pequeña aplicación web con Django para mostrar un catálogo de productos, con listado, detalle, resumen de stock y una interfaz visual simple.

## ¿Qué se hizo?
- Se creó la estructura base de la app `catalogo`.
- Se configuró la lógica para cargar productos desde un archivo JSON.
- Se implementó la vista `lista` con resumen de productos totales, con stock y sin stock.
- Se implementó la vista `detalle` para mostrar cada producto individualmente.
- Se generaron los templates base y de listado.
- Se añadieron estilos para mejorar la presentación visual.
- Se configuró el enrutado de la app y la estructura de archivos estáticos.

## Herramientas y asistente
Se utilizó un asistente de IA para apoyar en:
- la creación de archivos y estructura del proyecto,
- la sugerencia y corrección de código Python y templates Django,
- la resolución de errores de entorno y de activación del virtualenv,
- la preparación de plantillas HTML y CSS para la interfaz.

## Verificación realizada
Se comprobó que el proyecto compila sin errores de sintaxis con:

```powershell
.\venv\Scripts\python.exe -m compileall .\catalogo
```

Resultado verificado: `COMPILE_OK`.

## Cómo ejecutar el proyecto
1. Abrir PowerShell en la raíz del proyecto.
2. Activar el entorno virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Ejecutar el servidor Django:

```powershell
python manage.py runserver
```

4. Abrir la URL que muestre Django en el navegador, normalmente:

```text
http://127.0.0.1:8000/
```

## Consideraciones finales
El proyecto cumple con la etapa de catálogo y visualización básica de productos. El siguiente paso opcional sería completar la configuración del proyecto principal de Django para que la app se registre correctamente y se pueda acceder desde la raíz del sitio.
