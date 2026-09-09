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
    return render(request, "catalogo/lista.html", {"productos": productos})


def detalle(request, producto_id):
    productos = cargar_productos()
    producto = next((p for p in productos if p["id"] == producto_id), None)

    if producto is None:
        raise Http404("El producto solicitado no existe.")

    return render(request, "catalogo/detalle.html", {"producto": producto})