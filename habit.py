from database import connect

def add_habit(user_id, title, description):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO habits (user_id, title, description) VALUES (?, ?, ?)",
            (user_id, title, description)
        )
        conn.commit()
        print(f"Hábito '{title}' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar hábito: {e}")
    finally:
        conn.close()

def list_habits(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, description FROM habits WHERE user_id = ?",
        (user_id,)
    )
    habits = cursor.fetchall()
    conn.close()
    return habits

if __name__ == "__main__":
    user_id_teste = 1
    
    add_habit(user_id_teste, "Beber 2L de Água", "Meta diária de hidratação")
    add_habit(user_id_teste, "Estudar Python", "30 minutos por dia no projeto guiado")

    print(f"\nHábitos do Usuário {user_id_teste}:")
    meus_habitos = list_habits(user_id_teste)
    for h in meus_habitos:
        print(f"ID: {h[0]} | Título: {h[1]} | Descrição: {h[2]}")