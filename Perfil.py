from faker import Faker
from faker.providers import internet

lista = Faker('pt_BR') #País de origem dos dados
for _ in range (1): #Quantidade de dados
    print("Nome: ", lista.name()) #Gera o nome
    print("Endereço: ", lista.address())  #Gera o endereço]
    print("Email: ", lista.email()) #Gera email
    

lista.add_provider(internet)

print("IP: ", lista.ipv4_private()) #Gera o ip

print("Telefone: " , lista.phone_number()) #Gera os números (pelo que vi só telefone fixo)

#print(lista.profile()) #Gera um perfil aleatório (mt aleatório, 0 sentido)

#print (lista.simple_profile()) #Gera um perfil mais simples

#print ("Cartão full: ", lista.credit_card_full()) #Perfil inteiro do cartão de crédito

print ("Número do Cartão de crédito: ",lista.credit_card_number()) #número cartão de crédito


#Para gerar mais de 1 ao mesmo tempo colocar os prints de cima dentro do for
