import pytest

from models.checkout_data_model import CheckoutDataModel
from models.login_data_model import LoginDataModel
from pages.login.login_page import LoginPage
from pages.product.products_grid_page import ProductsGridPage
from pages.product.sort_option import SortOption
from tests.test_base import TestBase


class TestShop(TestBase):

    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page, request):
        page.goto(self.VARIABLES['base_url'])

        is_valid = 'invalid_login' not in request.node.keywords
        LoginPage(page).log_in(LoginDataModel.get_login_data(self.VARIABLES, is_valid))

    @pytest.mark.invalid_login
    def test_locked_out_user_log_in(self, page):
        error_msg = LoginPage(page).get_error_msg()
        expected_error_msg = self.VARIABLES['users']['locked_out']['error_msg']

        assert error_msg == expected_error_msg

    def test_check_out_flow(self, page):
        products_page = ProductsGridPage(page)
        confirm_msg = (products_page
                       .add_to_basket_n_products(products_page.get_random_quantity())
                       .go_to_cart()
                       .go_to_checkout()
                       .fill_checkout_data(CheckoutDataModel.get_checkout_data(self.VARIABLES))
                       .go_to_overview()
                       .confirm_purchase()
                       .get_confirmation_msg()
                       )
        expected_confirm_msg = self.VARIABLES['users']['standard']['confirmation_msg']

        assert confirm_msg == expected_confirm_msg

    @pytest.mark.parametrize("sort_option, is_descending", [
        (SortOption.AZ, False),
        (SortOption.ZA, True),
    ])
    def test_sort_products_by_title(self, page, sort_option, is_descending):
        products_page = ProductsGridPage(page)
        product_titles = products_page.save_product_titles()
        sorted_product_titles = products_page.sort_products(sort_option).save_product_titles()

        assert sorted_product_titles == sorted(product_titles, reverse=is_descending)

    @pytest.mark.parametrize("sort_option, is_descending", [
        (SortOption.PRICE_LOW_HIGH, False),
        (SortOption.PRICE_HIGH_LOW, True),
    ])
    def test_sort_products_by_price(self, page, sort_option, is_descending):
        products_page = ProductsGridPage(page)
        products_prices = products_page.save_product_prices()
        sorted_product_prices = products_page.sort_products(sort_option).save_product_prices()

        assert sorted_product_prices == sorted(products_prices, reverse=is_descending)

    def test_product_details_display(self, page):
        products_page = ProductsGridPage(page)
        random_product = products_page.get_nth_product_container(products_page.get_random_quantity())

        product_on_grid = (random_product
                           .map_to_product_model())

        product_on_its_page = (random_product
                               .go_to_product_page()
                               .map_to_product_model())

        assert product_on_grid == product_on_its_page
