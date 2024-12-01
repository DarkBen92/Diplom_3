from selenium.webdriver.common.by import By


class MainPageLocators:
    TITLE_CONSTRUCTOR = By.XPATH, "//h1[contains(text(),'Соберите бургер')]"
    FIRST_BUN = By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][contains(text(),'Флюоресцентная булка R2-D3')]"
    MODAL_WINDOW_DETAILS = By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']"
    TITLE_MODAL_WINDOW_DETAILS = By.XPATH, "//h2[contains(text(),'Детали ингредиента')]"
    BUTTON_CLOSE_MODAL_WINDOW_DETAILS = By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']"
    CLOSE_MODAL_WINDOW_DETAILS = By.XPATH, "//section[@class='Modal_modal__P3_V5']"
    UP_BASKET = By.XPATH, "//ul[@class='BurgerConstructor_basket__list_modified__2DyZl BurgerConstructor_basket__list__l9dp_']"
    BASKET = By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']"
    COUNTER = By.XPATH, "//p[@class='counter_counter__num__3nue1']"
    BUTTON_CREATE_ORDER = By.XPATH, "//button[contains(text(),'Оформить заказ')]"
    ID_ORDER = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"
    CLOSE_WINDOW_ORDER = By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
