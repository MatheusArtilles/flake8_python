from typing import Union

from constantes import CODIGO_PRIORITARIO, CODIGO_NORMAL
from fila_normal import FilaNormal
from fila_prioridade import FilaPrioritaria



class FabricaFila:

    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == CODIGO_NORMAL:
            return FilaNormal()
        elif tipo_fila == CODIGO_PRIORITARIO:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila inválida!')
