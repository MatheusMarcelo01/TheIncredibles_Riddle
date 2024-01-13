def main():
    input("""        
          ==================================================================================
               Pense em um personagem do universo dos incriveis, e eu tentarei adivinhar! 
          ==================================================================================
               Pressione Enter quando estiver pronto(a) para começar...
          ==================================================================================""")

    #definindo se o persaongem é heroi ou não:
    personagem = input("Seu personagem é um super heroi? (Sim/Não/Não Sei): ").lower()

    #definido que é HEROI, vamos definir se é um heroi que morreu ou esta vivo
    if personagem == "sim": 
        personagem_heroi = input("Seu personagem já morreu? (Sim/Não/Não Sei): ").lower()
        if personagem_heroi == "não" or personagem_heroi == "nao":
            perguntas_super_humano()
        elif personagem_heroi == "sim":
            perguntas_morreram()

    #definido que é HEROI, vamos definir se é um heroi que morreu ou esta vivo         
    elif personagem == "não" or "nao":
        personagem_outros = input("Seu personagem é humano? (Sim/Não/Não Sei): ").lower()
        if personagem_outros == "sim": 
            perguntas_humanos()
        elif personagem_outros == "não" or "nao":
            print("Seu personagem é o Omnidroid")
            

    elif personagem == "não sei" or "nao sei":
        print("Você não sabe??? só responda se seu personagem tem poderes ou não.")
    else:
        print("Resposta inválida. Por favor, responda com 'Sim', 'Não' ou 'Não Sei'.")


#Função para tabela super
def perguntas_super_humano():
    perguntas_super_humano_dict = {
        "familia_pera": "Seu super heroi faz parte da família Pera? (Sim/Não/Não Sei): ",
        "amigo_familia": "Seu super heroi é um amigo da família Pera? (Sim/Não/Não Sei): ",
        "feminino": "Seu super heroi é feminino? (Sim/Não/Não Sei): ",
        "masculino": "Seu super heroi é masculino? (Sim/Não/Não Sei): "
        # Continuar com mais perguntas para outros personagens se desejar
    }

    for caracteristica, pergunta in perguntas_super_humano_dict.items():
        resposta = input(pergunta).lower()
        if resposta == "sim":

            #GRUPO 1 - FAMILIA PERA 
            if caracteristica == "familia_pera":
                #MULHERES FAMILIA PERA
                cabelo = input("Seu personagem tem cabelo preto? (Sim/Não/Não Sei):").lower()
                if cabelo == "sim":
                    perguntas_Cpreto = {
                        "Helena Pera": "Seu super heroi anda de moto e estica? (Sim/Não/Não Sei): ",
                        "Violeta Pera": "Seu super heroi fica invisível? (Sim/Não/Não Sei): ",                        
                    }
                    for personagem, pergunta in perguntas_Cpreto.items():
                                resposta_Cpreto = input(pergunta).lower()
                                if resposta_Cpreto == "sim":
                                    print(f"Seu personagem é a {personagem.capitalize()}!")
                #HOMENS FAMILIA PERA
                elif cabelo == "nao" or "não":
                    fogo = input("Seu personagem tem poder de fogo? (Sim/Não/Não Sei):")
                    if fogo == "sim":
                         print("Seu personagem é o Zezé Pera")
                         return
                    elif fogo == "não" or fogo == "nao":
                        perguntas_Npreto = {
                        "Roberto Pera": "Seu super heroi tem super força? (Sim/Não/Não Sei): ",
                        "Flexa Pera": "Seu super heroi está sempre com pressa? (Sim/Não/Não Sei): "  ,                    
                        "Zezé Pera": "Seu super heroi é um bebê metamorfo? (Sim/Não/Não Sei): ",
                        }
                        for personagem, pergunta in perguntas_Npreto.items():
                                    resposta_Npreto = input(pergunta).lower()
                                    if resposta_Npreto == "sim":
                                        print(f"Seu personagem é a {personagem.capitalize()}!")
                                        return

            #GRUPO 2 - AMIGO DA FAMILIA
            elif caracteristica == "amigo_familia":
                perguntas_amigo_pera_dict = {
                    "Gelado": "Seu personagem sempre tem um gelinho pra colocar no suco?"
                }
                for personagem, pergunta in perguntas_amigo_pera_dict.items():
                    resposta_amigo_pera = input(pergunta).lower()
                    if resposta_amigo_pera == "sim":
                        print(f"Seu personagem é o {personagem.capitalize()}!")
                        return
                print("Não consegui identificar quem é super herói amigo da familia pera")

            #GRUPO 3 - HEROINAS 
            elif caracteristica == "feminino":
                perguntas_heroina = {
                    "Voyd": "Seu personagem controla portais?",
                    "Compactor": "Sua personagem é muito forte?"
                }
                for personagem, pergunta in perguntas_heroina.items():
                    resposta_heroina = input(pergunta).lower()
                    if resposta_heroina == "sim":
                        print(f"Seu personagem é o {personagem.capitalize()}!")
                        return
                print("Não consegui identificar quem é a super herói")

            #GRUPO 4 - HEROIS
            elif caracteristica == "masculino":
                perguntas_herois = {
                    "He-lectryx": "Seu personagem tem poder elétrico?",
                    "Reflux": "Sua personagem tem poder de refluxos ácidos?",
                    "Krushauer": "Sua personagem tem super força?"

                }
                for personagem, pergunta in perguntas_herois.items():
                    resposta_herois = input(pergunta).lower()
                    if resposta_herois == "sim":
                        print(f"Seu personagem é o {personagem.capitalize()}!")
                        return
                print("Não consegui identificar quem é o super herói")

