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
        alert = "There is no error in the given word" 
        return alert
    else:
        resultStr = "".join(resultSerialize)
        bit = int(resultStr, 2)
        vectorCorrected = []
        for i in range(1, len(newVector)+1):
            if(i == bit):
                value = '0' if newVector[i-1]=='1' else '1'
                vectorCorrected.append(value)
            else:
                vectorCorrected.append(newVector[i-1])
        vectorCorrectedStr = "".join(vectorCorrected)                 
        return vectorCorrectedStr

while True:
    option = input("Choose an option: \n 1) Codificate in Hamming  \n 2) Correcting the code  \n 3) Exit \n : ")
    if(option == "1"):
        word = input("Input the word -> ")
        print("The Hamming Codification is -> " + codification(word))
    elif(option == "2"):
        word = input("Input the word to correct -> ")
        print("Correction -> "+ correctErrors(word))
    else:
        print("Thanks for use the program ;)")
        break