# Formulario Automático

Este script en Python utiliza Selenium para llenar automáticamente un formulario web y enviarlo varias veces.

## Requisitos

- Python 3.x
- Selenium
- Faker

## Instalación

1. Clona este repositorio en tu máquina local:
  git clone https://github.com/tu_usuario/tu_repositorio.git
2. Navega hasta el directorio del proyecto:
  cd tu_repositorio
  
3. Instala las dependencias necesarias:
  pip install selenium faker
  
4. Descarga el controlador de Chrome adecuado para tu sistema operativo y colócalo en la ruta correcta. Puedes descargarlo desde [aquí](https://chromedriver.chromium.org/downloads).

## Uso

1. Abre el archivo `formulario_automatico.py` en un editor de texto.

2. Configura las opciones del formulario según tus necesidades. Puedes ajustar las listas de opciones para cada pregunta.

3. Cambia la variable `num_iteraciones` para establecer cuántas veces deseas que se envíe el formulario.

4. Ejecuta el script:
  python formulario_automatico.py
  
El script abrirá el formulario en el navegador y lo llenará automáticamente con datos generados aleatoriamente. Luego, enviará el formulario y esperará un tiempo antes de repetir el proceso según el número de iteraciones configuradas.

**Nota**: Asegúrate de tener el controlador de Chrome adecuado instalado y ubicado en la ruta especificada en el código.

## Contribución

Si encuentras algún error o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request. ¡Tu contribución es bienvenida!

## Licencia

Este proyecto está bajo la [MIT License](LICENSE).
