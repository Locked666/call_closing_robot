import os 
import sys
FILE_TEXT = 'text_for_close.txt'

text = [
]

def create_file_text():

    if not os.path.exists(FILE_TEXT):
        with open(FILE_TEXT, "w", encoding="UTF8") as file:
            default_texts = [
                """Realizado o procedimento conforme a demanda necessária, informado o cliente das devidas necessidades.""",
                """Conforme a necessidade do cliente, foram realizados os procedimentos necessários e o cliente foi informado.""",
                """Procedimentos realizados conforme solicitado pelo cliente, todas as informações foram devidamente repassadas.""",
                """A demanda do cliente foi atendida e os procedimentos necessários foram executados, cliente informado.""",
                """Os procedimentos foram realizados conforme solicitado e o cliente foi informado sobre todas as etapas.""",
                """Atendemos a solicitação do cliente e realizamos os procedimentos necessários, cliente ciente das ações.""",
                """Procedimentos realizados conforme a demanda do cliente, todas as informações foram devidamente comunicadas.""",
                """Realizamos os procedimentos necessários conforme solicitado pelo cliente e informamos sobre as ações tomadas.""",
                """A demanda do cliente foi atendida com sucesso e todas as informações foram repassadas conforme necessário.""",
                """Os procedimentos necessários foram realizados conforme a solicitação do cliente e todas as informações foram comunicadas.""",
                """A solicitação do cliente foi atendida de acordo com os procedimentos exigidos e o cliente foi devidamente informado.""",
                """Procedimentos realizados conforme a demanda do cliente, todas as etapas cumpridas e o cliente informado.""",
                """Os procedimentos foram realizados conforme solicitado pelo cliente, com todas as informações repassadas e esclarecidas.""",
                """Atendemos à solicitação do cliente, executando todos os procedimentos necessários e informando-o adequadamente.""",
                """A demanda do cliente foi atendida conforme solicitado, com a execução dos procedimentos e comunicação clara.""",
                """Realizamos os procedimentos necessários conforme as orientações do cliente e garantimos que ele fosse informado.""",
                """Os procedimentos foram realizados conforme a solicitação do cliente, com as devidas explicações fornecidas.""",
                """O cliente foi informado adequadamente sobre os procedimentos executados conforme a solicitação dele.""",
                """Realizamos as ações solicitadas pelo cliente, com todos os procedimentos executados e as informações necessárias repassadas.""",
                """Os procedimentos necessários foram realizados conforme as demandas do cliente e a comunicação foi clara e objetiva.""",
            ]
            for text_line in default_texts:
                file.write(text_line + "\n")
            text.extend(default_texts)

def get_text():
    create_file_text()
    with open(FILE_TEXT, "r", encoding="UTF8") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() and not line.startswith("#"):
                text.append(line.strip())    
    return text

def get_text_and_row():
    create_file_text()
    rows = []
    with open(FILE_TEXT, "r", encoding="UTF8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith("#"):
                rows.append((i + 1, line.strip()))
    return rows

def edit_text_row(row, text):
    
    with open(FILE_TEXT, "r", encoding="UTF8") as file:
        lines = file.readlines()
    
    if 0 < row <= len(lines):
        new_text = text.strip()
        if not new_text:
            raise ValueError("O texto não pode ser vazio.")
        if new_text.startswith("#"):
            raise ValueError("O texto não pode começar com '#'.")
        if new_text in [line.strip() for line in lines]:
            raise ValueError("O texto já existe na lista.")
        
        lines[row - 1] = new_text + "\n"
        
        with open(FILE_TEXT, "w", encoding="UTF8") as file:
            file.writelines(lines)
        return f"Texto na linha {row} editado com sucesso."
    else:
        return f"Linha {row} inválida. Deve estar entre 1 e {len(lines)}."

def insert_text_row(text):
    
    with open(FILE_TEXT, "a", encoding="UTF8") as file:
        new_text = text.strip()
        if not new_text:
            raise ValueError("O texto não pode ser vazio.")
        if new_text.startswith("#"):
            raise ValueError("O texto não pode começar com '#'.")
        if new_text in get_text():
            raise ValueError("O texto já existe na lista.")
        
        file.write(new_text + "\n")
    return f"Texto '{new_text}' adicionado com sucesso."

def delete_text_row(row):
    
    with open(FILE_TEXT, "r", encoding="UTF8") as file:
        lines = file.readlines()
    
    if 0 < row <= len(lines):
        del lines[row - 1]
        
        with open(FILE_TEXT, "w", encoding="UTF8") as file:
            file.writelines(lines)
        return f"Linha {row} deletada com sucesso."
    else:
        return f"Linha {row} inválida. Deve estar entre 1 e {len(lines)}."

create_file_text()
if __name__=='__main__':
    print("\n\n\n\n")
    delete = delete_text_row(20)
    print(delete)
    print("\n\n\n\n")