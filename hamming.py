import numpy as np


def verificationBinar(word):
    array = list(word)
    filtered = list(filter(lambda x: int(x) > 1, array))
    return True if len(filtered) > 0 else False

def verificationLen(word):
    if(len(word) > 4 or verificationBinar(word)):
        print("Invalid word format")
        return False
    else: return True

def sumF2(x):
   return 0 if x%2==0 else 1

def ConvertToVector(word):
        array  = list(word)
        result = map(lambda x: int(x),array)
        vector = np.array(list(result))
        return vector

def XorApplyAndMult(mat1, mat2):
    result = np.dot(mat1, mat2)
    XorApply = list(map(sumF2, list(result)))
    return XorApply

def codification(word=""):
    generatorMatrix = np.array([[1,0,0,0,0,1,1], 
                                [0,1,0,0,1,0,1],
                                [0,0,1,0,1,1,0],
                                [0,0,0,1,1,1,1]])
    if(verificationLen(word)):
        vector = ConvertToVector(word)
        Xor = XorApplyAndMult(vector, generatorMatrix)
        XorStr = list(map(lambda x : str(x), Xor))
        string = "". join(XorStr)
        return string

def correctErrors(word):
    paritycheck = np.array([[0, 0 ,0 ,1 ,1 ,1 ,1], 
                            [0, 1, 1, 0, 0, 1 ,1],
                            [1, 0, 1, 0, 1, 0, 1]])

    vector = ConvertToVector(word)
    newVector = list(map(lambda x: str(x), vector))
    vectorTrans = np.transpose(vector)
    result = XorApplyAndMult(paritycheck, vectorTrans)
    resultSerialize = list(map(lambda x: str(x), result))
    if(result == [0,0,0]):
        alert = "no hay ningún error en el código" 
        return alert
    else:
        resultStr = "".join(resultSerialize)
        bit = int(resultStr, 2)
        vectorCorrected = []
        for i in range(1, len(newVector)+1):
            if(i == bit):
                valor = '0' if newVector[i-1]=='1' else '1'
                vectorCorrected.append(valor)
            else:
                vectorCorrected.append(newVector[i-1])
        vectorCorrectedStr = "".join(vectorCorrected)                 
        return vectorCorrectedStr

while True:
    option  =input("escoge una opción: \n 1) codificar en Hamming \n 2) corregir (distancia minima 3) \n 3) Salir: \n")
    if(option == "1"):
        word = input("introduzca la palabra -> ")
        print("la codificación en Hamming es -> " + codification(word))
    elif(option == "2"):
        word = input("introduzca la palabra a corregir -> ")
        print("corrección -> "+ correctErrors(word))
    else:
        print("gracias por usar el programa ;)")
        break