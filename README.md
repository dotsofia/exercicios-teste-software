# Exercícios — Teste de Software

Este repositório contém 5 exercícios práticos de testes de software (Web e REST).

Cada exercício deve conter:
- Código dos testes (`tests/`)
- Um `README.md` com instruções de execução
- Um relatório de execução (HTML ou texto)
- Um print ou log mostrando os testes passando

---

## Configuração inicial (Windows)

1. Crie e ative o ambiente virtual:
```cmd
python -m venv .venv
venv\Scripts\activate
```

2. Atualize ferramentas básicas e instale as dependências:

```cmd
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Rodar Exercicio
pytest tests/

pytest -q --self-contained-html --html=reports/relatorio_geral.html
