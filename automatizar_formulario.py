from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import random
import time

# Crear una instancia de Faker y configurarla para generar nombres colombianos
fake = Faker('es_CO')

# Configurar las opciones para la pregunta "A que te dedicas"
ocupaciones = ['Empleado', 'Estudiante', 'Desempleado', 'Independiente']

# Configurar las opciones para la pregunta "Cual es tu promedio de ingresos"
ingresos = ['Menos del SMLV', 'Un SMLV', 'Entre 2 y 3 SMLV', 'Mas de 3 SMLV']

# Configurar las opciones para la pregunta "Tienes Vehiculo"
vehiculo = ['Sí', 'No']

preferencia = ['Moviles','Webs','Ambas']

compra = ['Chat de la aplicacion donde hice la compra','Mensajeria personal']

registro = ['Me registro con el boton y mi cuenta de Google','Lleno un formulario de registro']

criterio = ['Creo tener el criterio para hacerlo','Preferiria recibir asesoria']

informacion = ['Cantidad de baños', 'habitacion y area cuadrada',
'Parqueadero',
'Barrio',
'Direccion',
'Tipo de inmueble (Casa o apartamento)',
'Precio',
'Fotos del inmueble',
'Dueño del inmueble',
'Informacion de contacto del propietario',
'Todas las anteriores']

ideal = ['Si, puede ser util','Me es irrelevante']

# Configurar el enlace del formulario
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeEQyHMu03iu40eQMr3K2I6gbc7iMWlYEnTxwqRDy36y5epWg/viewform'

# Configurar el número de veces que se ejecutará el ciclo
num_iteraciones = 100

# Configurar el navegador Chrome (asegúrate de tener instalado el controlador de Chrome adecuado)
driver = webdriver.Chrome('C:/Users/David/Downloads/chromedriver.exe')

# Ciclo para ejecutar el código varias veces
for _ in range(num_iteraciones):
    # Abrir el formulario en el navegador
    driver.get(form_url)

    # Esperar a que se cargue el formulario completamente
    time.sleep(5)

    # Llenar el formulario con datos generados automáticamente
    driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i1"][aria-describedby="i2 i3"]').send_keys(fake.name())
    driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i5"][aria-describedby="i6 i7"]' ).send_keys(str(random.randint(19, 29)))

    # Seleccionar opciones para las preguntas restantes
    driver.find_element(By.CSS_SELECTOR, 'div[data-value="{}"]'.format(random.choice(ocupaciones))).click()
    driver.find_element(By.CSS_SELECTOR, 'div[data-value="{}"]'.format(random.choice(ingresos))).click()
    driver.find_element(By.CSS_SELECTOR, 'div[data-value="{}"]'.format(random.choice(vehiculo))).click()
    driver.find_element(By.CSS_SELECTOR, 'div[data-value="{}"]'.format(random.choice(preferencia))).click()
    driver.find_element(By.CSS_SELECTOR, 'div[data-value="{}"]'.format(random.choice(compra))).click()
    driver.find_element(By.CSS_SELECTOR, 'div[data-value="{}"]'.format(random.choice(registro))).click()
    driver.find_element(By.CSS_SELECTOR, 'div[data-value="{}"]'.format(random.choice(criterio))).click()
    driver.find_element(By.CSS_SELECTOR, 'div[data-value="{}"]'.format(random.choice(informacion))).click()
    driver.find_element(By.CSS_SELECTOR, 'div[data-value="{}"]'.format(random.choice(ideal))).click()

    # Selector CSS para el botón
    button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    # Esperar a que se envíe el formulario
    time.sleep(5)

# Cerrar el navegador después de terminar las iteraciones
driver.quit()