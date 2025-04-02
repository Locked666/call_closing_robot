from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager # Import the Edge driver manager
from datetime import datetime
from time import sleep
from text_for_close import text
from random import choice, randint
from dotenv import dotenv_values

config = dotenv_values(".env")

# Load environment variables
URL = config['URL_INIT']
USERNAME = config['MY_SECRET_USERNAME']
PASSWORD = config['MY_SECRET_PASSWORD']
TIME_SLEEP = 5


def _close_system_ticket():
    exit(0)

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
        print(f"Ocorrou um erro ao fazer login: {e}")
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

# Caso exista tickets para agrupar 

def _group_ticket(driver):
    try:
        # Wait until the modal is present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal-chamados-vinculados-id")))
        
        # Find all buttons with IDs starting with "btagrup_"
        buttons = driver.find_elements(By.XPATH, "//a[starts-with(@id, 'btagrup_')]")
        
        for button in buttons:
            try:
                # Click the button
                button.click()
                # print(f"Clicked button with ID: {button.get_attribute('id')}")
                
                # Handle any alerts that may appear
                __handle_alert(driver)
                
                # Wait for a short period to ensure the action is completed
                sleep(1)
            except Exception as e:
                print(f"Ocorreu um erro ao agupar tickets {button.get_attribute('id')}: {e}")
                continue
        click_close_alert_button(driver)
        return True    
    except Exception as e:
        print(f"Error in _group_ticket: {e}")

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
        # print("Alerta tratado com sucesso.")
        
    except Exception as e:
        print(f"Ocorreu um erro ao tratar alerta: {e}")

# Verificar a quantidade de linhas na tabela 
def check_table_has_rows(driver):
    try:
        # Wait until the table is loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tListaSac")))

        # Get all rows in the tbody
        rows = driver.find_elements(By.XPATH, "//table[@id='tListaSac']/tbody/tr")
        
        # print(f"Found {len(rows)} rows.")
        
        if len(rows) > 1:
            # print("Existe Linhas na tabela.")
            return True
        else:
            # print("Não existe linhas na tabela.")
            return False
    except Exception as e:
        print(f"Ocorreu um erro ao verificar linhas da tabela:\n Funcão (check_table_has_rows)\n {e}")
        return False

# Acessar a aba de chamados vinculados
def access_linked_tickets_tab(driver):
    try:
        # Check if the div exists
        if check_div_exists(driver, "boxAbasChamados"):
            # Click on the "chamados vinculados" tab
            linked_tickets_tab = driver.find_element(By.XPATH, "//a[@href=\"javascript:trocaAbaChamados('chamado');\" and @id='btAbaChamTic']")
            linked_tickets_tab.click()
            print("Verificando na aba Chamados Vinculados.")
            
            # Check if the table has rows
            return check_table_has_rows(driver)
        else:
            print("Não existe chamados vinculados")
            return False
    except Exception as e:
        print(f"Ocorreu um erro ao verificar a aba chamados vincualados:\n {e}")
        return False

def __randon_system_closed(n_system:list = []):
    """Gerador do sistema a ser fechado o ticket, gerado de forma aleatória.

    Args:
        n_system (list[int]): passado o número de sistemas que estão disponíveis para serem fechados.
    """
    try:
        if len(n_system) == 0:
            return choice(['2','3','4','5','125','73','7','45','61','8','9','11','82'])
        else :
            system = choice(n_system)
            return system
    except Exception as e:
        print(f"An error occurred: {e}")
    
## Method to alter ticket after close
def __alter_ticket(driver):
    print("Alterando ticket")
    sleep(TIME_SLEEP)
    
    try:
        # 1. Set "cSistema" to the value "5"
        
        if check_div_exists(driver, "boxAbasChamados"):
            access_linked_tickets_tab(driver)
            if check_table_has_rows(driver):
                # Check if the title attribute of the specified element is "encerrado"
                try:
                    element = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[8]/table/tbody/tr[2]/td[9]")
                    if element.get_attribute("title").lower() == "encerrado":
                        print("O chamado já está encerrado.")
                    else : 
                        print("Existe chamados vinculados, mas não estão encerrados.")
                        return    
                except Exception as e:
                    print(f"Erro ao verificar o título do elemento: {e}")
        
        else :             
            try: 
                sistema_select_sistema = Select(driver.find_element(By.ID, "cSistema"))
                # Try to select by value
                sistema_select_sistema.select_by_value(__randon_system_closed())
                
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
            except Exception as e:
                print(f"Ocorreu um erro na função(__alter_ticket) : {e} \n {e.__traceback__} \n {e.__cause__} \n {e.__context__} ")
            
            
        __close_ticket(driver)
    
    except Exception as e:
        print(f"Ocorreu um erro na função(__alter_ticket) : {e} \n {e.__traceback__} \n {e.__cause__} \n {e.__context__} ")
         
    
    # driver.quit()

