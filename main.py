from constantes import CODIGO_NORMAL, CODIGO_PRIORITARIO
from fila_base import FilaBase
from fila_normal import FilaNormal
from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada
# fila_teste = Fila_Normal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(10))
# print(fila_teste.chama_cliente(6))
# fila_teste2 = FilaPrioritaria()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# print(fila_teste2.chama_cliente(5))
# print(fila_teste2.chama_cliente(6))
# print(fila_teste2.chama_cliente(8))
# print(fila_teste2.chama_cliente(9))
# fila_teste2.atualiza_fila()
# print(fila_teste2.chama_cliente(10))
# print(fila_teste2.estatistica('10/11/2002', 205, 'detail'))
# fila_teste1 = Fila_Normal()
# fila_teste1.atualiza_fila()
# print(fila_teste1.chama_cliente(2))
teste_fabrica_fila = FabricaFila.pega_fila(CODIGO_PRIORITARIO)
teste_fabrica_fila.atualiza_fila()
teste_fabrica_fila.atualiza_fila()
teste_fabrica_fila.atualiza_fila()
teste_fabrica_fila.atualiza_fila()
print(teste_fabrica_fila.chama_cliente(2))
print(teste_fabrica_fila.chama_cliente(3))
print(teste_fabrica_fila.chama_cliente(10))
print(teste_fabrica_fila.chama_cliente(8))
print(teste_fabrica_fila.estatistica(EstatisticaDetalhada('30/03/1960', 112)))
