#definindo a classe 
class Carro:
    def __init__(self, cor, modelo, velocidade):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade
        self.velocidade_min = 0
        self.velocidade_max = 110

    def ligar(self):
        self.ligado = True
        
    def desligar(self):
        self.ligado = False
        print('Desligando carro')

    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10
            print('Aumentando a velocidade em 10km/h')

    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10
            print('Desacelerando a 10km/h')
    
    def __str__(self) -> str:
        return (f'Carro ligado: {self.ligado}, {self.cor}, {self.modelo}, velocidade {self.velocidade}km/h')
    
carro1 = Carro('amarelo', 'Gol', 60)
carro2 = Carro('azul', 'SUV', 80)
carro3 = Carro('preto', 'Mustang', 30)
carro1.ligar()
carro2.ligar()
carro3.ligar()

print(f'{carro1}\n{carro2}\n{carro3}')
carro2.acelerar()
print(carro2)
carro3.acelerar()
print(carro3)
carro1.desacelerar()
print(carro1)
carro1.desligar()
carro2.desligar()
carro3.desligar()
print(f'{carro1}\n{carro2}\n{carro3}')