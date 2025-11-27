## Comandos

#### Ejecuta todos los test
```sh
python -m pytest -v
```

#### Coverage por terminal

```sh
python -m pytest --cov=src tests/ --cov-report=term-missing
```

#### Coverage con reporte HTML

```sh
python -m pytest --cov=src tests/ --cov-report=html
```