#   method to close ticket
def __close_ticket(driver):
    sleep(TIME_SLEEP)
    
    # clicked bnt close ticket
    close_ticket_button = WebDriverWait(driver, TIME_SLEEP).until(
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
        
        save_ticket_button = WebDriverWait(driver, TIME_SLEEP).until(
        EC.element_to_be_clickable((By.ID, "btSalvar"))
        )
        save_ticket_button.click()  
        __handle_alert(driver)
        
        sleep(TIME_SLEEP)
        
    except Exception as e:
        print(f"Ocorreu um erro na funcção (__close_ticket): {e} \n {e.__traceback__} \n {e.__cause__} \n {e.__context__} ")

def check_div_exists(driver, div_id):
    try:
        elements = driver.find_elements(By.ID, div_id)
        if len(elements) > 0:
            # print(f"Div with ID '{div_id}' exists.")
            return True
        else:
            # print(f"Div with ID '{div_id}' does not exist.")
            return False
    except NoSuchElementException:
        # print(f"Div with ID '{div_id}' does not exist.")
        return False
    
def click_close_alert_button(driver):
    try:
        # Wait until the button is present
        close_alert_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='javascript:fecharAlertaTickets();' and @class='btnPadraoSac']"))
        )
        # Click the button
        close_alert_button.click()
        # print("Clicked the close alert button.")
    except Exception as e:
        print(f"Error clicking the close alert button: {e}")

def get_data(driver):
    n_tickets = []
    while True:
        try:
            
            # Wait until the table is loaded
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tListaSac")))

            # Get all rows in the tbody
            rows = driver.find_elements(By.XPATH, "//table[@id='tListaSac']/tbody/tr")
            
            # print(f"Found {len(rows)} rows.")
            if len(rows) <= 1:
                print("Não existe linhas na tabela.")
                _close_system_ticket()
                break
            
            for row in rows:
                # Get the link (first <a> element) in the row
                print(f"{len(n_tickets)} - {len(rows)}")  
                try: 
                    # print(f'Entrou no for' )
                    # print(f"n_tickets  = {n_tickets}")
                    
                    link_element = row.find_element(By.XPATH, ".//a[contains(@href, 'conteudo=sac_ticketaberto')]")
                    href = link_element.get_attribute("href")
                    
                    if href in n_tickets:
                        if len(rows) == len(n_tickets):
                            print("Todos os Tickets Foram Processados")
                            _close_system_ticket()
                            break
                        else:
                            continue
                        
                        
                    else: 
                        # Execute your function (e.g., open the link)
                        print(f"Processing: {href}")
                        
                        
                        driver.get(href)  # Navigate to the link
                        __alter_ticket(driver)  # Call the function to alter the ticket
                        n_tickets.append(href)
                        # Return to the main page or perform other necessary actions before the next iteration
                        driver.back()  # Go back to the previous page
                        _set_hundred_page(driver)
                        
                        break  # Proceed to the next row
                      
                except Exception as e:
                    print(f"Ocorreu um erro no processo for row in rows: {e}")
                    if 'no such element'.lower() in str(e):
                        break
                
        except Exception as e:
            print(f"Ocorreu um erro no laço de repetição while: {e} \n {e.__traceback__} \n {e.__cause__} \n {e.__context__} ")
            continue

def _set_hundred_page(driver):
    try: 
        
        value_page_exist = Select(driver.find_element(By.NAME, 'tListaSac_length'))
        value_page_exist.select_by_index(3)
        sleep(TIME_SLEEP)
    except  Exception as e: 
        print(f" Ocorreu um erro ao realizar  a função de mudar a quantidade de paginas: {e} \n {e.__cause__}")


def main():
    driver = open_browser()
    driver.get(URL)
    if login(driver):
        print("Sucesso ao realizar Login")
        sleep(TIME_SLEEP)
        if not check_div_exists(driver, "modal-chamados-vinculados-id"):
            # _set_filter_ticket(driver)
            _set_hundred_page(driver)
            get_data(driver)
        else:
            group = _group_ticket(driver)
            if group:
                # _set_filter_ticket(driver)
                _set_hundred_page(driver)
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
      