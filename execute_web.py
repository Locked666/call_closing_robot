from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException,WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager # Import the Edge driver manager
from PySide6.QtCore import QObject, Signal
from datetime import datetime
from time import sleep, time
import platform
import os
import tempfile
# import os 
import sys
from text_for_close import get_text
from random import choice, randint
from dotenv import dotenv_values

# text = get_text()  # Import the text from the text_for_close module

config = dotenv_values(".env")


# Load environment variables
URL = config['URL_INIT']
USERNAME = config['MY_SECRET_USERNAME']
PASSWORD = config['MY_SECRET_PASSWORD']
try:
    MODE_DEBUG = config['MODE_DEBUG'] == 'True'  # Convert string to boolean
except KeyError:
    MODE_DEBUG = False
    
TIME_SLEEP = 9



class WorkerLogger(QObject):
    """
    Classe simples para substituir os work.logs e enviar mensagens para a UI
    """
    log_signal = Signal(str)  # Sinal que será conectado à UI
    
    def log(self, message):
        """Método para log que substitui o work.log"""
        self.log_signal.emit(str(message))
        
    def __call__(self, message):
        """Permite usar a instância como função"""
        self.log(message)

# Cria uma instância global que será usada no lugar dos work.logs
work = WorkerLogger()



def finished_driver():
    global driver
    try:
        if driver is not None:
            driver.quit()
            work.log("Navegador encerrado corretamente")
            driver = None
    except Exception as e:
        work.log(f"Ocorreu um erro ao finalizar o driver: {e}")
    finally:
        _close_system_ticket()


def _close_system_ticket():
    sys.exit(0)

def open_browser():
    def build_options(user_data_dir=None):
        options = Options()
        if user_data_dir:
            options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_argument("--disable-features=EdgeSignin")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return options

    # Detecta se está rodando em .exe (PyInstaller)
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):  # Quando compilado com PyInstaller
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.abspath(relative_path)

    # Determina qual driver usar com base na arquitetura
    arch = platform.architecture()[0]
    if arch == '32bit':
        driver_path = resource_path("utils/edgedriver_win32/msedgedriver.exe")
    else:
        driver_path = resource_path("utils/edgedriver_win64/msedgedriver.exe")

    try:
        work.log("Iniciando Edge sem perfil personalizado...")
        s = Service(driver_path)
        driver = webdriver.Edge(service=s, options=build_options())
        return driver

    except WebDriverException as e:
        if "user data directory is already in use" in str(e):
            work.log("Perfil padrão está em uso. Tentando com perfil temporário...")
            temp_profile = tempfile.mkdtemp()
            driver = webdriver.Edge(service=s, options=build_options(user_data_dir=temp_profile))
            return driver
        else:
            work.log(f"Erro ao iniciar o Edge: {e}")
            raise e



# Correção de fora de area
# def open_browser():
#     def build_options(user_data_dir=None):
#         options = Options()
#         if user_data_dir:
#             options.add_argument(f"--user-data-dir={user_data_dir}")
#         options.add_argument("--disable-features=EdgeSignin")
#         options.add_argument("--disable-gpu")
#         options.add_argument("--headless")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#         return options

#     try:
#         # Tentativa sem perfil customizado
#         work.log("Iniciando Edge sem perfil personalizado...")
#         s = Service(EdgeChromiumDriverManager().install())
#         driver = webdriver.Edge(service=s, options=build_options())
#         return driver

#     except WebDriverException as e:
#         if "user data directory is already in use" in str(e):
#             work.log("Perfil padrão está em uso. Tentando com perfil temporário...")
#             temp_profile = tempfile.mkdtemp()
#             driver = webdriver.Edge(service=s, options=build_options(user_data_dir=temp_profile))
#             return driver
#         else:
#             raise e   

