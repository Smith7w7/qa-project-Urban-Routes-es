import time

from helpers import retrieve_phone_code

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.from_field))

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

class TariffPage:
    button_order_taxi = (By.CLASS_NAME, 'button.round')

    def __init__(self, driver):
        self.driver = driver

    # Espera a que aparezca el boton
    def wait_for_button_order_taxi(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.button_order_taxi))

    def click_button_order_taxi(self):
        self.driver.find_element(*self.button_order_taxi).click()

    def get_button_order_taxi_name(self):
        return self.driver.find_element(*self.button_order_taxi).get_attribute("textContent")

    def select_tariff(self):
        self.wait_for_button_order_taxi()
        self.click_button_order_taxi()
        self.get_button_order_taxi_name()

class OrderFormPage:

    tariff_card = (By.CLASS_NAME, 'tariff-cards')
    car_list = (By.CLASS_NAME, 'tcard')
    message_field = (By.ID, 'comment')
    button_order = (By.CLASS_NAME, 'smart-button')
    driver_information = (By.XPATH, "//div[contains(@class, 'order-header-title')]")

    def __init__(self, driver):
        self.driver = driver

    # Espera a que aparezca el Formulario
    def wait_for_order_form_tariff_card(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.tariff_card))

    def select_tariff_card(self, index):
        self.driver.find_elements(*self.car_list)[index].click()

    def get_tariff_card_name(self, index):
        cards = self.driver.find_elements(*self.car_list)
        if len(cards) > index:
            title_element = cards[index].find_element(By.CLASS_NAME, "tcard-title")
            return title_element.text.strip()
        else:
            raise Exception(f"No se encontró la tarjeta en el índice {index}. Se encontraron {len(cards)} elementos.")

    def set_message_driver(self,message_for_driver):
        self.driver.find_element(*self.message_field).send_keys(message_for_driver)

    def get_message_driver(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def click_button_order_form(self):
        self.driver.find_element(*self.button_order).click()
        time.sleep(5)

    def wait_for_driver_information(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.driver_information))

    def set_tariff_card(self, index):
        self.wait_for_order_form_tariff_card()
        self.select_tariff_card(index)
        self.get_tariff_card_name(index)

    def set_form_message_driver(self,message_for_driver):
        self.set_message_driver(message_for_driver)

    def set_order_form(self):
        self.click_button_order_form()
        self.wait_for_driver_information()

class PhoneFormPage:
    button_phone_number = (By.CLASS_NAME, 'np-button')
    number_field = (By.ID, 'phone')
    button_form_phone_number = (By.XPATH, "//button[text()='Siguiente']")
    code_field = (By.ID, 'code')
    button_code = (By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'full') and text()='Confirmar']")

    def __init__(self, driver):
        self.code = None
        self.driver = driver

    def click_button_phone_number(self):
        self.driver.find_element(*self.button_phone_number).click()

    def wait_for_modal_form_phone_number(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.button_phone_number))

    def set_number_phone(self, number):
        self.driver.find_element(*self.number_field).send_keys(number)

    def get_phone_number(self):
        return self.driver.find_element(*self.number_field).get_property('value')

    def confirm_form_phone_number(self):
        self.driver.find_element(*self.button_form_phone_number).click()

    def code_confirmation(self):
        self.driver.find_element(*self.code_field).send_keys(retrieve_phone_code(self.driver))

    def confirm_form_code(self):
        self.driver.find_element(*self.button_code).click()

    def set_form_phone_number(self, number):
        self.click_button_phone_number()
        self.wait_for_modal_form_phone_number()
        self.set_number_phone(number)
        self.get_phone_number()
        self.confirm_form_phone_number()
        self.code_confirmation()
        self.confirm_form_code()

class PaymentFormPage:

    payment_button = (By.CLASS_NAME, 'pp-button')
    add_card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.XPATH, "//div[@class='card-number-input']/input[@id='number']")
    card_code_field = (By.XPATH, "//div[@class='card-code-input']/input[@id='code']")
    form_click = (By.CLASS_NAME,'card-wrapper')
    add_button = (By.XPATH, "//div[@class='pp-buttons']/button[@type='submit' and text()='Agregar']")
    exit_button_payment_form = (By.CLASS_NAME, "close-button.section-close")

    def __init__(self, driver):
        self.code = None
        self.driver = driver

    def click_payment_button(self):
        self.driver.find_element(*self.payment_button).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_cvv_number(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_cvv_number(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def click_add_button(self):
        self.driver.find_element(*self.form_click).click()
        self.driver.find_element(*self.add_button).click()

    def click_exit_payment_form(self):
        self.driver.find_elements(*self.exit_button_payment_form)[2].click()

    def set_form_payment(self, card_number, card_code):
        self.click_payment_button()
        self.click_add_card_button()
        self.set_card_number(card_number)
        self.set_cvv_number(card_code)
        self.click_add_button()
        self.click_exit_payment_form()

class RequirementsPage :

    switch_blanket_scarves = (By.XPATH, "//div[@class='r-sw-container'][.//div[text()='Manta y pañuelos']]//span[contains(@class, 'slider')]")
    ice_cream_button = (By.XPATH, "//div[@class='r-counter-container'][.//div[text()='Helado']]//div[contains(@class, 'counter-plus')]")
    ice_cream_value = (By.XPATH, "//div[@class='r-counter-container'][.//div[text()='Helado']]//div[@class='counter-value']")

    def __init__(self, driver):
        self.code = None
        self.driver = driver

    def click_switch_requirement_blanket_scarves(self):
        self.driver.find_element(*self.switch_blanket_scarves).click()

    def click_for_ice_cream(self, amount_ice_cream):
        button = self.driver.find_element(*self.ice_cream_button)
        for _ in range(amount_ice_cream):
            button.click()

    def get_amount_ice_cream(self):
        return int(self.driver.find_element(*self.ice_cream_value).text)

    def set_requirements(self, amount_ice_cream):
        self.click_switch_requirement_blanket_scarves()
        self.click_for_ice_cream(amount_ice_cream)
        self.get_amount_ice_cream()
