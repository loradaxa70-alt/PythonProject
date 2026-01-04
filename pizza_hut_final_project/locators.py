from selenium.webdriver.common.by import By




class PizzaHutTestsLocators(object):
    SHOPPING_CART=(By.CLASS_NAME,"css-1h8ch3n")
    PIZZA_MENU=(By.CSS_SELECTOR, 'div >div.css-ug2o6l > a')
    CARRY_OUT_BUTTON=(By.CLASS_NAME,'css-1qy7znf')
    LOCATION_FIELD=(By.ID,'carryout-city-state-zip')
    SEARCH_BUTTON=(By.CSS_SELECTOR,'button[class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-fullWidth css-aoy6ko"]')
    RIGHT_LOCATION=(By.ID,"panel1bh-content-0")

class WelcomePageLocators(object):
    SEARCH=(By.ID, "search")
    RETURN_TO_WELCOME_PAGE=(By.CLASS_NAME, "css-2b4rnz")

class SchoolLunchPageLocators(object):
    CLICK_ON_SCHOOL_LUNCH=(By.LINK_TEXT, "School lunch")
