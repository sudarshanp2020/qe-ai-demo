from playwright.sync_api import Page, expect


class GreenKartPage:
    """Page Object Model for GreenKart application."""
    
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("input.search-keyword")
        self.product_cards = page.locator(".product")
        self.add_to_cart_buttons = page.locator("button:has-text('ADD TO CART')")
        self.cart_icon = page.locator("a.cart-icon")
        self.cart_items = page.locator(".cart-preview .cart-item")
        self.proceed_to_checkout_btn = page.locator("button:has-text('PROCEED TO CHECKOUT')")
        self.place_order_btn = page.locator("button:has-text('Place Order')")
        self.promo_code_input = page.locator("input.promoCode")
        self.apply_promo_btn = page.locator("button.promoBtn")
        self.promo_info = page.locator(".promoInfo")
        
    def search_product(self, product_name: str):
        """Search for a product by name."""
        self.search_input.fill(product_name)
        self.page.wait_for_timeout(1000)  # Wait for search results
        
    def get_visible_products(self):
        """Get all visible product cards."""
        return self.product_cards.all()
    
    def get_product_name(self, product_element):
        """Get product name from product card."""
        return product_element.locator("h4.product-name").inner_text()
    
    def get_product_price(self, product_element):
        """Get product price from product card."""
        return product_element.locator("p.product-price").inner_text()
    
    def add_product_to_cart_by_index(self, index: int):
        """Add product to cart by index."""
        products = self.get_visible_products()
        if index < len(products):
            add_btn = products[index].locator("button:has-text('ADD TO CART')")
            add_btn.click()
            self.page.wait_for_timeout(500)
    
    def add_product_to_cart_by_name(self, product_name: str):
        """Add product to cart by name."""
        products = self.get_visible_products()
        for product in products:
            name = self.get_product_name(product)
            if product_name.lower() in name.lower():
                add_btn = product.locator("button:has-text('ADD TO CART')")
                add_btn.click()
                self.page.wait_for_timeout(500)
                break
    
    def get_cart_count(self):
        """Get the number of items in cart."""
        cart_badge = self.page.locator(".cart-info tbody tr:nth-child(1) td:nth-child(3)")
        return cart_badge.inner_text()
    
    def open_cart(self):
        """Open the cart preview."""
        self.cart_icon.click()
        self.page.wait_for_timeout(500)
    
    def proceed_to_checkout(self):
        """Click proceed to checkout button."""
        self.proceed_to_checkout_btn.click()
        self.page.wait_for_load_state("networkidle")
    
    def apply_promo_code(self, promo_code: str):
        """Apply promo code."""
        self.promo_code_input.fill(promo_code)
        self.apply_promo_btn.click()
        self.page.wait_for_timeout(2000)  # Wait for promo validation
    
    def get_promo_message(self):
        """Get promo code validation message."""
        return self.promo_info.inner_text()
    
    def place_order(self):
        """Click place order button."""
        self.place_order_btn.click()
        self.page.wait_for_load_state("networkidle")
    
    def verify_product_displayed(self, product_name: str):
        """Verify if a product is displayed in search results."""
        products = self.get_visible_products()
        for product in products:
            name = self.get_product_name(product)
            if product_name.lower() in name.lower():
                return True
        return False

# Made with Bob
