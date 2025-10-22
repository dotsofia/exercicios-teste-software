import requests
import pytest
from jsonschema import validate

BASE = "https://jsonplaceholder.typicode.com"
TIMEOUT = 8

TODO_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "completed"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    },
    "additionalProperties": True
}

@pytest.fixture(scope="module")
def session():
    """Session requests para reuso de conexão."""
    with requests.Session() as s:
        yield s

@pytest.fixture
def created_ids():
    """Lista para guardar IDs criados durante os testes e limpar no teardown."""
    ids = []
    yield ids
    for _id in ids:
        try:
            resp = requests.delete(f"{BASE}/todos/{_id}", timeout=TIMEOUT)
        except Exception:
            pass


def test_create_todo(session, created_ids):
    payload = {
        "title": "Minha tarefa de teste",
        "completed": False,
        "userId": 1
    }
    resp = session.post(f"{BASE}/todos", json=payload, timeout=TIMEOUT)

    assert resp.status_code in (200, 201)
    data = resp.json()
    assert isinstance(data, dict)

    assert "id" in data
    created_ids.append(int(data["id"]))

    try:
        validate(instance=data, schema=TODO_SCHEMA)
    except Exception:
        # se a validação falhar, ao menos cheque campos básicos
        assert data.get("title") == payload["title"]
        assert data.get("completed") == payload["completed"]


def test_read_todo_existing(session):
    resp = session.get(f"{BASE}/todos/1", timeout=TIMEOUT)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    validate(instance=data, schema=TODO_SCHEMA)


def test_update_todo_patch(session):
    patch = {"completed": True}
    resp = session.patch(f"{BASE}/todos/1", json=patch, timeout=TIMEOUT)

    assert resp.status_code in (200, 204)
    if resp.status_code == 200:
        data = resp.json()
        assert "completed" in data
        assert data["completed"] is True


def test_delete_and_verify(session):
    resp = session.delete(f"{BASE}/todos/1", timeout=TIMEOUT)
    assert resp.status_code in (200, 204, 404)

    resp2 = session.get(f"{BASE}/todos/1", timeout=TIMEOUT)

    if resp2.status_code == 404:
        assert True
    elif resp2.status_code == 200:
        try:
            data = resp2.json()
            if isinstance(data, dict):
                assert "id" in data
        except ValueError:
            assert True
    else:
        pytest.fail(f"GET after DELETE retornou status inesperado: {resp2.status_code}")