# def open_browser():
#     # Set the path to the edgedriver
  
    
    # Set the options for the edgedriver
    # edge_options = Options()
    # temp_profile = tempfile.mkdtemp()
    # print("\n\n\n\n")
    # print(temp_profile)
    # print("\n\n\n\n")
    
    # # 1. Cria um diretório temporário único
    # edge_options.add_argument(f"--user-data-dir={temp_profile}")
    # edge_options.add_argument("--disable-features=EdgeSignin")
    # edge_options.add_argument("--disable-logging")
    # edge_options.add_argument("--log-level=3")
    # edge_options.add_argument("--disable-gpu")
    # edge_options.add_argument("--headless")
    # edge_options.add_argument("--no-sandbox")
    # edge_options.add_argument("--disable-dev-shm-usage")
    

    # s = Service(EdgeChromiumDriverManager().install())
    # driver = webdriver.Edge(service=s, options=edge_options)
    # return driver

def generate_text_close_ticket():
    text = get_text()  # Import the text from the text_for_close module
    return choice(text)


def login(driver):
    try :
        if not URL:
            work.log("URL não definida. Verifique na tela de configurações")
            return False
        if not USERNAME or not PASSWORD:
            work.log("Credenciais não definidas. Verifique na tela de configurações")
            return False
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
        work.log(f"Ocorrou um erro ao fazer login: {e}")
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
        work.log("Agrupando tickets")
        # Wait until the modal is present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal-chamados-vinculados-id")))
        
        # Find all buttons with IDs starting with "btagrup_"
        buttons = driver.find_elements(By.XPATH, "//a[starts-with(@id, 'btagrup_')]")
        
        for button in buttons:
            try:
                # Click the button
                button.click()
                # work.log(f"Clicked button with ID: {button.get_attribute('id')}")
                
                # Handle any alerts that may appear
                __handle_alert(driver)
                
                # Wait for a short period to ensure the action is completed
                sleep(1)
            except Exception as e:
                work.log(f"Ocorreu um erro ao agupar tickets {button.get_attribute('id')}: {e}")
                continue
        click_close_alert_button(driver)
        return True    
    except Exception as e:
        work.log(f"Error in _group_ticket: {e}")

def __handle_alert(driver):
    try:
        # Espera até o alerta ser presente
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        
        # Troca para o alerta
        alert = Alert(driver)
        
        # Clica no botão "OK" (ou similar) no alerta
        alert.accept()
        # work.log("Alerta tratado com sucesso.")
        
    except Exception as e:
        work.log(f"Ocorreu um erro ao tratar alerta: {e}")

# Verificar a quantidade de linhas na tabela 
def check_table_has_rows(driver):
    try:
        # Wait until the table is loaded
        sleep(TIME_SLEEP)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tListaSac")))

        # Get all rows in the tbody
        try: 
            rows = driver.find_elements(By.XPATH, "//table[@id='tListaSac']/tbody/tr")
        except StaleElementReferenceException:
            # Re-fetch the rows if the reference is stale
            rows = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[8]/table") 
             

        # work.log(f"Found {len(rows)} rows.")
        
        if len(rows) > 1:
            # work.log("Existe Linhas na tabela.")
            return True
        else:
            # work.log("Não existe linhas na tabela.")
            return False
    except Exception as e:
        work.log(f"Ocorreu um erro ao verificar linhas da tabela:\n Funcão (check_table_has_rows)\n {e}")
        return False

# Acessar a aba de chamados vinculados
def access_linked_tickets_tab(driver):
    try:
        # Check if the div exists
        if check_div_exists(driver, "boxAbasChamados"):
            # Click on the "chamados vinculados" tab
            linked_tickets_tab = driver.find_element(By.XPATH, "//a[@href=\"javascript:trocaAbaChamados('chamado');\" and @id='btAbaChamTic']")
            linked_tickets_tab.click()
            work.log("Verificando na aba Chamados Vinculados.")
            
            # Check if the table has rows
            return check_table_has_rows(driver)
        else:
            work.log("Não existe chamados vinculados")
            return False
    except Exception as e:
        work.log(f"Ocorreu um erro ao verificar a aba chamados vincualados:\n {e}")
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

