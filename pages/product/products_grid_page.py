from __future__ import annotations

import random

from playwright.sync_api import Page

from pages.checkout.basket_page import BasketPage
from pages.product.product_container_component import ProductContainerComponent
from pages.product.sort_option import SortOption


class ProductsGridPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.shopping_cart = page.locator('.shopping_cart_link')
        self.product_containers = page.locator('[data-test="inventory-item"]')
        self.sort_dropdown = page.locator('.product_sort_container')

    def get_product_containers(self) -> list[ProductContainerComponent]:
        return [ProductContainerComponent(self.page, self.product_containers.nth(i))
                for i in range(self.get_product_count())]

    def get_nth_product_container(self, index: int) -> ProductContainerComponent:
        return ProductContainerComponent(self.page, self.product_containers.nth(index))

    def add_to_basket_n_products(self, n: int) -> ProductsGridPage:
        for index in range(n):
            self.get_nth_product_container(index).add_to_basket()
        return self

    def save_product_titles(self) -> list[str]:
        return [container.get_product_title() for container in self.get_product_containers()]

    def save_product_prices(self) -> list[float]:
        return [container.get_product_price() for container in self.get_product_containers()]

    def sort_products(self, sort_option: SortOption) -> ProductsGridPage:
        self.sort_dropdown.select_option(sort_option.value)
        return self

    def go_to_cart(self) -> BasketPage:
        self.shopping_cart.click()
        return BasketPage(self.page)

    def get_random_quantity(self) -> int:
        return random.randint(1, self.get_product_count())

    def get_product_count(self) -> int:
        return self.product_containers.count()
