import random

from pages.checkout.basket_page import BasketPage
from pages.product.product_container_component import ProductContainerComponent


class ProductsGridPage:
    def __init__(self, page):
        self.page = page
        self.shopping_cart = page.locator('.shopping_cart_link')
        self.product_containers = page.locator('[data-test="inventory-item"]')
        self.sort_dropdown = page.locator('.product_sort_container')

    def get_product_containers(self):
        return [ProductContainerComponent(self.page, self.product_containers.nth(i), )
                for i in range(self.get_product_count())]

    def get_nth_product_container(self, index):
        container = self.product_containers.nth(index)
        return ProductContainerComponent(self.page, container)

    def add_to_basket_n_products(self, n):
        for index in range(n):
            self.get_nth_product_container(index).add_to_basket()
        return self

    def save_product_titles(self):
        product_container_components = self.get_product_containers()
        return [container.get_product_title() for container in product_container_components]

    def save_product_prices(self):
        product_container_components = self.get_product_containers()
        return [container.get_product_price() for container in product_container_components]

    def sort_products(self, sort_option: 'SortOption'):
        self.sort_dropdown.select_option(sort_option.value)
        return self

    def go_to_cart(self):
        self.shopping_cart.click()
        return BasketPage(self.page)

    def get_random_quantity(self):
        return random.randint(1, self.get_product_count())

    def get_product_count(self):
        return self.product_containers.count()
