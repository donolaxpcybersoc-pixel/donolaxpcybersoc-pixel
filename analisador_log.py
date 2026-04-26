# ANALISADOR BLUE TEAM v2.0 - LENDO ARQUIVO REAL
print("=== PYTHON 3.14.4 ONLINE ===")
print("=== AGENTE FELIPE V2.0 OPERACIONAL 🛡️ ===")

# PARTE 1: Criar um arquivo de log fake pra treinar
print("\n[1] Criando arquivo auth.log para simulação...")
with open("auth.log", "w") as arquivo:
    arquivo.write("Accepted password for user felipe\n")
    arquivo.write("Failed password for invalid user root\n")
    arquivo.write("Failed password for invalid user admin\n")
    arquivo.write("Accepted password for user felipe\n")
    arquivo.write("Failed password for invalid user hacker\n")
    arquivo.write("Failed password for invalid user test\n")
print("Arquivo auth.log criado com sucesso!")

# PARTE 2: Ler o arquivo igual Kali Linux faz
print("\n[2] Iniciando varredura no auth.log...")
ataques = 0
with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        if "Failed password" in linha:
            ataques += 1
            print(f"[ALERTA CRÍTICO] ATAQUE #{ataques}: {linha.strip()}")

print(f"\n=== SCAN COMPLETO: {ataques} TENTATIVAS DE INVASÃO BLOQUEADAS ===")
print("=== V2.0 ONLINE. PRONTO PRA LOGS REAIS ===")