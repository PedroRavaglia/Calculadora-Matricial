import numpy as np

def triangular(n):
    """Calcula a soma dos números naturais até 'n'"""
    return int(n*(n+1)/2) # fórmula da soma dos primeiros números naturais

def get_tag(x):
    """Determina qual o tipo de 'Matriz' a ser criada"""
    # ENTRADA
    # x (np.array): array do Numpy de dimensão 2 a ser avaliado
    #-------------------------------------------------------------
    # SAÍDA
    # tag (str): string contendo o tipo de matriz a ser construída
    
    if type(x) != np.ndarray:
        print("<func get_tag> Erro: Método aceita apenas objetos do tipo 'numpy.ndarray'")
        return None
    elif len(x.shape) != 2:
        print("<func get_tag> Erro: Só é possível converter para 'Matriz' arrays de duas dimensões")
        return None
    else:
        n = x.shape[0]
        m = x.shape[1]
        if n != m:
            if n == 1:
                return "l" # É matriz linha
            elif m == 1:
                return "c" # É matriz coluna
            else:
                return "r" # É matriz retangular
        else:
            inf = True
            sup = True
            for i in range(n):
                for j in range(m):
                    if i > j and x[i][j] != 0:
                        sup = False
                    if i < j and x[i][j] != 0:
                        inf = False
            if inf and sup:
                return "d" # É matriz diagonal
            elif inf:
                return "ti" # É matriz triangular inferior
            elif sup:
                return "ts" # É matriz triangular superior
            else:
                if (x == np.transpose(x)).all():
                    return "s" # É matriz simétrica
                else:
                    return "q" # É matriz quadrada

def array_to_matriz(x):
    """Converte um objeto do tipo 'np.array' de dimensão 2 para um objeto
    de uma classe que seja subclasse de 'Matriz'"""
    # ENTRADA
    # x (np.array): array do Numpy de dimensão 2 a ser convertido
    #---------------------------------------------------------------
    # SAÍDA
    # matriz (Matriz): especialização de 'Matriz' da classe adequada
    
    tag = get_tag(x)
    if tag == None:
        return None # A matriz não pode ser convertida sem saber o tipo dela
    else:
        n = x.shape[0] # número de linhas da matriz
        m = x.shape[1] # número de colunas da matriz
        dados = []
        
        if tag == "r" or tag == "l" or tag == "c" or tag == "q":
            
            # Construindo a lista de dados
            for i in range(n):
                for j in range(m):
                    dados.append(float(x[i][j]))
            
            if tag == "r": 
                return MatrizRet(n, m, dados) # Criando matriz retangular
            if tag == "l": 
                return MatrizLin(m, dados) # Criando matriz linha
            if tag == "c":
                return MatrizCol(n, dados) # Criando matriz coluna
            if tag == "q":
                return MatrizQuad(n, dados) # Criando matriz quadrada
            
        if tag == "ts" or tag == "s":
            
            # Construindo a lista de dados
            for i in range(n):
                for j in range(m):
                    if i <= j:
                        dados.append(float(x[i][j]))
                        
            if tag == "ts":
                return MatrizTriSup(n, dados) # Criando matriz triangular superior
            if tag == "s":
                return MatrizSim(n, dados) # Criando matriz simétrica
            
        if tag == "ti":
            
            # Construindo a lista de dados
            for i in range(n):
                for j in range(m):
                    if i >= j:
                        dados.append(float(x[i][j]))
                        
            return MatrizTriInf(n, dados) # Criando matriz triangular inferior
            
        if tag == "d":
            
            # Construindo a lista de dados
            for i in range(n):
                dados.append(float(x[i][i]))
                        
            return MatrizDiag(n, dados) # Criando matriz triangular diagonal
            
                    
