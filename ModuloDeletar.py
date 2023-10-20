from mysql import connector
from mysql.connector import cursor
from ConexãoBD import conectar
import mysql.connector
from tkinter import messagebox 

def deletar(cod_viagem):
    conexao, cursor = conectar()
    try:
        sqlDeletar = f"""DELETE FROM tb_reserva
                        WHERE cod_viagem ='{cod_viagem}'
                    """
        cursor.execute(sqlDeletar)
        conexao.commit()
        messagebox.showinfo("Deletado","Excluído com sucesso!")
        return True
    
    except mysql.connector.Error as falha: 
        messagebox.showerror ("Falha","Falha ao excluir" + str(falha))    
        return False

    finally:
        conexao.close()
        cursor.close()