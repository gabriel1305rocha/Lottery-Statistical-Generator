"""
Calculo de médias: Para cada posição (de 1 a 6), 
calculo de média dos valores correspondentes nas várias arrays. 
Resultado: estimativa do valor médio para cada posição (de 1 a 6).
"""
def calcular_medias(arrays):
    num_arrays = len(arrays)
    num_posicoes = len(arrays[0])

    
    medias = [0] * num_posicoes

    # Calcula a média para cada posição.
    for i in range(num_posicoes):
        # Calcular a média dos valores na posição i em todas as arrays
        soma = sum(array[i] for array in arrays)
        media = soma / num_arrays

        medias[i] = media

    return medias

# MEGA DA VIRADA: TODOS OS RESULTADOS DE 2005 A 2022; Fonte: https://galardians.com/todos-resultados-mega-da-virada/
arrays_mega_da_virada = [
    #2023
    [24,56,33,48,21,41]
    #2022 
    [4,5,10,34,58,59],
    #2021 
    [12,15,23,32,33,46],
    #2020 
    [17,20,22,35,41,42],
    #2019 
    [3,35,38,40,57,58],
    #2018 
    [5,10,12,18,25,33],
    #2017 
    [3,6,10,17,34,37],
    #2016 
    [5,11,22,24,51,53],
    #2015 
    [2,18,31,42,51,56],
    #2014 
    [1,5,11,16,20,56],
    #2013 
    [20,30,36,38,47,53],
    #2012 
    [14,32,33,36,41,52],
    #2011 
    [3,4,29,36,45,55],
    #2010 
    [2,10,34,37,43,50],
    #2009 
    [10,27,40,46,49,58],
    #2008 
    [1,11,26,51,59,60],
    #2007 
    [7,17,19,34,36,39],
    #2006 
    [10,14,32,47,50,56],
    #2005 
    [3,9,35,37,41,49]
]

medias_resultantes = calcular_medias(arrays_mega_da_virada)

medias_resultantes_arredondado = [int(round(num)) for num in medias_resultantes]

print("Baseado nos calculos das médias posicionais dos resultados previamente inseridos eu apóstaria nos numeros:", medias_resultantes_arredondado)
