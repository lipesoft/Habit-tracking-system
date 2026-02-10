from database import connect

def add_user(name, email):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        
        conn.commit()
        print(f"Usuário '{name}' cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        conn.close()

def list_users():
    """Retorna todos os usuários cadastrados."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

if __name__ == "__main__":
    add_user("Filipe", "filipe@teste.com")

    print("\nLista de Usuários:")
    users = list_users()
    if users:
        for user in users:
            print(f"ID: {user[0]} | Nome: {user[1]} | Email: {user[2]}")
    else:
        print("Nenhum usuário encontrado.")