def __execute_preencimento(driver):
    
    try: 
        work.log("\nPreenchendo informações do ticket")
        
        ## # Verifica se Existe o elemento cSistema
        try:
            sistema_select_sistema = Select(driver.find_element(By.ID, "cSistema"))
            # Pega todos os elementos <option> do <select>
            options = sistema_select_sistema.options

            # Cria uma lista com os values de cada option
            values_in_select_cSistema = [option.get_attribute("value") for option in options]
            
            # Try to select by value
            sistema_select_sistema.select_by_value(__randon_system_closed(values_in_select_cSistema))
        except NoSuchElementException:
            work.log("\nO elemento 'cSistema' não foi encontrado.")
                
        
        
        
        # 2. Check if "cResponsavel" is empty; if so, set it to the first option
        try:
            responsavel_select = Select(driver.find_element(By.ID, "cResponsavel"))
            if responsavel_select.first_selected_option.get_attribute("value") == "0":  # If "responsável" is selected
                responsavel_select.select_by_index(1)  # Select the first available option
        except NoSuchElementException:
            work.log("\nO elemento 'cResponsavel' não foi encontrado.")
                    
        
        # 3. Set "sPrevisao" to the current date in "dd/mm/yyyy" format
        try:
            previsao_input = driver.find_element(By.ID, "sPrevisao")
            current_date = datetime.now().strftime("%d/%m/%Y")
            previsao_input.clear()  # Clear any existing value
            previsao_input.send_keys(current_date)  # Set the current date
        except NoSuchElementException:
            work.log("\nO elemento 'sPrevisao' não foi encontrado.")
            return
                
        
        # 4. Click the "Salvar" button
        try:
            update_ticket_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btAtualizar"))
            )
            update_ticket_button.click()  
            
            __handle_alert(driver)
        except NoSuchElementException:
            work.log("\nO botão 'btAtualizar' não foi encontrado.")
            return   
        
    except ValueError as e:
        
        if MODE_DEBUG: 
            work.log(f"Ocorreu um erro na função(__execute_preencimento) first tray : {e} \n  ")
        else: 
            work.log(f"Ocorreu um erro na função(__execute_preencimento): {e}\n ")
    
    
## Method to alter ticket after close
def __alter_ticket(driver):
    work.log("Alterando ticket")
    sleep(TIME_SLEEP)
    
    try:
        # 1. Set "cSistema" to the value "5"
        
        # Wait until the element is loaded
        if check_div_exists(driver, "boxAbasChamados"):
            # Click on the "chamados vinculados" tab
            access_linked_tickets_tab(driver)
            if check_table_has_rows(driver):
                # Check if the title attribute of the specified element is "encerrado"
                try:
                    element = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[8]/table/tbody/tr[2]/td[9]")
                    if element.get_attribute("title").lower() == "encerrado":
                        work.log("O chamado já está encerrado.")
                        __execute_preencimento(driver)
                    else : 
                        work.log("Existe chamados vinculados, mas não estão encerrados.")
                        return    
                except Exception as e:
                    work.log(f"Erro ao verificar o título do elemento: {e}")
                    return
            else:
                work.log("Não existe linhas na tabela.")
                __execute_preencimento(driver) 
                
        else :
            try: 
                __execute_preencimento(driver)
            except Exception as e:
                work.log(f"Ocorreu um erro ao executar o preenchimento do ticket : {e}")
                return                
            
        try:    
            __close_ticket(driver)
        except Exception as e:
            work.log(f"Ocorreu um erro ao fechar o ticket: {e}")
            return    
    
    except ValueError as e:
        if MODE_DEBUG: 
            work.log(f"Ocorreu um erro na função(__alter_ticket) principal : {e} \n ") 
        else:    
            work.log(f"Ocorreu um erro na função(__alter_ticket) principal.  ")
         
    
    # driver.quit()

