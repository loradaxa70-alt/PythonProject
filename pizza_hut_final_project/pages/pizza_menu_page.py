

class PizzaMenuPage():
    def __init__(self, driver):
        self.driver = driver



    def enter_pizza_menu_page(self):
        self.driver.get('https://www.pizzahut.com/menu/pizza')
        print('correct url to pizza menu')
        url = self.driver.current_url
        assert url == 'https://www.pizzahut.com/menu/pizza', 'pizza menu url is not as expected'
