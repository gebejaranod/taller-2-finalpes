# Taller 2: Predicción de abandono de clientes en FinAlpes

Curso MINE-4101 Ciencia de Datos Aplicada, Universidad de los Andes, 2026-20.

**Integrantes:** *(completar)*

FinAlpes quiere una herramienta que prediga qué clientes de un banco están en riesgo de irse, para ofrecerles una campaña de retención. El taller entrena y compara tres modelos con un dataset de clientes europeos, explica cómo decide el modelo elegido (Random Forest) y calcula cuánto le costaría y cuánto le ganaría a un banco de 20.000 clientes.

## Estructura

```
taller_2.ipynb               Notebook con las actividades 1 a 5
presentacion_ejecutiva.html  Presentación corta con los hallazgos y la recomendación (actividad 6)
declaracion_ia.md            Declaración de uso de IA generativa (actividad 7)
datos/churn.csv              Dataset entregado con el enunciado
crear_sqlite.py              Opcional: copia el dataset a SQLite para explorarlo en Metabase
requirements.txt             Versiones exactas de las librerías
```

## Dónde está cada entregable

| Actividad | Peso | Dónde está |
|---|---|---|
| 1. Entendimiento y preparación de los datos | 10 % | Notebook, sección 1 |
| 2. Entrenamiento del modelo | 15 % | Notebook, sección 2 |
| 3. Análisis cuantitativo de resultados | 20 % | Notebook, sección 3 |
| 4. Análisis cualitativo de resultados | 20 % | Notebook, sección 4 |
| 5. Generación de valor | 20 % | Notebook, sección 5 |
| 6. Insights | 10 % | [`presentacion_ejecutiva.html`](presentacion_ejecutiva.html). Se abre en el navegador y se avanza con las flechas del teclado o con clic |
| 7. Declaración de uso de IA generativa | 5 % | [`declaracion_ia.md`](declaracion_ia.md) |

## Cómo ejecutarlo

Se necesita Python 3.12. Desde la raíz del repositorio:

```bash
python -m venv venv
```

```bash
venv/Scripts/python.exe -m pip install -r requirements.txt
```

En Linux o Mac la ruta es `venv/bin/python`.

Hay un solo notebook, `taller_2.ipynb`. Se abre con el kernel del entorno y se ejecuta de arriba abajo; tarda unos minutos por la búsqueda de hiperparámetros y el cálculo de SHAP. También se puede ejecutar desde la terminal:

```bash
venv/Scripts/python.exe -m jupyter nbconvert --to notebook --execute --inplace taller_2.ipynb
```

El notebook solo necesita `datos/churn.csv`, que ya está en el repositorio. Al ejecutarse, guarda los datos limpios en `datos/churn.sqlite` (tabla `churn_limpio`).

## Uso de IA generativa

Ver [`declaracion_ia.md`](declaracion_ia.md).
