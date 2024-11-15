import random

agentes = [
    "Brimstone", "Phoenix", "Sage", "Sova", "Viper", "Cypher",
    "Reyna", "Killjoy", "Breach", "Omen", "Jett", "Raze",
    "Skye", "Yoru", "Astra", "KAY/O", "Chamber", "Neon",
    "Fade", "Harbor", "Gekko", "Deadlock", "Clove", "Iso", "Vyse"
]

personas = ['davo', 'h', 'babs', 'valen', 'musashi']
agentiques = ["Phoenix", "Sage", "Jett", "Brimstone", "Sova"]

asignaciones = {}

for persona in personas:
    if persona in ['h', 'musashi']:
        elegido = random.choice(agentiques)
        agentiques.remove(elegido)
        agentes.remove(elegido)
    else:
        elegido = random.choice(agentes)
        agentes.remove(elegido)
    
    asignaciones[persona] = elegido

for persona, agente in asignaciones.items():
    print(f"{persona} {agente}")