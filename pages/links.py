import pytest

class MainPageLinks():
    MAIN_LINK           = "http://selenium1py.pythonanywhere.com/"
    LOG_LINK            = "http://selenium1py.pythonanywhere.com/accounts/login/"

class ProductPageLinks():   
    COMMON_LINK         = "http://selenium1py.pythonanywhere.com/catalogue/"
    
    PRODUCT_LINK        = "en-gb/catalogue/the-city-and-the-stars_95/"

    ITEM_TO_CARD_LINKS  = [
    ("the-shellcoders-handbook_209/?promo=newYear"),
    ("coders-at-work_207/?promo=newYear2019.")  
    ]
    
    NUMBER_OF_PAGES     = 10
    PROMO_PAGES_LINKS   = []
    XFAIL = 7
    for i in range(NUMBER_OF_PAGES):
        if i == XFAIL:
            bugged_link = f"{COMMON_LINK}coders-at-work_207/?promo=offer{i}"
            PROMO_PAGES_LINKS.append(pytest.param(bugged_link, marks=pytest.mark.xfail(reason="Mistake on page: Product name does not match message.")))
        else:
            PROMO_PAGES_LINKS.append(f"{COMMON_LINK}coders-at-work_207/?promo=offer{i}")
        with open('list_of_links.txt', 'w') as ouf:
            ouf.write(str(PROMO_PAGES_LINKS) + '\n')
