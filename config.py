import os 
import configparser
from pathlib import Path


global PATH_DATABASE
global PATH_CONFIG_INI 
global USERNAME_INI
global PASSWORD_INI
global SELECT_THEMA_INI
global MODE_DEBUG
global __version__
global URL_INI


__version__= '1.0.0.0'
PATH_CONFIG_INI = 'config.ini'

MODE_DEBUG = False




## arquivo ini ###
config = configparser.ConfigParser()
settings_sec =  {
    'username':'',
    'password':'',
    'thema':'',
}

database_sec= {
    'host': 'localhost',
    'port': '3306',
    'database': fr'{os.path.join(Path(__file__).parent,'database','database.db')}'
}

# Verificando a existencia do config
if not os.path.exists(PATH_CONFIG_INI):
    config['Settings'] = settings_sec
    config['Database'] = database_sec
    with open(PATH_CONFIG_INI, 'w') as configfile:
        config.write(configfile)

config.read(PATH_CONFIG_INI)

def complement_ini(session:str = '', line:str = '', new_info = ''):
    # Modifica os valores desejados

    try:
        config[session][line] = new_info 
    # Salva as alterações de volta no arquivo
        with open(PATH_CONFIG_INI, 'w') as configfile:
            config.write(configfile)

        return f"Sessão {session} linha {line} informação {new_info}"    
    
    except ValueError as e:
        return f'Ocorreu ao executar a função\n {e}'



PATH_DATABASE = config['Database']['database']
USERNAME_INI = config['Settings']['username']
PASSWORD_INI = config['Settings']['password']

if not config.has_option('Settings', 'thema'):
    config.set('Settings', 'thema', 'dark')
    with open(PATH_CONFIG_INI, 'w') as configfile:
        config.write(configfile)

SELECT_THEMA_INI = config['Settings']['thema']


if __name__=='__main__':
    # complement_ini('Settings', 'username', 'oiiii')
    print(SELECT_THEMA_INI)
    pass