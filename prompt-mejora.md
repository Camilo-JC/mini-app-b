## Rol
Actúa como desarrollador backend senior con experiencia en FastAPI, Jinja2 y pruebas con pytest.

## Objetivo
Agregar la funcionalidad de cantidad opcional a la mini-aplicación de trivia: GET /api/preguntas acepta el parámetro opcional cantidad (entre 1 y 5) y devuelve solo esa cantidad de preguntas. Sin el parámetro devuelve 5, y con un valor fuera del rango responde con el código 422. La página permite elegir cuántas preguntas se juegan. Además, agrega una prueba nueva en tests/test_mejora.py que compruebe esta mejora.

## Contexto
Lee AGENTS.md. El contrato de la API existente está en tests/test_aceptacion.py, el cual NO debe modificarse bajo ninguna circunstancia.

## Restricciones
- No modifiques ni rompas tests/test_aceptacion.py.
- Usa solo las dependencias de requirements.txt.
- La lógica debe residir en app/servicios.py y las rutas en app/main.py.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que vas a modificar o crear (incluyendo tests/test_mejora.py) y espera mi aprobación. Al terminar, resume brevemente qué hace cada archivo.

## Ejemplo
GET /api/preguntas?cantidad=2 devuelve una lista con solo 2 preguntas de trivia.
GET /api/preguntas?cantidad=10 responde con el código de estado 422.

## Criterio de éxito
python -m pytest -v pasa todas las pruebas (tanto las de aceptación como las nuevas de la mejora) y ruff check no reporta errores. Si después de 3 intentos las pruebas no pasan, detente y explica el problema.