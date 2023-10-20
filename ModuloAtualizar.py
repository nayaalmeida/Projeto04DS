from mysql import connector
from mysql.connector import cursor
from ConexãoBD import conectar
import mysql.connector
from tkinter import messagebox 

def atualizar(cod_viagem, nome, cpf, local_orig, local_dest, pagamento, data):
    conexao, cursor = conectar()
    try:
        sqlAtualizar = f"""UPDATE tb_reserva
                        SET 
                        nome= '{nome}', 
                        cpf='{cpf}', 
                        local_orig='{local_orig}', 
                        local_dest='{local_dest}',
                        pagamento='{pagamento}',
                        data='{data}',
                        WHERE cod_viagem = '{cod_viagem}'
                        """
        cursor.execute(sqlAtualizar)
        conexao.commit()
        messagebox.showinfo("Atualizado","Atualização relizada!")
        return True

    except mysql.connector.Error as falha:
        messagebox.showerror("Falha","Falha ao atualizar!" + str(falha))
        return False

    finally:
        conexao.close()
        cursor.close()