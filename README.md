## Controle de estoque

### Como iniciar o projeto:

- Clone esse repositório
- Crie um virtual env com Python 3
- Instale as dependências (requirements.txt)
- Rode as migrações

Opcional:
Instale o **git-cola**, uma interface gráfica para usar o Git (você só precisa fazer o git-push via terminal)
```sh
sudo apt install git-cola
```

Exemplo:
```sh
git clone git@github.com:Siluryan/Django-Estoque.git
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```