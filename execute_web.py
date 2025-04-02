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
from PySide6.QtCore import QObject, Signal
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

class WorkerLogger(QObject):
    """
    Classe simples para substituir os prints e enviar mensagens para a UI
    """
    log_signal = Signal(str)  # Sinal que será conectado à UI
    
    def log(self, message):
        """Método para log que substitui o print"""
        self.log_signal.emit(str(message))
        
    def __call__(self, message):
        """Permite usar a instância como função"""
        self.log(message)

# Cria uma instância global que será usada no lugar dos prints
work = WorkerLogger()



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
        work.log(e)
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
                work.log(f"Clicked button with ID: {button.get_attribute('id')}")
                
                # Handle any alerts that may appear
                __handle_alert(driver)
                
                # Wait for a short period to ensure the action is completed
                sleep(1)
            except Exception as e:
                work.log(f"Error clicking button with ID {button.get_attribute('id')}: {e}")
                continue
        click_close_alert_button(driver)
        return True    
    except Exception as e:
        work.log(f"Error in _group_ticket: {e}")

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
#         work.log("Option with value '5' not found. Trying to select by visible text.")
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
        work.log("Alerta tratado com sucesso.")
        
    except Exception as e:
        work.log(f"An error occurred: {e}")


def check_table_has_rows(driver):
    try:
        # Wait until the table is loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tListaSac")))

        # Get all rows in the tbody
        rows = driver.find_elements(By.XPATH, "//table[@id='tListaSac']/tbody/tr")
        
        work.log(f"Found {len(rows)} rows.")
        
        if len(rows) > 1:
            work.log("Existe Linhas na tabela.")
            return True
        else:
            work.log("Não existe linhas na tabela.")
            return False
    except Exception as e:
        work.log(f"An error occurred while checking the table: {e}")
        return False

def access_linked_tickets_tab(driver):
    try:
        # Check if the div exists
        if check_div_exists(driver, "boxAbasChamados"):
            # Click on the "chamados vinculados" tab
            linked_tickets_tab = driver.find_element(By.XPATH, "//a[@href=\"javascript:trocaAbaChamados('chamado');\" and @id='btAbaChamTic']")
            linked_tickets_tab.click()
            work.log("Clicado na aba chamados vinculados")
            
            # Check if the table has rows
            return check_table_has_rows(driver)
        else:
            work.log("Não existe chamados vinculados")
            return False
    except Exception as e:
        work.log(f"An error occurred while accessing the linked tickets tab: {e}")
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
        work.log(f"An error occurred: {e}")
    
## Method to alter ticket after close
def __alter_ticket(driver):
    work.log("Alterando ticket")
    sleep(TIME_SLEEP)
    
    try:
        # 1. Set "cSistema" to the value "5"
        
        if check_div_exists(driver, "boxAbasChamados"):
            access_linked_tickets_tab(driver)
            if check_table_has_rows(driver):
                return            
            
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
            work.log(f"Ocorreu um erro na função(__alter_ticket) : {e} \n {e.__traceback__} \n {e.__cause__} \n {e.__context__} ")
            
            
        __close_ticket(driver)
    
    except Exception as e:
        work.log(f"Ocorreu um erro na função(__alter_ticket) : {e} \n {e.__traceback__} \n {e.__cause__} \n {e.__context__} ")
         
    
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
        work.log(f"Ocorreu um erro na funcção (__close_ticket): {e} \n {e.__traceback__} \n {e.__cause__} \n {e.__context__} ")

def check_div_exists(driver, div_id):
    try:
        elements = driver.find_elements(By.ID, div_id)
        if len(elements) > 0:
            # work.log(f"Div with ID '{div_id}' exists.")
            return True
        else:
            # work.log(f"Div with ID '{div_id}' does not exist.")
            return False
    except NoSuchElementException:
        # work.log(f"Div with ID '{div_id}' does not exist.")
        return False
    
def click_close_alert_button(driver):
    try:
        # Wait until the button is present
        close_alert_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='javascript:fecharAlertaTickets();' and @class='btnPadraoSac']"))
        )
        # Click the button
        close_alert_button.click()
        work.log("Clicked the close alert button.")
    except Exception as e:
        work.log(f"Error clicking the close alert button: {e}")

def get_data(driver):
    n_tickets = []
    while True:
        try:
            
            # Wait until the table is loaded
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tListaSac")))

            # Get all rows in the tbody
            rows = driver.find_elements(By.XPATH, "//table[@id='tListaSac']/tbody/tr")
            
            # work.log(f"Found {len(rows)} rows.")
            if len(rows) <= 1:
                work.log("Não existe linhas na tabela.")
                _close_system_ticket()
                break
            
            for row in rows:
                # Get the link (first <a> element) in the row
                work.log(f"{len(n_tickets)} - {len(rows)}")  
                try: 
                    work.log(f'Entrou no for' )
                    # work.log(f"n_tickets  = {n_tickets}")
                    
                    link_element = row.find_element(By.XPATH, ".//a[contains(@href, 'conteudo=sac_ticketaberto')]")
                    href = link_element.get_attribute("href")
                    
                    if href in n_tickets:
                        if len(rows) == len(n_tickets):
                            work.log("Todos os Tickets Foram Processados")
                            _close_system_ticket()
                            break
                        else:
                            continue
                        
                        
                    else: 
                        # Execute your function (e.g., open the link)
                        work.log(f"Processing: {href}")
                        
                        
                        driver.get(href)  # Navigate to the link
                        __alter_ticket(driver)  # Call the function to alter the ticket
                        n_tickets.append(href)
                        # Return to the main page or perform other necessary actions before the next iteration
                        driver.back()  # Go back to the previous page
                        
                        break  # Proceed to the next row
                      
                except Exception as e:
                    work.log(f"Ocorreu um erro no processo for row in rows: {e}")
                    if 'no such element'.lower() in str(e):
                        break
                
        except Exception as e:
            work.log(f"Ocorreu um erro no laço de repetição while: {e} \n {e.__traceback__} \n {e.__cause__} \n {e.__context__} ")
            continue


def main():
    driver = open_browser()
    driver.get(URL)
    if login(driver):
        work.log("Login success")
        sleep(TIME_SLEEP)
        if not check_div_exists(driver, "modal-chamados-vinculados-id"):
            # _set_filter_ticket(driver)
            get_data(driver)
        else:
            group = _group_ticket(driver)
            if group:
                # _set_filter_ticket(driver)
                get_data(driver)    
    else:
        work.log("Login failed")
    driver.quit()

    
if __name__ == "__main__":
    # get_data()  # Call the function to get the data
    main() # Call the main function
    # a = generate_text_close_ticket()
    # work.log(a)
      