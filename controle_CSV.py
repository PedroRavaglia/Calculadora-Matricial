import csv
import numpy as np
import pandas as pd
import classe_matriz as cm



## Tira os colchetes das strings que representam as matrizes no arquivo CSV
 # EX: '[1 2 3];[4 5 6]' -> '1 2 3;4 5 6'
def cleanStrData(str):
    data = str.replace('[', '')
    data = data.replace(']', '')
    return data




## Converte uma string em uma matriz, de acordo com seu tipo
def str2matrix(str, type):
    
    if type in ['r', 'q', 'l', 'c']:
        mat = cleanStrData(str)
        mat = mat.split(';')
        
        for i in range(len(mat)):
            mat[i] = np.fromstring(mat[i], sep=' ')
            
            
    if type == 'd':
        mat = cleanStrData(str)
        mat = np.fromstring(mat, sep=' ')
        mat = np.diag(mat)
        
        
    if type in ['ts', 'ti']:
        mat = cleanStrData(str)
        mat = mat.split(';')
        
        for i in range(len(mat)):
            mat[i] = np.fromstring(mat[i], sep=' ')
            
            if len(mat[i]) < len(mat) and type == 'ts':
                mat[i] = np.append(np.zeros(len(mat) - len(mat[i])), mat[i])
                
            if len(mat[i]) < len(mat) and type == 'ti':
                mat[i] = np.append(mat[i], np.zeros(len(mat) - len(mat[i])))
                
                
    if type == 's':
        mat = cleanStrData(str)
        mat = mat.split(';')
        for i in range(len(mat)):
            mat[i] = np.fromstring(mat[i], sep=' ')
        
        for i in range(len(mat)):
            for j in range(i+1, len(mat)):
                mat[i] = np.append(mat[i], mat[j][i])
        
        
    mat = np.array(mat)
    
    return cm.array_to_matriz(mat)




## Adiciona uma nova matriz na última linha do dataframe
def add_row(mat, df):
    str_mat = []
    
    if mat.tag in ['r', 'q', 'l', 'c']:
        for i in range(mat.n):
            array = np.array(mat[i])
            str_array = np.array2string(array)
            str_mat.append(str_array)
            
        str_mat = ';'.join(str_mat)
        
        
    if mat.tag == 'd':
        for i in range(mat.n):
            str_mat.append(mat.Get_Aij(i, i))
        array = np.array(str_mat)
        str_mat = np.array2string(array)
        
        
    if mat.tag in ['ts', 'ti', 's']:
        for i in range(mat.n):
            array = np.array(mat[i])
            
            if mat.tag == 'ts':
                str_array = np.array2string(array[i: mat.n])
            else:
                str_array = np.array2string(array[0: i+1])
                
            str_mat.append(str_array)
            
        str_mat = ';'.join(str_mat)
        
    
    new_row = {'type': mat.tag, 'num_rows': mat.n, 'num_cols': mat.m, 'matrix': str_mat}
    
    return df.append(new_row, ignore_index=True)




## Retorna a matriz do dataframe referente ao índice
def index2matrix(i, df):
    return str2matrix(df['matrix'][i], df['type'][i])

## Retorna a matriz referente ao índice do arquivo CSV
def getMatrix(path, i):
    df = pd.read_csv(path, skiprows=1)
    return str2matrix(df['matrix'][i], df['type'][i])




## Retorna o número de matrizes que estão gravadas no arquivo CSV
def n_mat(path):
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        return int(next(csv_reader)[0])




## Retorna a lista de matrizes do arquivo CSV
def get_list(path):
    l = []
    n = n_mat(path)
    
    for i in range(n):
        l.append(getMatrix(path, i))
        
    return l
    
    
    

## Grava a lista de matrizes no arquivo CSV 
def list2csv(path, l):
    
    # Criando um dataframe com a lista de matrizes
    attributes = ['type', 'num_rows', 'num_cols', 'matrix']
    df = pd.DataFrame(columns=attributes)
    for i in range(len(l)):
       df = add_row(l[i], df)
       
    # Escrevendo no cabeçalho do arquivo a quantidade de matrizes da lista
    df1 = pd.DataFrame({'a': [len(l)]})
    df1.to_csv(path, index=False, header=None)
       
    # Escrevendo o dataframe da lista de matrizes no arquivo
    df.to_csv(path, index=False, encoding = "ISO-8859-1", mode='a')
       
    return




## Grava uma nova matrix na última linha do arquivo CSV e retorna a lista de
 # matrizes atualizada.
def add_matrix(path, mat, l): 
    l.append(mat)
    list2csv(path, l)
    
    return l
