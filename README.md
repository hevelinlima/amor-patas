# Bootcamp Back-end Python e Django

## Projeto Final: AMOR & PATAS - Sistema de gerenciamento de um abrigo para animais  

<p align="center">
  <img alt="Página inicial do site do abrigo Amor & Patas" src=".github/preview.jpeg" width="100%">
</p>

<p>
  AMOR & PATAS foi construído como um sistema de gerenciamento de abrigo para animais, permitindo o cadastro de espécies, raças, portes e gêneros e por fim de animais, e também o cadastro de colaboradores do abrigo (voluntários e cuidadores), estes cadastros são realizados apenas por um administrador. Na aplicação aberta ao público estão as páginas de início, a lista de animais disponíveis para adoção, uma breve apresentação dos colaboradores do abrigo e a página de contatos que permite enviar uma mensagem/dúvida para os responsáveis pelo abrigo. Já aos usuários logados é permitido fazer a solicitação de adoção de um dos animais cadastrados a partir de um formulário, o usuário também pode acompanhar o status da sua solicitação. O cadastro pode ser realizado por qualquer pessoa interessada, sinta-se à vontade. Mas tenha em mente que este é um site fictício realizado a fim de aprendizado.
</p> 

## Tecnologias Utilizadas

Esse projeto foi desenvolvido com as seguintes tecnologias:

- HTML e CSS
- Bootstrap
- Git e Github
- Python
- Framework Django

## Projeto

AMOR & PATAS é um site de um abrigo para animais.

- [Acesse o site aqui!](https://hevelinmiranda.pythonanywhere.com/)


<br>
<strong>
  PS: TODAS AS INFORMAÇÕES CONTIDAS NESTE SITE SÃO FICTÍCIAS!
</strong> 

## Execução do projeto

Para executar o projeto em sua máquina, siga os passos a seguir:

- Passo 1: Certifique-se de ter o Git instalado no seu sistema. Se não tiver, você pode baixá-lo e instalá-lo a partir do site oficial do Git: https://git-scm.com/.
  
- Passo 2: Clone este repositório
  
```bash
git clone <https://github.com/hevelinlima/amor-patas.git>
```

- Passo 3: Instale o django 
```bash
pip install django
```

- Passo 4: Instale as dependências do projeto
```bash
pip install -r requirements.txt
```

- Passo 5: Execute as migrações
```bash
python manage.py migrate
```

- Passo 6: Execute o servidor de desenvolvimento
```bash
python manage.py runserver
```
 
O servidor iniciará na porta 8000 por padrão. Abra um navegador da web e acesse este endereço (http://127.0.0.1:8000/) para ver o aplicativo Django em ação.

Agora que você clonou com sucesso o repositório do GitHub e configurou seu aplicativo Django localmente, você pode fazer alterações, desenvolver novos recursos e contribuir de volta para o repositório original quando estiver pronto.
