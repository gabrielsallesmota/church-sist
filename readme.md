# Church CAD

O Church CAD é um sistema de cadastro de membros e ministérios para igrejas. Ele permite que você mantenha um registro organizado dos membros da igreja, suas informações pessoais e seus ministérios de atuação. 

Ele foi desenvolvido a fim acadêmico pelos alunos Jéssica Becaro Janardi Mota e Gabriel Salles Mota, do curso de Pós Graduação em Engenharia de Software da PUC Minas.

## Protótipo Navegável

Um protótipo navegável do Church CAD pode ser visualizado [aqui](https://drive.google.com/file/d/1iI_JcyJSNRt-harTpCjV5z0Z_XKPJutK/view?usp=sharing).

## Recursos

- Cadastro de membros: Adicione e gerencie os membros da igreja, incluindo informações como nome, data de nascimento, email, telefone, entre outros.
- Cadastro de ministérios: Crie e gerencie os ministérios da igreja, atribuindo líderes e membros a cada ministério.
- Consulta de membros: Realize consultas personalizadas para encontrar membros específicos com base em critérios como nome, idade, ministério de atuação, entre outros.
- Edição e exclusão de membros: Atualize as informações dos membros ou remova membros do sistema.
- Edição e exclusão de ministérios: Faça alterações nos detalhes dos ministérios ou exclua ministérios existentes.
- Relatórios: Obtenha relatórios sobre os membros da igreja e os ministérios ativos.

## Pré-requisitos

- Python (versão 3.11.3)
- Django (versão 4.2.1)

## Instalação

1. Clone o repositório do Church CAD: `git clone https://github.com/gabrielsallesmota/church-cad.git`
2. Acesse o diretório do projeto: `cd church-cad`
3. Instale as dependências do Python: `pip install -r requirements.txt`
4. Execute as migrações do banco de dados: `python manage.py migrate`
5. Inicie o servidor local: `python manage.py runserver`
6. Acesse o Church Sist em seu navegador: `http://localhost:8000`