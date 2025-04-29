@echo off

REM Ativando o ambiente virtual
call venv\Scripts\activate.bat

REM Executando o script Python
python "execute_webcopy.py"

REM Pausa para visualizar qualquer mensagem ou saída

exit
