# Script de Comunicação Serial - Relógio Comparador

Este projeto é um script Python desenvolvido para se comunicar com um Relógio Comparador através de uma porta serial. Ele permite enviar comandos e registrar respostas, como leituras de deformação ou o número de série do equipamento, enquanto realiza o log de eventos relevantes para um arquivo de texto.

## Recursos

- **Configuração dinâmica da porta serial:**
  - O script carrega a configuração da porta serial e baud rate a partir de um arquivo `config.txt`.
- **Registro de eventos:**
  - Todos os eventos, incluindo comandos enviados, respostas recebidas e erros, são registrados no arquivo `log_eventos.txt`.
- **Envio de comandos e leitura de respostas:**
  - Comandos `1` e `V` são aceitos. O comando `V` retorna o número de série, enquanto o comando `1` retorna leituras formatadas.

## Estrutura do Projeto

```
.
├── config.txt          # Arquivo de configuração para porta serial e baud rate
├── log_eventos.txt     # Log de eventos gerado automaticamente pelo script
└── Serial_Relogio_Mit.py           # Script Python principal
```

## Arquivo de Configuração

O arquivo `config.txt` deve conter as seguintes chaves:

```
porta=COM4
baud_rate=9600
```

- **porta:** Define a porta serial utilizada.
- **baud_rate:** Define a taxa de comunicação.

## Como Executar

### 1. Configuração do Ambiente

- Certifique-se de ter o Python instalado.
- Instale o módulo `pyserial` (se ainda não estiver instalado):

  ```bash
  pip install pyserial
  ```

### 2. Configurar o Arquivo `config.txt`

- Edite o arquivo `config.txt` com as configurações adequadas para seu dispositivo.

### 3. Executar o Script

- No terminal, execute:

  ```bash
  python Serial_Relogio_Mit.py
  ```

- Comandos disponíveis durante a execução:
  - **`1`**: Envia o comando para leitura de deformação.
  - **`V`**: Envia o comando para leitura do número de série.
  - **`e`**: Encerra o programa.

## Logs

- Todos os eventos serão registrados no arquivo `log_eventos.txt`:
  - Comandos enviados
  - Respostas recebidas
  - Erros encontrados
  - Eventos gerais do programa

Exemplo de um log:

```
Conexão iniciada em COM4 a 9600 bps.
Comando enviado: V
Número de Série Recebido: 1ITN61003927
Comando enviado: 1
Deformação Lida: +0005.3525
Comando enviado: e
Programa encerrado pelo usuário.
```

## Tratamento de Erros

O script trata os seguintes erros:

1. **Arquivo de configuração não encontrado:**
   - Certifique-se de que o arquivo `config.txt` esteja no local correto.

2. **Problemas na conexão serial:**
   - Verifique se a porta especificada em `config.txt` está correta e disponível.

3. **Erros gerais:**
   - Qualquer exceção inesperada é registrada no arquivo de log.

## Autor

- **Davi Fuhr**
