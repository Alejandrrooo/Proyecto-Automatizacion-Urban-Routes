import time
import data
import pytest
from selenium import webdriver
from Urban_Routes_Page import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None
    initial_header = None
    final_header = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome() #desired_capabilities=capabilities
        cls.driver.implicitly_wait(15)

    #Prueba 1: Configurar la dirección
    @pytest.mark.sleep(8)
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    #Prueba 2: Seleccionar la tarifa Comfort
    @pytest.mark.sleep(5)
    def test_request_comfort_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_button()
        routes_page.click_comfort_button()
        assert self.driver.find_element(*routes_page.comfort_button_container).get_attribute('class') == 'tcard active'

    # Prueba 3: Rellenar y verificar el número de teléfono
    @pytest.mark.sleep(10)
    def test_fill_and_verification_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_field_button()
        routes_page.phone_number(data.phone_number)
        routes_page.click_phone_box_button()
        routes_page.verification_code()
        routes_page.click_confirm_button_in_verification_popup()
        assert self.driver.find_element(*routes_page.phone_box_field).get_property('value') == data.phone_number

    #Pruebas 4: Agregar una tarjeta de credito
    @pytest.mark.sleep(10)
    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        routes_page.click_add_payment_card()
        routes_page.set_card_number()
        routes_page.set_card_code()
        routes_page.press_tab_key()
        routes_page.click_confirm_credit_card_button()
        routes_page.click_payment_box_close()
        assert self.driver.find_element(*routes_page.payment_method_selected).text == 'Tarjeta'

    #Prueba 5: Escribir un mensaje para el controlador
    @pytest.mark.sleep(5)
    def test_message_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_driver()
        assert routes_page.driver.find_element(*routes_page.message_driver).get_property('value') == data.message_for_driver

    #Prueba 6: Pedir una manta y pañuelos
    def test_click_blankets_and_tissues_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        initial_state = routes_page.get_blankets_and_tissues_button_state()
        routes_page.click_blankets_and_tissues_button()
        final_state = routes_page.get_blankets_and_tissues_button_state()
        assert initial_state != final_state, "El estado del botón no cambió."

    #Prueba 7: Pedir 2 helados
    @pytest.mark.sleep(5)
    def test_add_icecream_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_icecream_button()
        assert routes_page.driver.find_element(*routes_page.add_icecream_button).is_selected()

    #Prueba 8: Aparece el modal para buscar un taxi
    @pytest.mark.sleep(5)
    def test_final_taxi_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_final_taxi_button()

    #Prueba 9: Esperar a que aparezca la información del conductor en el modal
    def test_wait_driver_info(self):
        # Espera 60 segundos antes de realizar la verificación
        time.sleep(60)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
