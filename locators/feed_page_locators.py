from selenium.webdriver.common.by import By


class FeedPageLocators:
    TITLE_FEED = By.XPATH, "//h1[contains(text(),'Лента заказов')]"
    FIRST_ORDER_IN_LIST = By.XPATH, "//body/div[@id='root']/div[@class='App_App__aOmNj']/main[@class='App_componentContainer__2JC2W']/div[@class='OrderFeed_orderFeed__2RO_j']/div[@class='OrderFeed_contentBox__3-tWb']/ul[@class='OrderFeed_list__OLh59']/li[1]"
    MODAL_WINDOW_ORDER = By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"
    TEXT_MODAL_WINDOW_ORDER = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"
    ID_ORDER = By.XPATH, "//p[@class='text text_type_digits-default']"
    NUMBER_ALL_TIME = By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    NUMBER_ORDER = By.XPATH, "//ul[@class='OrderFeed_orderList__cBvyi']//li[1]"
    NUMBER_TODAY = By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
