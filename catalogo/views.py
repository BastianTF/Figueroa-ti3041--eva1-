import json
from pathlib import Path

from django.http import Http404
from django.shortcuts import render

DATA_PATH = Path(__file__).resolve().parent / "data" / "productos.json"


def cargar_productos():
    with open(DATA_PATH, encoding="utf-8") as archivo:
        return json.load(archivo)


def lista(request):
    productos = cargar_productos()
    total_productos = len(productos)
    total_con_stock = sum(1 for p in productos if p["stock"] > 0)

    contexto = {
        "productos": productos,
        "total_productos": total_productos,
        "total_con_stock": total_con_stock,
        "total_sin_stock": total_productos - total_con_stock,
    }
    return render(request, "catalogo/lista.html", contexto)


def detalle(request, producto_id):
    productos = cargar_productos()
    producto = next((p for p in productos if p["id"] == producto_id), None)

    if producto is None:
        raise Http404("El producto solicitado no existe.")

    return render(request, "catalogo/detalle.html", {"producto": producto})