from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager # Import the Edge driver manager
from datetime import datetime
from time import sleep
from text_for_close import text
from random import choice
from dotenv import dotenv_values

config = dotenv_values(".env")

# Load environment variables
URL = config['URL_INIT']
USERNAME = config['MY_SECRET_USERNAME']
PASSWORD = config['MY_SECRET_PASSWORD']




def open_browser():
    # Set the path to the edgedriver
    s = Service(EdgeChromiumDriverManager().install())
    
    # Set the options for the edgedriver
    edge_options = Options()
    edge_options.add_argument("--disable-features=EdgeSignin")
    # edge_options.add_argument("--headless")
    # edge_options.add_argument("--no-sandbox")
    # edge_options.add_argument("--disable-dev-shm-usage")
    
    # Start the edgedriver
    driver = webdriver.Edge(service=s, options=edge_options)
    return driver


def generate_text_close_ticket():
    return choice(text)


def login(driver):
    try :
        # Get the username field
        username = driver.find_element(By.ID, "login")
        # Type the username
        username.send_keys(USERNAME)
        # Get the password field
        password = driver.find_element(By.ID, "senha")
        # Type the password
        password.send_keys(PASSWORD)
        # Press enter
        password.send_keys(Keys.RETURN)
        return True
    except Exception as e:
        print(e)
        driver.quit()
            
def _set_filter_ticket(driver):
    # Wait until the element is loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cPrazo")))
    
    # Get the select element
    select_element = Select(driver.find_element(By.ID, "cPrazo"))
    
    # Select the option with value="1"
    select_element.select_by_value("1")
    filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btnPadraoSac"))
    )
    filter_button.click()  


# def __alter_ticket(driver):
#     # Wait until the element is loaded
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cSistema")))
    
#     # Get the select element
#     select_element = Select(driver.find_element(By.ID, "cSistema"))
#     # Wait for the elements to be loaded on the page
                
#     try:
#         WebDriverWait(driver, 95).until(EC.presence_of_element_located((By.ID, "cSistema")))
#         sistema_select_sistema = Select(driver.find_element(By.ID, "cSistema"))
#         # Try to select by value
#         sistema_select_sistema.select_by_value("5")
#     except:
#         print("Option with value '5' not found. Trying to select by visible text.")
#         # If value "5" is not found, try selecting by visible text
    
#     # 2. Check if "cResponsavel" is empty; if so, set it to the first option
#     responsavel_select = Select(driver.find_element(By.ID, "cResponsavel"))
#     if responsavel_select.first_selected_option.get_attribute("value") == "0":  # If "responsável" is selected
#         responsavel_select.select_by_index(1)  # Select the first available option
    
#     # 3. Set "sPrevisao" to the current date in "dd/mm/yyyy" format
#     previsao_input = driver.find_element(By.ID, "sPrevisao")
#     current_date = datetime.now().strftime("%d/%m/%Y")
#     previsao_input.clear()  # Clear any existing value
#     previsao_input.send_keys(current_date)  # Set the current date

#     # After setting the values, we can either continue with the next row or do further processing

def __handle_alert(driver):
    try:
        # Espera até o alerta ser presente
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        
        # Troca para o alerta
        alert = Alert(driver)
        
        # Clica no botão "OK" (ou similar) no alerta
        alert.accept()
        print("Alert accepted.")
        
    except Exception as e:
        print(f"An error occurred: {e}")


## Method to alter ticket after close
def __alter_ticket(driver):
    print("Alterando ticket")
    sleep(5)
    
    # 1. Set "cSistema" to the value "5"
    
    sistema_select_sistema = Select(driver.find_element(By.ID, "cSistema"))
    # Try to select by value
    sistema_select_sistema.select_by_value("5")
    
    # 2. Check if "cResponsavel" is empty; if so, set it to the first option
    responsavel_select = Select(driver.find_element(By.ID, "cResponsavel"))
    if responsavel_select.first_selected_option.get_attribute("value") == "0":  # If "responsável" is selected
        responsavel_select.select_by_index(1)  # Select the first available option
    
    # 3. Set "sPrevisao" to the current date in "dd/mm/yyyy" format
    previsao_input = driver.find_element(By.ID, "sPrevisao")
    current_date = datetime.now().strftime("%d/%m/%Y")
    previsao_input.clear()  # Clear any existing value
    previsao_input.send_keys(current_date)  # Set the current date
    
    # 4. Click the "Salvar" button
    
    update_ticket_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btAtualizar"))
    )
    update_ticket_button.click()  
    
    __handle_alert(driver)
    
    __close_ticket(driver)
    
    # driver.quit()

#   method to close ticket
def __close_ticket(driver):
    sleep(5)
    
    # clicked bnt close ticket
    close_ticket_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btAtribuir"))
    )
    close_ticket_button.click()  

    try:
        # Espera até que o estilo de display da div não seja 'none'
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.ID, "boxFormInteracao").value_of_css_property('display') != 'none'
        )
        
        # Aqui a div já está visível (display diferente de 'none')
        # Então, podemos prosseguir com a interação
        textarea = driver.find_element(By.ID, "cMotivoEnc")
        textarea.send_keys(generate_text_close_ticket())
        
        save_ticket_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btSalvar"))
        )
        save_ticket_button.click()  
        __handle_alert(driver)
        
        sleep(5)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    
        
    

        


def get_data(driver):
    while True:
        try:
            # Wait until the table is loaded
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tListaSac")))

            # Get all rows in the tbody
            rows = driver.find_elements(By.XPATH, "//table[@id='tListaSac']/tbody/tr")
            
            for row in rows:
                # Get the link (first <a> element) in the row
                link_element = row.find_element(By.XPATH, ".//a[contains(@href, 'conteudo=sac_ticketaberto')]")
                href = link_element.get_attribute("href")
                
                # Execute your function (e.g., open the link)
                print(f"Processing: {href}")
                driver.get(href)  # Navigate to the link
                __alter_ticket(driver)  # Call the function to alter the ticket
                
                # Return to the main page or perform other necessary actions before the next iteration
                driver.back()  # Go back to the previous page
    
                break  # Proceed to the next row
        except Exception as e:
            print(f"An error occurred: {e}")
            break


def main():
    driver = open_browser()
    driver.get(URL)
    if login(driver):
        print("Login success")
        _set_filter_ticket(driver)
        get_data(driver)
    else:
        print("Login failed")
    driver.quit()

# Example of how to use the main function:
# main()

    
if __name__ == "__main__":
    # get_data()  # Call the function to get the data
    main() # Call the main function
    # a = generate_text_close_ticket()
    # print(a)
        