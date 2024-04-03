
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from framework.webapp import WebApp
from data.config import settings



def before_scenario(context, scenario):
    # URL del hub remoto de Selenium Grid
    grid_url = 'http://localhost:4444/wd/hub'

    # Configurar opciones del navegador
    if settings['browser'] == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        driver = webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities=DesiredCapabilities.CHROME.copy(),
            options=options
        )
    elif settings['browser'] == 'firefox':
        driver = webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
        )
    else:
        # Navegador por defecto
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        driver = webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities=DesiredCapabilities.CHROME.copy(),
            options=options
        )

    # Aumentar el tiempo de espera para los comandos
    driver.implicitly_wait(10)  # Tiempo de espera implícito de 10 segundos
    driver.set_script_timeout(30)  # Tiempo de espera para ejecutar scripts de 30 segundos

    print(f"Valor de context.evidence_path: {context.evidence_path}")
    # Inicializar la aplicación web
    context.driver = driver
    context.app = WebApp(context.driver)



def after_scenario(context, scenario):
    # Imprimir mensaje de depuración
    print("Executing after_all()")

    # Verificar si context.driver está definido
    if hasattr(context, 'driver'):
        # Cerrar el navegador al finalizar
        context.driver.quit()
    else:
        # Imprimir mensaje de error si context.driver no está definido
        print("Error: context.driver is not defined")
        print(context.driver.get_log('browser'))
