# Verificador de Status de Ordem de Serviço iPlace

Eu fiz esse script para verificar o status de uma ordem de serviço na iPlace. Ele notifica o status da ordem de serviço via uma notifação do Windows.

Coloquei o script para rodar de manhã, meio-dia e noite, através do `Agendador de Tarefas do Windows`, mas você pode adaptar para rodar nos horários que você quiser.

## Como usar

1. Clone o repositório ou baixe o arquivo `main.py` e `requirements.txt` e coloque-os em uma pasta.
2. Abra o terminal na pasta e digite `pip install -r requirements.txt` para instalar as dependências.
3. Abra o arquivo `.env` e preencha com o número da sua ordem de serviço e CPF (sem pontos e traços).
4. Abra o `Agendador de Tarefas do Windows` e crie uma nova tarefa que roda o script com o comando `python main.py` nos horários que você desejar.

## Observações

- O script foi pensado para ser utilizado apenas em Windows, adapte a forma de notificação para o seu sistema operacional ou versão do Windows.
- Você pode executar o script dentro de um virtualenv, se preferir.
