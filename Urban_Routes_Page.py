import data
from utility import retrieve_phone_code
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Paso 2
    taxi_button = (By.XPATH, "//button[text()='Pedir un taxi']")
    comfort_button = (By.XPATH, "(//div[text()='Comfort'])[1]")
    comfort_button_container = (By.XPATH, "//div[@class='tcard active']")
    # Paso 3
    phone_field_button = (By.XPATH, "//div[text()= 'Número de teléfono']")
    phone_box_field = (By.ID, 'phone')
    phone_box_button = (By.XPATH, "(//button[@type='submit'])[1]")
    code_field = (By.ID, 'code')
    code_confirm_button = (By.XPATH, "(//button[@type='submit'])[2]")
    # Paso 4
    payment_method = (By.XPATH, "(//div[text()='Método de pago'])[2]")  # metodo de pago
    add_payment_card = (By.XPATH, "//div[@class='pp-plus-container']//img[1]")  # caja de pago - agregar tarjeta
    credit_card_field = (By.ID, 'number')  # ingresar numero de tarjeta
    credit_card_code = (By.XPATH, "(//input[@id='code'])[2]")  # ingresar codigo de tarjeta
    confirm_credit_card_button = (By.XPATH, "//button[text()='Agregar']")  # ingresar datos de tarjeta
    payment_box_close = (By.XPATH, "(//button[@class='close-button section-close'])[3]")  # cerrar caja de pago
    payment_method_selected = (By.CLASS_NAME, 'pp-value-text')  # validación
    # Paso 5
    message_driver = (By.ID, 'comment')
    # Paso 6
    blankets_and_tissues_button = (By.XPATH, "(//span[@class='slider round'])[1]")
    blankets_and_tissues_checkbox = (By.CSS_SELECTOR, "div.r-sw-container input.switch-input")
    # Paso 7
    add_icecream_button = (By.XPATH, "(//div[@class='counter-plus'])[1]")
    # Paso 8
    final_taxi_button = (By.XPATH, "(//button[@type='button']//span)[1]")
    # Paso 9
    wait_driver_info = (By.XPATH, "(//div[@class='order-button'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self,address_from,address_to):
        self.driver.get(data.urban_routes_url)
        self.set_from(address_from)
        self.get_from()
        self.set_to(address_to)
        self.get_to()

    def click_taxi_button(self):
        self.driver.find_element(*self.taxi_button).click()

    def click_comfort_button(self):
        self.driver.find_element(*self.comfort_button).click()

    def click_phone_field_button(self):
        self.driver.find_element(*self.phone_field_button).click()

    def phone_number(self, phone_number):
        self.driver.find_element(*self.phone_box_field).send_keys(phone_number)

    def click_phone_box_button(self):
        self.driver.find_element(*self.phone_box_button).click()

    def verification_code(self):
        self.driver.find_element(*self.code_field).send_keys(retrieve_phone_code(self.driver))

    def click_confirm_button_in_verification_popup(self):
        self.driver.find_element(*self.code_confirm_button).click()

    def click_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_payment_card(self):
        self.driver.find_element(*self.add_payment_card).click()

    def set_card_number(self):
        self.driver.find_element(*self.credit_card_field).send_keys(data.card_number)

    def set_card_code(self):
        self.driver.find_element(*self.credit_card_code).send_keys(data.card_code)

    def press_tab_key(self):
        self.driver.find_element(*self.credit_card_code).send_keys(Keys.TAB)

    def click_confirm_credit_card_button(self):
        self.driver.find_element(*self.confirm_credit_card_button).click()

    def click_payment_box_close(self):
        self.driver.find_element(*self.payment_box_close).click()

    def set_message_driver(self):
        self.driver.find_element(*self.message_driver).send_keys(data.message_for_driver)

    def click_blankets_and_tissues_button(self):
        self.driver.find_element(*self.blankets_and_tissues_button).click()

    def get_blankets_and_tissues_button_state(self):
        checkbox = self.driver.find_element(*self.blankets_and_tissues_checkbox)
        return checkbox.is_selected()

    def click_add_icecream_button(self):
        add_icecream_buttons = self.driver.find_elements(*self.add_icecream_button)
        for button in add_icecream_buttons:
            button.click()
            button.click()

    def click_final_taxi_button(self):
        self.driver.find_element(*self.final_taxi_button).click()



