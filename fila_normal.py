class Fila_Normal:
    codigo: int = 0
    fila = []
    clientesatendidos = []
    senha: str = ""

    def gera_senha_atual(self) -> None:
        self.senhaatual = f"NM{self.codigo}"

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.gera_senha_atual()
        self.reseta_fila()
        self.fila.append(self.senhaatual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')
