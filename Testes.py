from ModuloAtualizar import atualizar
from ModuloDeletar import deletar
from ModuloCadastrar import reserva
from ModuloConsultar import consultar
from ModuloAtualizar import atualizar

#--------------TESTE ATUALIZAR--------------------------
# atualizar(2,"Aynoã Almeida","123.789.456-98","Brasil - Pe - Recife","Brasil - RJ - Paraty", 'Débito')

#--------------TESTE DELETAR--------------------------
#deletar(1)

#--------------TESTE CONSULTAR------------------------
# for item in consultar():
#     print("Nome: " + str (item[1]))
#     print("CPF: " + str (item[2]))
#     print("Local de origem: " + str (item [3]))
#     print("Local de destino: " + str (item[4]))
#     print("Pagamento: " + str (item[5]))
#     print("--------------------")


#--------------TESTE CADASTRAR/RESERVA----------------
# reserva("Aynoã Almeida","123.789.456-98","Brasil - Pe - Recife","Brasil - RJ - Jacarepaguá", 'pix')
# reserva("Caio Monteiro","456.789.654-98","Brasil - Pe - Garanhus","Brasil - Pe - Recife", "Crétido")
reserva("Carla Péricles","456.789.654-98","Brasil - Pe - Garanhus","Brasil - Pe - Recife", "Crétido","2023-12-12")