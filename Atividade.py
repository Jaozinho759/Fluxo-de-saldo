#Atividade 1
class ContaBancaria:    #1
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R$ {self.saldo:.2f}'

#Atividade 2
class ContaBancaria:     #2
    taxa_juros = 0.02  # Taxa de juros padrão (exemplo)
    total_contas = 0  # Contador de contas criadas

    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo
        ContaBancaria.total_contas += 1  # Incrementa o contador de contas

    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R$ {self.saldo:.2f}'
    


    taxa_juros = 0.02  # Taxa de juros padrão 
    total_contas = 0  # Contador de contas criadas

    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo
        ContaBancaria.total_contas += 1  # Incrementa o contador de contas

    def depositar(self, valor):  # Atividade 3
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('O valor não pode ser zero ou negativo!')

    def sacar(self, valor):  # Atividade 4
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor inválido ou saldo insuficiente!')

    def verificar_saldo(self):     # Atividade 5
        print(f'Saldo atual: R$ {self.saldo:.2f}')

    @classmethod
    def ajustar_taxa_juros(cls, nova_taxa):  # Atividade 6
        if nova_taxa > 0:
            cls.taxa_juros = nova_taxa
            print(f'Nova taxa de juros ajustada para {nova_taxa * 100:.2f}%')
        else:
            print('A taxa de juros deve ser positiva!')

    @classmethod
    def mostrar_total_contas(cls):    # Atividade 7
        print(f'Total de contas criadas: {cls.total_contas}')

    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R$ {self.saldo:.2f}' 
    
class ConversorMoeda:  # Atividade 8
        
    @staticmethod
    def converter_moeda(valor: float, taxa: float) -> float:

        return round(valor * taxa, 2)


class CalendarioUtils:  # Atividade 9
    @staticmethod

    def dias_no_ano(ano: int) -> int:

        if type(ano) is not int:
            raise TypeError("Ano deve ser inteiro")
        
        return 366 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else 365



    
conta = ContaBancaria("João", 1000.0)
#print(conta)
#conta.depositar(500)
#print(conta)
#conta.sacar(500)
#print(conta)
#conta.sacar(2000)
#conta.verificar_saldo()
#ContaBancaria.ajustar_taxa_juros(0.05)
#ContaBancaria.mostrar_total_contas()

#print(ConversorMoeda.converter_moeda(250, 5.45))  
#print(CalendarioUtils.dias_no_ano(2025))