def perguntas_morreram():
    perguntas_morreram_dict = {
        "mortes_capa": "Seu super heroi foi morto por usar capa? (Sim/Não/Não Sei): ",
        "fantasmaticos": "Seu super heroi fez parte da equipes dos fantasmáticos? (Sim/Não/Não Sei): ",
        "feminino": "Seu super heroi é feminino? (Sim/Não/Não Sei): ",
        "masculino": "Seu super heroi é masculino? (Sim/Não/Não Sei): "
    }
    
    while True:
        for caracteristica, pergunta in perguntas_morreram_dict.items():
            resposta = input(pergunta).lower()

            #Informações:
            if resposta == "nao sei" or resposta == "não sei":
                if caracteristica == "mortes_capa":
                      print("""
                    =============================================================================
                       EDNA diz: Não use capa! Os heróis que morreram por esta razão foram:
                       Homem trovão, Strato Gata, Super Tchibum, Dinamite e Mega Homem
                    =============================================================================""")
                      input("Pressione qualquer tecla para continuar jogando...")
                      break
                      
                      
                     
                elif caracteristica == "fantasmaticos":
                      print("""
                    =============================================================================
                       Os heróis que faziam parte dos fantasmáticos eram:
                       Vidente, Onda Psiquica,Raio de plasma, Ventania e Olho laser
                    =============================================================================""")
                      input("Pressione qualquer tecla para continuar jogando...")
                      break

            if resposta == "sim":
                #GRUPO 1 - Mortos pela capa 
                if caracteristica == "mortes_capa":
                    #MULHERES Mortas por capa
                    mulher_capa = input("Sua personagem é mulher? (Sim/Não/Não Sei):").lower()
                    if mulher_capa == "sim":
                        print("Sua personagem é a Strato Gata!")
                        return
                    #HOMENS MORTOS Pela capa
                    elif mulher_capa == "não" or mulher_capa == "nao":
                        perguntas_homem_capa = {
                        "Homem trovão": "Seu herói morreu porque sua capa ficou presa a um foguete? (Sim/Não/Não Sei): ",
                        "Super Tchibum": "Seu herói morreu sugado por um vortex? (Sim/Não/Não Sei): "  ,                    
                        "Dinamite": "Seu herói morreu porque sua capa ficou presa ao chão quando saiu voar? (Sim/Não/Não Sei): ",
                        "Mega Homem": "Seu heroi morreu porque sua capa ficou presa no elevador expresso? (Sim/Não/Não Sei): ",
                        }
                        for personagem, pergunta in perguntas_homem_capa.items():
                                    resposta_homem_capa = input(pergunta).lower()
                                    if resposta_homem_capa == "sim":
                                        print(f"Seu personagem é a {personagem.capitalize()}!")
                                        return               
                #Grupo 2 - Fantasmaticos
                elif caracteristica == "fantasmaticos":
                    #homens
                    homem_fant = input("Seu personagem é um homem? (Sim/Não/Não Sei):").lower()
                    if homem_fant == "nao" or homem_fant == "não":
                         print("Sua personagem é Onda Psiquica!")
                         return

                    elif homem_fant == "sim":
                        #Lider dos fantasmaticos
                        lider = input("Seu personagem foi lider dos fantasmaticos? (Sim/Não/Não Sei):").lower()

                        
                        if lider == "sim":
                            print("Seu personagem é o Vidente!")
                            return
                        
                        elif lider == "nao sei":
                             print("""
                    =============================================================================
                       Os lider dos fantasmáticos tinha poder de telepatia e lia mentes.
                    =============================================================================""")
                             input("Pressione qualquer tecla para continuar jogando...")
                             break
                            
                        elif lider == "não" or lider == "nao":
                            perguntas_homem_fant = {
                            "Olho Laser": "Você é a Duda, e esta jogando pela primeira vez? (Sim/Não/Não Sei): ",
                            "Ventania": "Seu herói tem o poder de criar e controlar ventos? (Sim/Não/Não Sei): "  ,                    
                            "Raio de Plasma": "Seu herói tem poder de disparar raios de plasma? (Sim/Não/Não Sei): ",
                            }
                            for personagem, pergunta in perguntas_homem_fant.items():
                                        resposta_homem_fant = input(pergunta).lower()
                                        if resposta_homem_fant == "sim":
                                            print(f"Seu personagem é a {personagem.capitalize()}!")
                                            return             
                    

                     #Lider dos fantasmaticos
                    lider = input("Seu personagem foi lider dos fantasmaticos? (Sim/Não/Não Sei):").lower()
                    if lider == "sim":
                        print("Seu personagem é o Vidente!")
                        return
                    

                    #HOMENS dos Fantasmaticos
                    elif mulher_capa == "não" or mulher_capa == "nao":
                        perguntas_homem_capa = {
                        "Homem trovão": "Seu herói morreu porque sua capa ficou presa a um foguete? (Sim/Não/Não Sei): ",
                        "Super Tchibum": "Seu herói morreu sugado por um vortex? (Sim/Não/Não Sei): "  ,                    
                        "Dinamite": "Seu herói morreu porque sua capa ficou presa ao chão quando saiu voar? (Sim/Não/Não Sei): ",
                        "Mega Homem": "Seu heroi morreu porque sua capa ficou presa no elevador expresso? (Sim/Não/Não Sei): ",
                        }
                        for personagem, pergunta in perguntas_homem_capa.items():
                                    resposta_homem_capa = input(pergunta).lower()
                                    if resposta_homem_capa == "sim":
                                        print(f"Seu personagem é a {personagem.capitalize()}!")
                                        return            

