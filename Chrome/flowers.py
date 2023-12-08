from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from colorama import Fore, Style
import time


def click_element_if_present(driver, locator):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()
        return True
    except:
        return False


def order():
    service = Service()
    options = webdriver.ChromeOptions()

    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    # driver.set_window_position(2000, 0)
    # driver.set_window_size(1100, 1200)

    driver.get("https://www.bunches.co.uk")

    print("Bunches home page loaded 💐")

    product_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/section[2]/div[1]/div/a/img')
    product = wait.until(EC.element_to_be_clickable(product_locator))
    product.click()
    print("Flowers (Chrome) - Product Selected ✅")

    continue_button_locator = (By.CSS_SELECTOR, '.bn-button--lg.bn-button.bn-button--primary')
    if click_element_if_present(driver, continue_button_locator):
        print("Flowers - Variant picked ✅")
    else:
        print("🔔 Product has no variants. Skipping to the next step.")

    place_order_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div[2]/section[2]/div[4]/div[2]/button')
    place_order_button = wait.until(EC.element_to_be_clickable(place_order_button_locator))
    place_order_button.click()
    print("Flowers (Chrome) - Place order button pressed ✅")

    skip_button_locator = (By.XPATH, '//*[@id="extras"]/div/div[3]/button')
    skip_button = wait.until(EC.element_to_be_clickable(skip_button_locator))
    skip_button.click()
    print("Flowers (Chrome) - Extras Skipped ✅")

    card_select_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[2]/div/button')
    card_select = wait.until(EC.element_to_be_clickable(card_select_locator))
    card_select.click()

    free_card_locator = (By.XPATH, '/html/body/dialog/div/div/div[2]/div[3]/span/button')
    free_card = wait.until(EC.element_to_be_clickable(free_card_locator))
    free_card.click()
    print("Flowers (Chrome) - Default Card Selected ✅")

    message_locator = (By.XPATH, '//*[@id="message"]/section/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div')
    message = wait.until(EC.element_to_be_clickable(message_locator))
    message.click()
    message.send_keys('hello world')

    continue_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[3]/section/div[4]/button[2]')
    continue_button = wait.until(EC.element_to_be_clickable(continue_button_locator))
    continue_button.click()
    print("Flowers (Chrome) - Message added ✅")

    checkout_as_guest_button_locator = (By.XPATH, '//*[@id="details"]/div/div[2]/form/button[2]')
    checkout_as_guest_button = wait.until(EC.element_to_be_clickable(checkout_as_guest_button_locator))
    checkout_as_guest_button.click()

    email_input_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/form/div[1]/input')
    email_input = wait.until(EC.element_to_be_clickable(email_input_locator))
    email_input.send_keys('bot@test.com')

    name_input_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/form/div[2]/input')
    name_input = wait.until(EC.element_to_be_clickable(name_input_locator))
    name_input.send_keys('I am not a bot, I promise')

    telephone_input_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/form/div[3]/input')
    telephone_input = wait.until(EC.element_to_be_clickable(telephone_input_locator))
    telephone_input.send_keys('123456789')

    continue_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[4]/div/div[2]/form/div[5]/button')
    continue_button = wait.until(EC.element_to_be_clickable(continue_button_locator))
    continue_button.click()
    print("Flowers (Chrome) - Guess account name + email filled in ✅")

    recipient_name_input_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[1]/input')
    recipient_name_input = wait.until(EC.element_to_be_clickable(recipient_name_input_locator))
    recipient_name_input.send_keys('Mr Bottington Bot')

    manual_address_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[2]/a')
    manual_address_button = wait.until(EC.element_to_be_clickable(manual_address_button_locator))
    manual_address_button.click()

    address_postcode_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[6]/input')
    address_postcode = wait.until(EC.element_to_be_clickable(address_postcode_locator))
    address_postcode.send_keys('NG15 0DQ')

    address_line_1_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[2]/input')
    address_line_1 = wait.until(EC.element_to_be_clickable(address_line_1_locator))
    address_line_1.send_keys('25 Bot Street')

    address_line_2_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[3]/input')
    address_line_2 = wait.until(EC.element_to_be_clickable(address_line_2_locator))
    address_line_2.send_keys('Bot Road')

    address_line_3_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[4]/input')
    address_line_3 = wait.until(EC.element_to_be_clickable(address_line_3_locator))
    address_line_3.send_keys('Bot Town')

    address_town_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/div/div[5]/input')
    address_town = wait.until(EC.element_to_be_clickable(address_town_locator))
    address_town.send_keys('Bot Town 2')

    time.sleep(2)

    update_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/form/button')
    update_button = wait.until(EC.element_to_be_clickable(update_button_locator))
    update_button.click()

    continue_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[5]/div/div/button')
    continue_button = wait.until(EC.element_to_be_clickable(continue_button_locator))
    continue_button.click()
    print("Flowers (Chrome) - Recipient address entered ✅")

    proceed_to_payment_button_locator = (By.XPATH, '/html/body/div[1]/div[1]/main/div[3]/section[6]/div/div[2]/span/button')
    proceed_to_payment_button = wait.until(EC.element_to_be_clickable(proceed_to_payment_button_locator))
    proceed_to_payment_button.click()

    # print("Flowers (Chrome) - Proceeded to payment page ✅")
    print(f"{Fore.GREEN}Flowers (Chrome) - Proceeded to payment page {Fore.GREEN}✅{Style.RESET_ALL}")

    driver.quit()


if __name__ == '__main__':
    order()
