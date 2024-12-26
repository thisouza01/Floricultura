class Planta:
    def __init__(self, nome, preco, preferencia):
        self.nome = nome
        self.preco = preco
        self.preferencia = preferencia

    def dicionario(self):
        return {"Nome": self.nome, "Preço": self.preco, "Preferência": self.preferencia}    

if __name__ == '__main__':
    def recebe_dados():
        nome = str(input('Nome da planta: '))
        preco = float(input('Preço: '))
        preferencia = str(input('Preferencia: ')) 

        return nome, preco, preferencia

    planta = recebe_dados()
    planta1 = Planta(*planta)

    print(planta1.nome)