def perguntas_humanos():
    perguntas_humanos = {
        "vilao": "Seu personagem é uma vilã ou vilão? (Sim/Não/Não Sei): ",
        "memoria": "Seu personagem teve a memória apagada? (Sim/Não/Não Sei): ",
        "Hfeminino": "Sua personagem é uma mulher? (Sim/Não/Não Sei): ",
        "Hmasculino": "Seu personagem é um homem? (Sim/Não/Não Sei): "
    }

    for caracteristica, pergunta in perguntas_humanos.items():
        resposta = input(pergunta).lower()
        if resposta == "sim":
            #GRUPO 1 - VILAO 
            if caracteristica == "vilao":
                #Vila - MULHER
                vilaoF = input("A personagem é uma mulher? (Sim/Não/Não Sei):").lower()
                if vilaoF == "sim":
                    print("Sua personagem é a Evelyn Deavor!!!")
                    return

                #Vilao Homem
                elif vilaoF == "nao" or "não":
                        perguntas_vilaoM = {
                        "Bochecha (Sindrome)": "Seu super heroi tem super força? (Sim/Não/Não Sei): ",
                        "Escavador:": "Este vilão gosta de cavar e roubar bancos? (Sim/Não/Não Sei): "  ,                    
                        "Bomb Voyage": "Seu vilão é mimico? (Sim/Não/Não Sei): ",
                        "Winston Deavor": "Seu vilão é irmão da 'hacker' no filme? (Sim/Não/Não Sei): ",
                        }
                        for personagem, pergunta in perguntas_vilaoM.items():
                                    resposta_vilaoM = input(pergunta).lower()
                                    if resposta_vilaoM == "sim":
                                        print(f"Seu personagem é a {personagem.capitalize()}!")
                                        return

            #GRUPO 2 - Memoria apagadas
            elif caracteristica == "memoria":
                deleteM = input("Sua personagem era quem cuidava do Zezé?(Sim/Não/Não Sei):").lower()
                if deleteM == "sim":
                     print("Sua personagem é a Karen!")
                     return
                elif deleteM == "nao" or deleteM == "não":
                     print("Seu personagem é o Toninho!")
                     return

            #GRUPO 3 - Mulheres 
            elif caracteristica == "Hfeminino":
                perguntas_heroina = {
                    "Edna Moda": "Sua personagem costuma criar uniformes para os heróis?",
                    "Mirage": "Sua personagem era assistente do Sindrome Bochecha?",
                    "Mel": "Sua personagem era esposa do Gelado?",
                    "Selick": "Sua personagem é uma embaixadora?"
                }
                for personagem, pergunta in perguntas_heroina.items():
                    resposta_heroina = input(pergunta).lower()
                    if resposta_heroina == "sim":
                        print(f"Seu personagem é o {personagem.capitalize()}!")
                        return
                print("Não consegui identificar quem é sua personagem.")

            #GRUPO 4 - HOMENS
            elif caracteristica == "Hmasculino":
                perguntas_herois = {
                    "Ricardo Dicker": "Seu personagem apaga as memórias de quem sabe demais?",
                    "Bernardo Braga": "Seu personagem é professor?",
                    "Gilberto Lima": "Seu personagem era chefe de uma empresa, onde o Sr. Incrível trabalhava?"
                }
                for personagem, pergunta in perguntas_herois.items():
                    resposta_herois = input(pergunta).lower()
                    if resposta_herois == "sim":
                        print(f"Seu personagem é o {personagem.capitalize()}!")
                        return
                print("Não consegui identificar quem é seu personagem.")
     


#Função final
if __name__ == "__main__":
    main()