#   method to close ticket
def __close_ticket(driver):
    sleep(TIME_SLEEP)
    try:
        # clicked bnt close ticket
        close_ticket_button = WebDriverWait(driver, TIME_SLEEP).until(
            EC.element_to_be_clickable((By.ID, "btAtribuir"))
        )
        close_ticket_button.click()
        
    except Exception as e:
        work.log(f"Ocorreu um erro ao clicar no botão de encerrar: {e}")      

    try:
        # Espera até que o estilo de display da div não seja 'none'
        WebDriverWait(driver, TIME_SLEEP).until(
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
        work.log(f"Ocorreu um erro na funcção (__close_ticket): {e} \n  ")

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
        # work.log("Clicked the close alert button.")
    except Exception as e:
        work.log(f"Error clicking the close alert button: {e}")

def get_data(driver):
    n_tickets = []
    first_ex = 0
    while True:
        try:
            
            # Wait until the table is loaded
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tListaSac")))

            # Get all rows in the tbody
            rows = driver.find_elements(By.XPATH, "//table[@id='tListaSac']/tbody/tr")
            if first_ex == 0:
                first_ex = int(len(rows))
            
            # work.log(f"Found {len(rows)} rows.")
            if len(rows) <= 1:
                work.log("Não existe tickets a serem executados")
                _close_system_ticket()
                break
            
            for row in rows:
                 
                try:       
                                  
                    link_element = row.find_element(By.XPATH, ".//a[contains(@href, 'conteudo=sac_ticketaberto')]")
                    href = link_element.get_attribute("href")
                    
                    if href not in n_tickets:
                        work.log("-------------------------------------------------------------------")
                        work.log(f"Total: {first_ex} - Executado: {len(n_tickets)} - Restante: {first_ex - len(n_tickets)}\n")
                        work.log("-------------------------------------------------------------------")  

                        work.log(f"Processando: {href}")

                        driver.get(href)  # Navigate to the link
                        __alter_ticket(driver)  # Call the function to alter the ticket
                        n_tickets.append(href)
                        
                        driver.back()  # Go back to the previous page
                        
                        _set_hundred_page(driver)
                        
                        break  # Proceed to the next row

                    else:
                        
                        if first_ex <= len(n_tickets):
                            work.log("Todos os Tickets Foram Processados")
                            _close_system_ticket()  # Close the system if all tickets are processed
                            break
                        else:
                            continue
                        
                except Exception as e:
                    work.log(f"Ocorreu um erro no processo for row in rows: {e}")
                    if 'no such element'.lower() in str(e):
                        break
                
        except Exception as e:
            work.log(f"Ocorreu um erro no laço de repetição while: {e} \n  ")
            continue

def _set_hundred_page(driver):
    try: 
        
        value_page_exist = Select(driver.find_element(By.NAME, 'tListaSac_length'))
        value_page_exist.select_by_index(3)
        sleep(TIME_SLEEP)
    except  Exception as e: 
        work.log(f" Ocorreu um erro ao realizar  a função de mudar a quantidade de paginas: {e} \n {e.__cause__}")


def main():
    try:
        driver = open_browser()
        driver.get(URL)
        
        if login(driver):
            work.log("Sucesso ao realizar Login")
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
            work.log("Login failed")
            
        driver.quit()
        
    except Exception as e:
        work.log(f"Ocorreu um erro na função main: {e} \n\n  ")
        driver.quit() 
         # Ensure the driver is terminated in case of an error
    
    finally:
        if 'driver' in locals():
            driver.quit()
            work.log("Navegador encerrado corretamente")       


    
if __name__ == "__main__":

    # main() # Call the main function
    open_browser()  # Open the browser to test the function

      