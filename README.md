# README — Testes dos Exercícios

Este repositório contém os exercícios de testes automatizados. Cada exercício inclui:

* **Código dos testes** (dentro da pasta do exercício)
* **README.md** (este arquivo, no nível do repositório)
* **Relatório de execução (report)**
* **Log de execução (log.txt)**
---

## Estrutura do repositório

```
/exercicios
├── exercicio_01/
│   ├── tests/                # código dos testes
│   ├── report/               # pasta contendo o relatório
│   │   └── report_geral.html
│   ├── log.txt               # log de execução dos testes
│   └── README.md             # (opcional) instruções específicas
├── exercicio_02/
│   └── ...
└── README.md                 # este arquivo
```

> Observação: cada exercício tem sua própria pasta. O **log** fica no arquivo `log.txt` dentro da pasta de cada exercício. O **relatório (report)** fica em `report/report_geral.html` dentro da pasta do exercício.

---

## Requisitos

* Python 3.8+
* `pip` para instalar dependências

```bash
pip install -r requirements.txt
```

---

## Como executar os testes

1. Abra o terminal e vá até a pasta do exercício:

```bash
cd exercicios/exercicio_01
```

2. Execute os testes e gere logs e relatórios. Exemplo de comandos:

```bash
# Executa pytest e salva o log em log.txt
pytest -q > log.txt 2>&1

# Gera um relatório HTML (caso pytest-html esteja instalado)
pytest --html=report/report_geral.html --self-contained-html
```

---

## Localização dos logs e relatórios

* **Log de execução:** `exercicios/exercicio_N/log.txt`
* **Relatório (report):** `exercicios/exercicio_N/report/report_geral.html`

Cada pasta de exercício deve conter pelo menos um desses arquivos após a execução dos testes.

---

## Evidências (prints / logs)


* `log.txt` — log de execução
* `report/report_geral.html` — relatório completo