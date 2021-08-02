# simpleCrm

Run project for linux:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 manage.py runserver
    
    
    попасть в админку: http://127.0.0.1:8000/admin
          user: user
      password: password
      
    В админке происходит управление служебными данными Clients, Employees, Orders
    у заказов присутствует фильтрация.
    
    Также реальзован telegram api.
        чтобы воспользоваться нужно при регистрации пользователя указать chat_id пользователя
        http://t.me/domClick_simpleCrmBot
