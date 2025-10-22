import requests
import pytest
from jsonschema import validate

BASE = "https://fakestoreapi.com"

PRODUCT_SCHEMA = {
    "type": "object",
    "required": ["id", "title", "price", "description", "category", "image", "rating"],
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "price": {"type": ["number", "integer"]},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "image": {"type": "string"},
        "rating": {
            "type": "object",
            "required": ["rate", "count"],
            "properties": {
                "rate": {"type": ["number", "integer"]},
                "count": {"type": "integer"}
            }
        }
    },
    "additionalProperties": True
}

EXPECTED_CATEGORIES = {
    "electronics",
    "jewelery",
    "men's clothing",
    "women's clothing"
}

REQUEST_TIMEOUT = 8  # segundos


def test_listar_todos_produtos():
    resp = requests.get(f"{BASE}/products", timeout=REQUEST_TIMEOUT)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0

    validate(instance=data[0], schema=PRODUCT_SCHEMA)


def test_buscar_produto_por_id():
    resp = requests.get(f"{BASE}/products/1", timeout=REQUEST_TIMEOUT)
    assert resp.status_code == 200
    prod = resp.json()
    validate(instance=prod, schema=PRODUCT_SCHEMA)
    assert prod["id"] == 1
    assert "title" in prod
    assert "price" in prod


def test_filtrar_por_categoria_parametrizado():
    # Endpoint: /products/category/{category}
    for cat in EXPECTED_CATEGORIES:
        resp = requests.get(f"{BASE}/products/category/{cat}", timeout=REQUEST_TIMEOUT)
        assert resp.status_code == 200, f"categoria {cat} retornou {resp.status_code}"
        items = resp.json()
        assert isinstance(items, list)
        for it in items:
            validate(instance=it, schema=PRODUCT_SCHEMA)
            assert it["category"].lower() == cat.lower()


def test_validar_schema_da_resposta():
    resp = requests.get(f"{BASE}/products", timeout=REQUEST_TIMEOUT)
    assert resp.status_code == 200
    items = resp.json()
    for it in items:
        validate(instance=it, schema=PRODUCT_SCHEMA)


@pytest.mark.parametrize("limit", [1, 3, 5, 10])
def test_limite_de_produtos_retornados(limit):
    resp = requests.get(f"{BASE}/products?limit={limit}", timeout=REQUEST_TIMEOUT)
    assert resp.status_code == 200
    items = resp.json()
    assert isinstance(items, list)
    assert len(items) <= limit
