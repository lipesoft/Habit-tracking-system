from database import connect
from datetime import date

def log_habit(habit_id, status, log_date=None):
    if log_date is None:
        log_date = date.today().isoformat()
    
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO habit_logs (habit_id, log_date, status)
            VALUES (?, ?, ?)
        ''', (habit_id, log_date, status))
        
        conn.commit()
        print(f"Status '{status}' registrado para o hábito {habit_id} em {log_date}!")
    except Exception as e:
        print(f"Erro ao registrar progresso: {e}")
    finally:
        conn.close()

def get_habit_progress(habit_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT log_date, status 
        FROM habit_logs 
        WHERE habit_id = ? 
        ORDER BY log_date DESC
    ''', (habit_id,))
    
    logs = cursor.fetchall()
    conn.close()
    return logs

if __name__ == "__main__":
    habit_id_teste = 1
    
    log_habit(habit_id_teste, "completed")
    
    log_habit(habit_id_teste, "completed", "2023-10-25")

    print(f"\nHistórico do Hábito {habit_id_teste}:")
    historico = get_habit_progress(habit_id_teste)
    for log in historico:
        print(f"Data: {log[0]} | Status: {log[1]}")