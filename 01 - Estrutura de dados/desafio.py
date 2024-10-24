from datetime import datetime

usuarios_cadastrados = []

class Conta:
    def __init__(self, usuario, conta, agencia, cpf, endereco):
        self.usuario = usuario
        self.conta = conta
        self.agencia = agencia
        self.cpf = cpf
        self.endereco = endereco
        self.saldo = 0.0
        self.transacoes = []
        self.saques_realizados = 0

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append({
            'tipo': 'Depósito',
            'valor': valor,
            'data': datetime.now()
        })
        print(f"Você depositou R${valor:.2f}. Saldo atual: R${self.saldo:.2f}")

    def sacar(self, valor):
        if self.saques_realizados >= 3:
            print("Limite de 3 saques por dia atingido!")
            return
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return
        if valor > 500:
            print("Valor máximo para saque é R$ 500!")
            return
        self.saldo -= valor
        self.saques_realizados += 1
        self.transacoes.append({
            'tipo': 'Saque',
            'valor': valor,
            'data': datetime.now()
        })
        print(f"Você sacou R${valor:.2f}. Saldo atual: R${self.saldo:.2f}")

    def extrato(self):
        if not self.transacoes:
            print("Não há transações registradas.")
            return
        print("Extrato:")
        for transacao in self.transacoes:
            data_formatada = transacao['data'].strftime("%d/%m/%Y %H:%M:%S")
            print(f"{transacao['tipo']}: R${transacao['valor']:.2f} em {data_formatada}")

def cadastrar():
    usuario = input("Qual nome do usuário? ")
    conta = int(input("Número da conta? "))
    agencia = int(input("Número da agência? "))
    cpf = input("Número do CPF? ")
    endereco = input("Qual endereço? ")

    for usuario_info in usuarios_cadastrados:
        if usuario_info.cpf == cpf:
            print("CPF já cadastrado! Tente novamente.")
            return None  

    nova_conta = Conta(usuario, conta, agencia, cpf, endereco)
    usuarios_cadastrados.append(nova_conta)
    return nova_conta

def listar_usuarios():
    if not usuarios_cadastrados:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios_cadastrados:
            print(f"Nome: {usuario.usuario}, Conta: {usuario.conta}, Agência: {usuario.agencia}, CPF: {usuario.cpf}")

def main():
    while True:
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        [c] Cadastrar
        [u] Listar Usuários
        => """
        
        opcao = input(menu).strip().lower()

        if opcao == 'c':
            cadastrar()
        elif opcao == 'u':
            listar_usuarios()
        elif opcao in ['d', 's', 'e']:
            if not usuarios_cadastrados:
                print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
                continue
            
            cpf = input("Digite o CPF do usuário: ")
            usuario_encontrado = next((u for u in usuarios_cadastrados if u.cpf == cpf), None)
            if not usuario_encontrado:
                print("Usuário não encontrado!")
                continue
            
            if opcao == 'd':
                valor = float(input("Qual valor para depósito? "))
                usuario_encontrado.depositar(valor)
            elif opcao == 's':
                valor = float(input("Qual o valor a sacar? "))
                usuario_encontrado.sacar(valor)
            elif opcao == 'e':
                usuario_encontrado.extrato()
        elif opcao == 'q':
            print('Obrigado, volte sempre...')
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
