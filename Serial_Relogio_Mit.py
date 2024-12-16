###################################
# Autor: Davi Fuhr
# Propriedade Tecsistel Sistemas Eletrônicos Ltda
###################################
import serial
import os

#carrega as informações de porta serial e baud_rate(9600)
def carregar_configuracao():
    config_path = "C:\desenvolvimento\relogcomp\config.txt"
    if not os.path.exists(config_path):
        raise FileNotFoundError("Arquivo de configuração 'config' não encontrado.")

    with open(config_path, "r") as f:
        lines = f.readlines()

    config = {}
    for line in lines:
        key, value = line.strip().split("=", 1)
        config[key.strip()] = value.strip()

    porta = config.get("porta", "COM1")
    baud_rate = int(config.get("baud_rate", 9600))
    return porta, baud_rate

#formata a resposta recebida
def formatar_resposta(response):
    if len(response) >= 12:
        return response[-10:]
    else:
        return None

def enviar_comando(ser, comando):
    ser.write(comando.encode('utf-8') + b'\r')

def receber_resposta(ser):
    return ser.readline().decode('utf-8').strip()

def registrar_evento(evento):
    with open("log_eventos.txt", "a") as log_file:
        log_file.write(evento + "\n")

def main():
    try:
        # carrega as configurações da porta serial
        porta, baud_rate = carregar_configuracao()
        with serial.Serial(porta, baud_rate, timeout=1) as ser:
            registrar_evento(f"Conexão iniciada em {porta} a {baud_rate} bps.")

            aguardando_resposta = False
            comando = None

            while True:
                if not aguardando_resposta:
                    comando = input()
                    if comando.lower() == 'e':  # encerra o programa
                        registrar_evento("Programa encerrado pelo usuário.")
                        break
                    elif comando in ["1", "V"]: # comandos válidos -> apenas '1' e 'V'
                        enviar_comando(ser, comando)
                        registrar_evento(f"Comando enviado: {comando}")
                    else: # comando inválido
                        registrar_evento(f"Comando inválido: {comando}")
                    
                    aguardando_resposta = True
                else:
                    response = receber_resposta(ser)
                    if not response:  # timeout ou resposta vazia
                        registrar_evento("Nenhuma resposta recebida.")
                    elif comando == "V":
                        registrar_evento(f"Número de Série Recebido: {response}")
                    else:
                        resposta_formatada = formatar_resposta(response)
                        if resposta_formatada:
                            registrar_evento(f"Deformação Lida: {resposta_formatada}")
                        else:
                            registrar_evento("Deformação inválida ou insuficiente.")
                    aguardando_resposta = False

    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except serial.SerialException as e:
        registrar_evento(f"Erro na comunicação serial: {e}")
    except KeyboardInterrupt:
        registrar_evento("Interrupção pelo usuário.")
    except Exception as e:
        registrar_evento(f"Erro inesperado: {e}")
    finally:
        registrar_evento("Programa finalizado.")

if __name__ == "__main__":
    main()