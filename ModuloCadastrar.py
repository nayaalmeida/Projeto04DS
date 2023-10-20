from mysql import connector
from mysql.connector import cursor
from ConexãoBD import conectar
import mysql.connector
from tkinter import messagebox 

def reserva(nome, cpf, local_orig, local_dest, pagamento, data):
    conexao, cursor = conectar()
    try:
        sqlReserva = f"""INSERT INTO tb_reserva
        (nome, cpf, local_orig, local_dest, pagamento, data)
        VALUES
        ('{nome}', '{cpf}', '{local_orig}',
        '{local_dest}', '{pagamento}','{data}')
        """
        cursor.execute(sqlReserva)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Reserva efetuada com sucesso!")
        return True

    except mysql.connector.Error as falha:
        messagebox.showerror("Falha","Falha ao cadastrar" + str(falha))

    finally:
        conexao.close()
        cursor.close()    
