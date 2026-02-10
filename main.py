import user
import habit
import habit_log
from database import create_tables

def menu():
    create_tables()

    while True:
        print("\n--- HABIT TRACKER SYSTEM ---")
        print("")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Criar Novo Hábito")
        print("4. Listar Meus Hábitos")
        print("5. Registrar Progresso (Check-in)")
        print("6. Ver Meu Histórico")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1" :
            nome = input("Nome: ")
            email = input("Email: ")
            user.add_user(nome, email)

        elif opcao == "2":
            usuarios = user.list_users()
            for u in usuarios:
                print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]}")

        elif opcao == "3":
            u_id = input("ID do Usuário: ")
            titulo = input("Título do Hábito: ")
            desc = input("Descrição: ")
            habit.add_habit(u_id, titulo, desc)

        elif opcao == "4":
            u_id = input("ID do Usuário: ")
            habitos = habit.list_habits(u_id)
            for h in habitos:
                print(f"ID: {h[0]} | Hábito: {h[1]}")

        elif opcao == "5":
            h_id = input("ID do Hábito: ")
            status = input("Status (completed / not_completed): ")
            habit_log.log_habit(h_id, status)

        elif opcao == "6":
            h_id = input("ID do Hábito: ")
            progresso = habit_log.get_habit_progress(h_id)
            for p in progresso:
                print(f"Data: {p[0]} | Status: {p[1]}")

        elif opcao == "0":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()