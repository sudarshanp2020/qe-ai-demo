import pytest
from playwright.sync_api import Page, expect
from tests.pages.greenkart_page import GreenKartPage


class TestGreenKartSearch:
    """Test cases for product search functionality."""
    
    @pytest.mark.smoke
    def test_search_product_by_name(self, page: Page):
        """Test searching for a product by name."""
        greenkart = GreenKartPage(page)
        
        # Search for brocolli (note: website has typo - one 'c')
        greenkart.search_product("bro")
        
        # Verify brocolli is displayed
        assert greenkart.verify_product_displayed("brocolli"), "Brocolli should be displayed in search results"
        
        # Verify only matching products are shown
        products = greenkart.get_visible_products()
        assert len(products) > 0, "At least one product should be displayed"
        
        for product in products:
            product_name = greenkart.get_product_name(product)
            assert "bro" in product_name.lower(), f"Product {product_name} should contain 'bro'"
    
    @pytest.mark.smoke
    def test_search_with_no_results(self, page: Page):
        """Test searching with a term that has no results."""
        greenkart = GreenKartPage(page)
        
        # Search for non-existent product
        greenkart.search_product("xyz123")
        
        # Verify no products are displayed
        products = greenkart.get_visible_products()
        visible_products = [p for p in products if p.is_visible()]
        assert len(visible_products) == 0, "No products should be displayed for invalid search"
    
    @pytest.mark.regression
    def test_search_case_insensitive(self, page: Page):
        """Test that search is case insensitive."""
        greenkart = GreenKartPage(page)
        
        # Search with uppercase
        greenkart.search_product("TOMATO")
        
        # Verify tomato is displayed
        assert greenkart.verify_product_displayed("tomato"), "Search should be case insensitive"
    
    @pytest.mark.regression
    def test_clear_search(self, page: Page):
        """Test clearing search shows all products."""
        greenkart = GreenKartPage(page)
        
        # First search for specific product
        greenkart.search_product("cucumber")
        products_after_search = len(greenkart.get_visible_products())
        
        # Clear search
        greenkart.search_product("")
        products_after_clear = len(greenkart.get_visible_products())
        
        # Verify more products are shown after clearing
        assert products_after_clear > products_after_search, "Clearing search should show more products"


class TestGreenKartCart:
    """Test cases for shopping cart functionality."""
    
    @pytest.mark.smoke
    def test_add_single_product_to_cart(self, page: Page):
        """Test adding a single product to cart."""
        greenkart = GreenKartPage(page)
        
        # Add first product to cart
        greenkart.add_product_to_cart_by_index(0)
        
        # Verify cart count is updated
        cart_count = greenkart.get_cart_count()
        assert "1" in cart_count, "Cart should show 1 item"
    
    @pytest.mark.smoke
    def test_add_multiple_products_to_cart(self, page: Page):
        """Test adding multiple products to cart."""
        greenkart = GreenKartPage(page)
        
        # Add three products to cart
        greenkart.add_product_to_cart_by_index(0)
        greenkart.add_product_to_cart_by_index(1)
        greenkart.add_product_to_cart_by_index(2)
        
        # Verify cart count
        cart_count = greenkart.get_cart_count()
        assert "3" in cart_count, "Cart should show 3 items"
    
    @pytest.mark.regression
    def test_add_product_by_name(self, page: Page):
        """Test adding a specific product by name."""
        greenkart = GreenKartPage(page)
        
        # Search and add brocolli (note: website has typo - one 'c')
        greenkart.search_product("brocolli")
        greenkart.add_product_to_cart_by_name("brocolli")
        
        # Verify cart count
        cart_count = greenkart.get_cart_count()
        assert "1" in cart_count, "Cart should show 1 item after adding brocolli"
    
    @pytest.mark.regression
    def test_cart_icon_clickable(self, page: Page):
        """Test that cart icon is clickable and opens cart preview."""
        greenkart = GreenKartPage(page)
        
        # Add product to cart
        greenkart.add_product_to_cart_by_index(0)
        
        # Click cart icon
        greenkart.open_cart()
        
        # Verify cart preview is visible
        expect(greenkart.proceed_to_checkout_btn).to_be_visible()


