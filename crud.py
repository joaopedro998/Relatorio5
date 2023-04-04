class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("escolha uma opçao:  ")

            if command == "5":
                print("voce saiu!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Isso nao é umas da opçoes validas")


class livroCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("1", self.create_livro)
        self.add_command("2", self.read_livro)
        self.add_command("3", self.update_livro)
        self.add_command("4", self.delete_livro)

    def create_livro(self):
        titulo = input("entre com o titulo : ")
        autor = input("entre com o autor: ")
        ano = int(input("entre com o ano do livro: "))
        preco = int(input("entre como preço : "))

        self.livro_model.create_livro(titulo, autor, ano, preco)

    def read_livro(self):
        id = input("entre com o id: ")
        livro = self.livro_model.read_livro_by_id(id)
        if livro:
            print(f"Livro: {livro['titulo']}")
            print(f"author: {livro['autor']}")
            print(f"year: {livro['ano']}")
            print(f"price: {livro['preco']}")

    def update_livro(self):
        id = input("entre com o id: ")
        titulo = input("entre com o titulo : ")
        autor = input("entre com o autor: ")
        ano = int(input("entre com o ano do livro: "))
        preco = int(input("entre como preço : "))
        self.livro_model.update_livro(id, titulo, autor, ano, preco)

    def delete_livro(self):
        id = input("entre com o id: ")
        self.livro_model.delete_livro(id)

    def run(self):
        print("Bem vindo a Biblioteca")
        print("1-adicionar livro")
        print("2-procurar livro")
        print("3-atualizar livro")
        print("4-deletar livro")
        print("5-sair")
        super().run()