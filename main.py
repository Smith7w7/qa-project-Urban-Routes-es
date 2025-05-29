import data
from selenium import webdriver
from pages import UrbanRoutesPage
from pages import TariffPage
from pages import OrderFormPage
from pages import PhoneFormPage
from pages import PaymentFormPage
from pages import RequirementsPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        options = Options()
        for key, value in capabilities.items():
            options.set_capability(key, value)
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_home_page()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_tariff(self):
        tariff_page = TariffPage(self.driver)
        tariff_page.select_tariff()
        button_order_taxi_name = "Pedir un taxi"
        assert tariff_page.get_button_order_taxi_name() == button_order_taxi_name

    def test_set_card_tariff(self):
        order_form = OrderFormPage(self.driver)
        order_form.set_tariff_card(4)
        card_tariff_name = data.card_tariff_name
        assert order_form.get_tariff_card_name(4) == card_tariff_name

    def test_set_phone_form(self):
        phone_form = PhoneFormPage(self.driver)
        phone_number = data.phone_number
        phone_form.set_form_phone_number(phone_number)
        assert phone_form.get_phone_number() == phone_number

    def test_se_payment_form(self):
        payment_form = PaymentFormPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        payment_form.set_form_payment(card_number, card_code)
        assert payment_form.get_card_number() == card_number
        assert payment_form.get_cvv_number() == card_code

    def test_set_message_for_driver(self):
        order_form = OrderFormPage(self.driver)
        message_for_driver = data.message_for_driver
        order_form.set_form_message_driver(message_for_driver)
        assert order_form.get_message_driver() == message_for_driver

    def test_set_requirements_form(self):
        requirements_form = RequirementsPage(self.driver)
        amount_ice_cream = data.amount_ice_cream
        requirements_form.set_requirements(amount_ice_cream)
        assert requirements_form.get_amount_ice_cream() == amount_ice_cream

    def test_set_order_form(self):
        order_form = OrderFormPage(self.driver)
        order_form.set_order_form()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