class Matriz:
    
    def __init__(self, n = None, m = None, dados = None):
        """Construtor da classe raiz
        
        Se os valores de entrada não forem adequados, a matriz será tratada como
        vazia, impedindo todas as operações de serem realizadas até as informações 
        contidas se tornarem válidas"""
        
        # ENTRADA
        # n      (int): número de linhas
        # m      (int): número de colunas
        # dados (list): lista contendo os dados a serem inseridos nas entradas
        #   da matriz, sendo apenas a quantidade estritamente necessária para
        #   gerar a matriz de acordo com a subclasse adequada; cada subclasse
        #   possui o seu próprio construtor para cuidar das especializações
        #---------------------------------------------------------------------
        # SAÍDA
        
        if self.validated == True:
            for i in range(len(dados)):
                dados[i] = float(dados[i])
            self.dados = dados
            self.n = n
            self.m = m
        else:
            self.dados = None
            self.n = None
            self.m = None
            
        return None
    
    def typeValidation(self, n, m, dados):
        """Certifica-se de os valores recebidos pelo construtor são do tipo
        desejado, caso o contrário declara a matriz como sendo vazia"""
        
        if type(n) != int:
            print("<func typeValidation> Aviso: Matriz será tratatda como vazia até 'n' ser objeto do tipo 'int'")
            return False
        
        if n <= 0:
            print("<func typeValidation> Aviso: Matriz será tratatda como vazia até 'n' ser um inteiro positivo")
            return False
        
        if type(m) != int:
            print("<func typeValidation> Aviso: Matriz será tratatda como vazia até 'm' ser objeto do tipo 'int'")
            return False
        
        if m <= 0:
            print("<func typeValidation> Aviso: Matriz será tratatda como vazia até 'm' ser um inteiro positivo")
            return False
        
        if type(dados) != list:
            print("<func typeValidation> Aviso: Matriz será tratatda como vazia até 'dados' ser objeto do tipo 'list'")
            return False
        
        return True
    
    def valueValidation(self, n, m, dados):
        """Certifica-se de que 'dados', recebido pelo construtor, contém a 
        quantidade adequada de elementos, sendo todos do tipo 'int' ou 'float',
        caso o contrário declara a matriz como sendo vazia"""
        
        if len(dados) != n*m:
            print("<func valueValidation> Aviso: Matriz será tratatda como vazia até o número de elementos em 'dados' ser adequado")
            return False
        
        for i in range(n*m):
            if type(dados[i]) != int and type(dados[i]) != float:
                print("<func valueValidation> Aviso: Matriz será tratatda como vazia até todos os elementos de 'dados' serem objetos do tipo 'int' ou 'float'")
                return False
            
        return True
    
    def matriz_to_array(self):
        """Converte um objeto herdado de 'Matriz' em um array do Numpy"""
        
        if self.validated == False:
            print("<func matriz_to_array> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        matriz = []
        for i in range(self.n):
            matriz.append(self.m*[0.0])
            
        for i in range(len(self.dados)):
            matriz[i//self.m][i%self.m] = self.dados[i]
        
        return np.array(matriz)
        
    def __add__(self, x):
        """Soma dois objetos herdados de 'Matriz' se tiverem dimensões compatíveis"""
        
        if self.validated == False:
            print("<func __add__> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        if not issubclass(type(x), Matriz):
            print("<func __add__> Erro: 'x' precisa ser herdado de 'Matriz'")
        else:
            if self.n != x.n or self.m != x.m:
                print("<func __add__> Erro: Não é possível somar matrizes de dimensões diferentes")
                return None
            else:
                A = self.matriz_to_array()
                B = x.matriz_to_array()
                return array_to_matriz(A + B)
        
    def __radd__(self, x):
        """Implementa a soma à direita"""
        return self.__add__(x)
    
    def __mul__(self, x):
        """Realiza o produto matricial entre dois objetos herdados de 'Matriz' se compatíveis"""
        
        if self.validated == False:
            print("<func __mul__> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        if not issubclass(type(x), Matriz) and type(x) != int and type(x) != float:
            print("<func __mul__> Erro: Só é adimitido o produto de matrizes ou de matriz por escalar")
            return None
        
        elif type(x) == int or type(x) == float:
            A     = self.matriz_to_array()
            alpha = x
            C     = alpha*A
            return array_to_matriz(C)
        
        else:
            if self.m != x.n:
                print("<func __mul__> Erro: Matrizes de dimensões não compatíveis")
                return None
            else:
                A = self.matriz_to_array()
                B = x.matriz_to_array()
                C = np.dot(A, B)
                return array_to_matriz(C)
    
    def __rmul__(self, x):
        """Implementa o produto à direita"""
        
        if self.validated == False:
            print("<func __rmul__> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        if type(x) == int or type(x) == float:
            A     = self.matriz_to_array()
            al1pha = x
            C     = alpha*A
            return array_to_matriz(C)
        else:
            print("<func __rmul__> Erro: Só é adimitido o produto de matrizes ou de matriz por escalar")
            return None
    
    def __str__(self):
        """Constroi a string a ser mostrada quando usado o comando 'print'"""
        
        if self.validated == False:
            print("<func __str__> Aviso: Não é possível operar com uma matriz vazia")
            return ""
        
        string = str(self.matriz_to_array())
        return string
    
    def __repr__(self):
        """Constroi a string a ser mostrada quando um objeto herdado de 'Matriz'
        for chamado"""
        
        if self.validated == False:
            print("<func __repr__> Aviso: Não é possível operar com uma matriz vazia")
            return ""
        
        string = repr(self.matriz_to_array())
        string = string.replace("array", "Matriz")
        string = string.replace("\n", "\n ")
        return string
        
    def __getitem__(self, index):
        """Obtêm a linha da matriz correspondente de acordo com 'index'"""
        
        if self.validated == False:
            print("<func __getitem__> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        if type(index) != int:
            print("<func __getitem__> Erro: Índice precisa ser do tipo 'int'")
            return None
        elif index < 0 or index >= self.n:
            print("<func __getitem__> Erro: Índice fora dos limites")
            return None
        else:
            A = self.matriz_to_array()
            lista = []
            for j in range(self.m):
                lista.append(float(A[index][j]))
            return lista
    
    def __setitem__(self, index, value):
        """Altera a linha da matriz correspondente de acordo com 'index' e gera um aviso 
        caso a alteração de acordo com 'value' gere uma mudança na classe original"""
        # ENTRADA
        # index  (int): índice da linha a ser subtituída
        # value (list): linha para substituir
        #---------------------------------------------------------------------
        # SAÍDA
        
        if self.validated == False:
            print("<func __setitem__> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        if type(index) != int:
            print("<func __setitem__> Erro: Índice precisa ser do tipo 'int'")
            return None
        elif index < 0 or index >= self.n:
            print("<func __setitem__> Erro: Índice fora dos limites")
            return None
        elif type(value) != list:
            print("<func __setitem__> Erro: Valor atribuído deve ser um objeto do tipo 'list'")
            return None
        elif len(value) != self.m:
            print("<func __setitem__> Erro: Comprimento de 'value' deve ser igual ao número de colunas da matriz")
            return None
        else:
            for j in range(self.m):
                if type(value[j]) != int and type(value[j]) != float:
                    print("<func __setitem__> Erro: Objetos de 'value' devem ser tipo 'int' ou 'float'")
                    return None
            
            A = self.matriz_to_array()
            A[index] = value
            A = array_to_matriz(A)
            if self.tag == A.tag:
                self.dados = A.dados
                return None
            else:
                print("<func __setitem__> AVISO: Não é possível alterar esse valor, pois altera a classe do objeto")
                return None
        
    def Set_Aij(self, i, j, dado):
        """Altera o elemento da linha 'i' e coluna 'j' para o objeto 'dado' e gera um 
        aviso caso a alteração de acordo com 'value' gere uma mudança na classe original"""
        
        if self.validated == False:
            print("<func Set_Aij> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        self[i][j] = dado
        return None
    
    def Get_Aij(self, i, j):
        """Obtêm o elemento da linha 'i' e coluna 'j'"""
        
        if self.validated == False:
            print("<func Get_Aij> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        return self[i][j]
        
    def t(self):
        """Calcula a tranposta"""
        
        if self.validated == False:
            print("<func t> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        A = self.matriz_to_array()
        A = np.transpose(A)
        return array_to_matriz(A)
    
    def trace(self):
        
        if self.validated == False:
            print("<func trace> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        print("<func trace> Erro: Este método só pode ser aplicado em instâncias de subclasses de 'MatrizQuad'")
        return None
        
    def det(self):
        
        if self.validated == False:
            print("<func det> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        print("<func det> Erro: Este método só pode ser aplicado em instâncias de subclasses de 'MatrizQuad'")
        return None    
        
    def inv(self):
        
        if self.validated == False:
            print("<func inv> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        print("<func inv> Erro: Este método só pode ser aplicado em instâncias de subclasses de 'MatrizQuad'")
        return None
    
    def diag(self):
        
        if self.validated == False:
            print("<func diag> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        print("<func diag> Erro: Este método só pode ser aplicado em instâncias da classe 'MatrizSim'")
        return None
    
class MatrizRet(Matriz):
    
    def __init__(self, n = None, m = None, dados = None):
        """Construtor"""
        self.validated = Matriz.typeValidation(self, n, m, dados)
        if self.validated:
            self.validated = Matriz.valueValidation(self, n, m, dados)
        Matriz.__init__(self, n, m, dados)
        self.tag = "r"
        
        return None
    
    def validate(self, n = None, m = None, dados = None):
        """Tenta transformar uma matriz vazia em uma matriz não vazia chamando novamente o construtor das classe"""
        self.__init__(n, m, dados)
        return None
        
class MatrizLin(MatrizRet):
    
    def __init__(self, m = None, dados = None):
        """Construtor"""
        self.validated = Matriz.typeValidation(self, 1, m, dados)
        if self.validated:
            self.validated = Matriz.valueValidation(self, 1, m, dados)
        Matriz.__init__(self, 1, m, dados)
        self.tag = "l"
        
        return None
    
    def validate(self, m = None, dados = None):
        """Tenta transformar uma matriz vazia em uma matriz não vazia chamando novamente o construtor das classe"""
        self.__init__(m, dados)
        return None
    
class MatrizCol(MatrizRet):
    
    def __init__(self, n = None, dados = None):
        """Construtor"""
        self.validated = Matriz.typeValidation(self, n, 1, dados)
        if self.validated:
            self.validated = Matriz.valueValidation(self, n, 1, dados)
        Matriz.__init__(self, n, 1, dados)
        self.tag = "c"
        
        return None
    
    def validate(self, n = None, dados = None):
        """Tenta transformar uma matriz vazia em uma matriz não vazia chamando novamente o construtor das classe"""
        self.__init__(n, dados)
        return None
    
class MatrizQuad(Matriz):
    
    def __init__(self, n = None, dados = None):
        """Construtor"""
        self.validated = Matriz.typeValidation(self, n, n, dados)
        if self.validated:
            self.validated = Matriz.valueValidation(self, n, n, dados)
        Matriz.__init__(self, n, n, dados)
        self.tag = "q"
        
        return None
    
    def validate(self, n = None, dados = None):
        """Tenta transformar uma matriz vazia em uma matriz não vazia chamando novamente o construtor das classe"""
        self.__init__(n, dados)
        return None
    
    def trace(self):
        """Calcula o traço"""
        
        if self.validated == False:
            print("<func trace> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        A = self.matriz_to_array()
        x = np.trace(A)
        return x
    
    def det(self):
        """Calcula o determinante"""
        
        if self.validated == False:
            print("<func det> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        A = self.matriz_to_array()
        x = np.linalg.det(A)
        return x
        
    def inv(self):
        """Calcula a inversa"""
        
        if self.validated == False:
            print("<func inv> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        A = self.matriz_to_array()
        try:
            x = np.linalg.inv(A)
        except:
            print("<func inv> Erro: A matriz é singular")
            return None
        else:
            return x
    
class MatrizTriSup(MatrizQuad):
    
    def __init__(self, n = None, dados = None):
        """Construtor"""
        self.validated = Matriz.typeValidation(self, n, n, dados)
        if self.validated:
            self.validated = self.valueValidation(n, dados)
        Matriz.__init__(self, n, n, dados)
        self.tag = "ts"
        
        return None
    
    def validate(self, n = None, dados = None):
        """Tenta transformar uma matriz vazia em uma matriz não vazia chamando novamente o construtor das classe"""
        self.__init__(n, dados)
        return None
    
    def valueValidation(self, n, dados):
        """Validação especializada"""
        aux = dados[:]
        aux = aux + [0.0]*triangular(n-1)
        return Matriz.valueValidation(self, n, n, aux)
    
    def matriz_to_array(self):
        """Converte um objeto herdado de 'Matriz' em um array do Numpy"""
        
        if self.validated == False:
            print("<func matriz_to_array> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        matriz = []
        for i in range(self.n):
            matriz.append(self.m*[0.0])
        
        index = 0
        for i in range(self.n):
            for j in range(self.n):
                if i <= j:
                    matriz[i][j] = self.dados[index]
                    index += 1
        
        return np.array(matriz)
    
class MatrizTriInf(MatrizQuad):
    
    def __init__(self, n = None, dados = None):
        """Construtor"""
        self.validated = Matriz.typeValidation(self, n, n, dados)
        if self.validated:
            self.validated = self.valueValidation(n, dados)
        Matriz.__init__(self, n, n, dados)
        self.tag = "ti"
        
        return None
    
    def validate(self, n = None, dados = None):
        """Tenta transformar uma matriz vazia em uma matriz não vazia chamando novamente o construtor das classe"""
        self.__init__(n, dados)
        return None
    
    def valueValidation(self, n, dados):
        """Validação especializada"""
        aux = dados[:]
        aux = aux + [0.0]*triangular(n-1)
        return Matriz.valueValidation(self, n, n, aux)
    
    def matriz_to_array(self):
        """Converte um objeto herdado de 'Matriz' em um array do Numpy"""
        
        if self.validated == False:
            print("<func matriz_to_array> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        matriz = []
        for i in range(self.n):
            matriz.append(self.m*[0.0])
        
        index = 0
        for i in range(self.n):
            for j in range(self.n):
                if i >= j:
                    matriz[i][j] = self.dados[index]
                    index += 1
                    
        return np.array(matriz)

class MatrizDiag(MatrizTriInf, MatrizTriSup):
    
    def __init__(self, n = None, dados = None):
        """Construtor"""
        self.validated = Matriz.typeValidation(self, n, n, dados)
        if self.validated:
            self.validated = self.valueValidation(n, dados)
        Matriz.__init__(self, n, n, dados)
        self.tag = "d"
        
        return None
    
    def validate(self, n = None, dados = None):
        """Tenta transformar uma matriz vazia em uma matriz não vazia chamando novamente o construtor das classe"""
        self.__init__(n, dados)
        return None
    
    def valueValidation(self, n, dados):
        """Validação especializada"""
        aux = dados[:]
        aux = aux + [0.0]*triangular(n-1)
        return super().valueValidation(n, aux)
    
    def matriz_to_array(self):
        """Converte um objeto herdado de 'Matriz' em um array do Numpy"""
        
        if self.validated == False:
            print("<func matriz_to_array> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        matriz = []
        for i in range(self.n):
            matriz.append(self.m*[0.0])
        
        index = 0
        for i in range(self.n):
            matriz[i][i] = self.dados[i]
                    
        return np.array(matriz)
    
class MatrizSim(MatrizQuad):
    
    def __init__(self, n = None, dados = None):
        """Construtor"""
        self.validated = Matriz.typeValidation(self, n, n, dados)
        if self.validated:
            self.validated = self.valueValidation(n, dados)
        Matriz.__init__(self, n, n, dados)
        self.tag = "s"
        
        return None
    
    def validate(self, n = None, dados = None):
        """Tenta transformar uma matriz vazia em uma matriz não vazia chamando novamente o construtor das classe"""
        self.__init__(n, dados)
        return None
    
    def valueValidation(self, n, dados):
        """Validação especializada"""
        aux = dados[:]
        aux = aux + [0.0]*triangular(n-1)
        return Matriz.valueValidation(self, n, n, aux)
    
    def matriz_to_array(self):
        """Converte um objeto herdado de 'Matriz' em um array do Numpy"""
        
        if self.validated == False:
            print("<func matriz_to_array> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        matriz = []
        for i in range(self.n):
            matriz.append(self.m*[0.0])
        
        index = 0
        for i in range(self.n):
            for j in range(self.n):
                if i <= j:
                    matriz[i][j] = self.dados[index]
                    index += 1
                if i > j:
                    matriz[i][j] = matriz[j][i]
                    
        return np.array(matriz)
    
    def diag(self):
        """Calcula a diagonalização, retornando uma tupla contendo um matriz 
        diagonal de autovalores e uma matriz cujas colunas são os autovetores"""
        
        if self.validated == False:
            print("<func diag> Aviso: Não é possível operar com uma matriz vazia")
            return None
        
        A = self.matriz_to_array()
        decomp = np.linalg.eigh(A)
        
        lambdas = []
        for i in range(self.n):
            lambdas.append(float(decomp[0][i]))
        lambdas = MatrizDiag(self.n, lambdas)
        
        vectors = decomp[1]
        vectors = array_to_matriz(vectors)

        return (lambdas, vectors)
        