class TestGreenKartCheckout:
    """Test cases for checkout functionality."""
    
    @pytest.mark.smoke
    def test_proceed_to_checkout(self, page: Page):
        """Test proceeding to checkout page."""
        greenkart = GreenKartPage(page)
        
        # Add products and proceed to checkout
        greenkart.add_product_to_cart_by_index(0)
        greenkart.add_product_to_cart_by_index(1)
        greenkart.open_cart()
        greenkart.proceed_to_checkout()
        
        # Verify checkout page is loaded
        expect(greenkart.place_order_btn).to_be_visible()
        expect(greenkart.promo_code_input).to_be_visible()
    
    @pytest.mark.regression
    def test_apply_invalid_promo_code(self, page: Page):
        """Test applying an invalid promo code."""
        greenkart = GreenKartPage(page)
        
        # Add product and go to checkout
        greenkart.add_product_to_cart_by_index(0)
        greenkart.open_cart()
        greenkart.proceed_to_checkout()
        
        # Apply invalid promo code
        greenkart.apply_promo_code("INVALID123")
        
        # Verify error message
        promo_message = greenkart.get_promo_message()
        assert "invalid" in promo_message.lower(), "Should show invalid promo code message"
    
    @pytest.mark.regression
    def test_apply_valid_promo_code(self, page: Page):
        """Test applying a valid promo code."""
        greenkart = GreenKartPage(page)
        
        # Add product and go to checkout
        greenkart.add_product_to_cart_by_index(0)
        greenkart.open_cart()
        greenkart.proceed_to_checkout()
        
        # Apply valid promo code (rahulshettyacademy is a known valid code)
        greenkart.apply_promo_code("rahulshettyacademy")
        
        # Verify success message
        promo_message = greenkart.get_promo_message()
        assert "applied" in promo_message.lower() or "success" in promo_message.lower(), "Should show promo code applied message"
    
    @pytest.mark.smoke
    def test_place_order_button_visible(self, page: Page):
        """Test that place order button is visible on checkout page."""
        greenkart = GreenKartPage(page)
        
        # Add product and go to checkout
        greenkart.add_product_to_cart_by_index(0)
        greenkart.open_cart()
        greenkart.proceed_to_checkout()
        
        # Verify place order button
        expect(greenkart.place_order_btn).to_be_visible()
        expect(greenkart.place_order_btn).to_be_enabled()


class TestGreenKartUI:
    """Test cases for UI elements and layout."""
    
    @pytest.mark.ui
    def test_page_title(self, page: Page):
        """Test that page has correct title."""
        expect(page).to_have_title("GreenKart - veg and fruits kart")
    
    @pytest.mark.ui
    def test_search_box_visible(self, page: Page):
        """Test that search box is visible and functional."""
        greenkart = GreenKartPage(page)
        
        expect(greenkart.search_input).to_be_visible()
        expect(greenkart.search_input).to_be_editable()
    
    @pytest.mark.ui
    def test_products_display_with_images(self, page: Page):
        """Test that products are displayed with images."""
        greenkart = GreenKartPage(page)
        
        products = greenkart.get_visible_products()
        assert len(products) > 0, "Products should be displayed"
        
        # Check first product has image
        first_product = products[0]
        product_image = first_product.locator("img")
        expect(product_image).to_be_visible()
    
    @pytest.mark.ui
    def test_cart_icon_visible(self, page: Page):
        """Test that cart icon is visible."""
        greenkart = GreenKartPage(page)
        
        expect(greenkart.cart_icon).to_be_visible()
    
    @pytest.mark.ui
    def test_product_cards_have_required_elements(self, page: Page):
        """Test that product cards have all required elements."""
        greenkart = GreenKartPage(page)
        
        products = greenkart.get_visible_products()
        first_product = products[0]
        
        # Check for product name
        product_name = first_product.locator("h4.product-name")
        expect(product_name).to_be_visible()
        
        # Check for product price
        product_price = first_product.locator("p.product-price")
        expect(product_price).to_be_visible()
        
        # Check for add to cart button
        add_button = first_product.locator("button:has-text('ADD TO CART')")
        expect(add_button).to_be_visible()


class TestGreenKartEndToEnd:
    """End-to-end test scenarios."""
    
    @pytest.mark.smoke
    def test_complete_shopping_flow(self, page: Page):
        """Test complete shopping flow from search to checkout."""
        greenkart = GreenKartPage(page)
        
        # Step 1: Search for product
        greenkart.search_product("cucumber")
        assert greenkart.verify_product_displayed("cucumber"), "Cucumber should be found"
        
        # Step 2: Add product to cart
        greenkart.add_product_to_cart_by_name("cucumber")
        
        # Step 3: Search for another product
        greenkart.search_product("tomato")
        assert greenkart.verify_product_displayed("tomato"), "Tomato should be found"
        
        # Step 4: Add second product
        greenkart.add_product_to_cart_by_name("tomato")
        
        # Step 5: Verify cart count
        cart_count = greenkart.get_cart_count()
        assert "2" in cart_count, "Cart should have 2 items"
        
        # Step 6: Open cart
        greenkart.open_cart()
        
        # Step 7: Proceed to checkout
        greenkart.proceed_to_checkout()
        
        # Step 8: Verify on checkout page
        expect(greenkart.place_order_btn).to_be_visible()
        expect(greenkart.promo_code_input).to_be_visible()
    
    @pytest.mark.regression
    def test_shopping_with_promo_code(self, page: Page):
        """Test shopping flow with promo code application."""
        greenkart = GreenKartPage(page)
        
        # Add multiple products
        greenkart.add_product_to_cart_by_index(0)
        greenkart.add_product_to_cart_by_index(1)
        greenkart.add_product_to_cart_by_index(2)
        
        # Go to checkout
        greenkart.open_cart()
        greenkart.proceed_to_checkout()
        
        # Apply promo code
        greenkart.apply_promo_code("rahulshettyacademy")
        
        # Verify promo applied
        promo_message = greenkart.get_promo_message()
        assert len(promo_message) > 0, "Promo message should be displayed"
        
        # Verify place order button is still available
        expect(greenkart.place_order_btn).to_be_visible()

# Made with Bob
