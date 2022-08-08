class Veiculo:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True
        return (f'Veículo placa {self.placa} estacionado')

    def sair_vaga(self):
        self.estacionado = False
        return (f'Veículo placa {self.placa} saiu da vaga.')


class Carro(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)


class Moto(Veiculo):
    def __init__(self, placa):
        super().__init__(placa)


class Vaga:
    def __init__(self, id, tipo, veiculo):
        self.id = id
        self.tipo = tipo
        self.livre = True
        self.placa = veiculo.placa

    def ocupar(self, veiculo = Veiculo):
        self.livre = False
        if self.tipo == 'moto':
            print(f'Moto placa {self.placa} ocupando vaga {self.id}')
        elif self.tipo == 'carro':
            print(f'Carro placa {self.placa} ocupando vaga {self.id}')

    def desocupar(self):
        self.livre = True
        return('saiu')



class Estacionamento:
    def __init__(self):
        self.vagas_carro = {
            "vaga 1C": None,
            "vaga 2C": None,
            "vaga 3C": None,
            "vaga 4C": None,
            "vaga 5C": None
        }
        self.vagas_moto = {
            "vaga 1M": None,
            "vaga 2M": None,
            "vaga 3M": None,
            "vaga 4M": None,
            "vaga 5M": None
        }
        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_moto = 5

    @property
    def total_vagas_carro(self):
        return self.total_vagas_livres_carro

    @total_vagas_carro.setter
    def total_vagas_carro(self, numero):
        self.total_vagas_livres_carro = numero

    @property
    def total_vagas_moto(self):
        return self.total_vagas_livres_moto

    @total_vagas_moto.setter
    def total_vagas_moto(self, numero):
        self.total_vagas_livres_moto = numero

 
    def estacionar(self, veiculo):
        opcao = str(input('Carro (C) ou Moto (M): ')).upper()
        if opcao == "C":
            if self.total_vagas_carro > 0:
                for chave in self.vagas_carro.keys():
                    if self.vagas_carro[chave] is None:
                        print("- "*10)
                        print("Estacionando carro placa " + veiculo.placa)
                        self.vagas_carro[chave] = veiculo
                        self.total_vagas_livres_carro -=1
                        print("Carro estacionado na " + chave)
                        break
            else:
                print('Não há mais vagas de carro disponíveis!')
                print('-'*10)
                    
        elif opcao == "M":
            if self.total_vagas_moto > 0:
                for chave in self.vagas_moto.keys():
                    if self.vagas_moto[chave] is None:
                        print("Estacionando moto placa " + veiculo.placa)
                        self.vagas_moto[chave] = veiculo
                        self.total_vagas_livres_moto -= 1
                        print("Moto estacionada na " + chave)
                        break
            else: 
                print('Não há mais vagas de moto disponíveis!')
                mudar = str(input('Deseja estacionar na vaga de carro?\n(S) sim\n(N) não\n')).upper()
                if mudar == 'S':
                    for chave in self.vagas_carro.keys():
                        if self.vagas_carro[chave] is None:
                            print("Estacionando moto placa " + veiculo.placa)
                            self.vagas_carro[chave] = veiculo
                            self.total_vagas_livres_carro -=1
                            print("Moto estacionada na " + chave)
                            break
                    else:
                        print('Não há mais vagas disponíveis no estacionamento!')
                        print('-'*10)

        else:
            print('Opção de veículo inválida.')
            print('-'*10)

    def remover(self, placa):
            opcao = str(input('Carro (C) ou Moto (M): ')).upper()
            if opcao == "C":
                for chave in self.vagas_carro.keys():
                    if self.vagas_carro[chave] is not None:
                        if self.vagas_carro[chave].placa == placa:
                            print("Removendo carro placa " + placa)
                            self.vagas_carro[chave] = None
                            self.total_vagas_livres_carro += 1
                            print(self.vagas_carro)
                            break
                        
                        else:
                            print('Placa informada não encontrada!')
                            print('-'*10)

    
            elif opcao == "M":
                for chave in self.vagas_moto.keys():
                    if self.vagas_moto[chave] is not None:
                        if self.vagas_moto[chave].placa == placa:
                            print("Removendo carro placa " + placa)
                            self.vagas_moto[chave] = None
                            self.total_vagas_livres_moto += 1
                            print(self.vagas_moto)
                            break

                        else:
                            print('Placa informada não encontrada!')
                            print('-'*10)

def estacionar(estacionamento):
    placa = str(input('Entre com a placa: '))
    novo_veiculo = Veiculo(placa)
    estacionamento.estacionar(novo_veiculo)

def estado_do_estacionamento(estacionamento):
    print('--- Ocupação atual:---')
    print(f'Vagas de carro disponíveis: {estacionamento.total_vagas_carro}')
    print(f'Vagas de moto disponíveis: {estacionamento.total_vagas_moto}')
    print('-'*10)


def remover(estacionamento):
    placa = str(input('Entre com a placa  que deseja remover: '))
    estacionamento.remover(placa)

def mostra_menu():
    menu_options = {
        1: 'Estacionar',
        2: 'Remover',
        3: 'Listar',
        4: 'Sair',
    }
    mensagem = 'Bem vindo !Digite a opção desejada'


if __name__ == '__main__':
    estacionamento = Estacionamento()
    print('* '*10)
    print('Bem vindo ao Parking Estacionamento!')
    print('* '*10)

    while (True):
        mostra_menu()
        print('(1) Estacionar\n(2) Remover\n(3) Listar\n(4) Sair')
        print('* '*10)
        option = ''
        option = int(input('Digite a opção desejada: '))
        if option == 1:
            estacionar(estacionamento)
        elif option == 2:
            remover(estacionamento)
        elif option == 3:
            estado_do_estacionamento(estacionamento)
        elif option == 4:
            exit()
        else:
            print('Opção inválida. Insira um número entre 1 and 4.')

