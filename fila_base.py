class FilaBase:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha: str = ""
    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1