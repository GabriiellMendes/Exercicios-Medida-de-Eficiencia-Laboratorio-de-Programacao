import random


def conexao_mock(sempre_falha=False):
    if sempre_falha or random.random() < 0.7:
        raise ConnectionError("Falha na conexão com a API")
    return "Conexão realizada com sucesso"


def conectar_com_tentativas(sempre_falha=False):
    tentativas = 3

    for tentativa in range(1, tentativas + 1):
        try:
            resposta = conexao_mock(sempre_falha)
        except ConnectionError:
            print(f"Tentativa {tentativa} de {tentativas} falhou.")
        else:
            print(resposta)
            return resposta

    print("Falha: limite de 3 tentativas atingido. Encerrando com segurança.")
    return None


print("--- Conexão instável (aleatória) ---")
conectar_com_tentativas()

print("--- Conexão que sempre falha ---")
conectar_com_tentativas(sempre_falha=True)
