
plainText = raw_input("What is your plaintext? ")
shift = int(raw_input("What is your shift? "))

def caesar(plainText, shift):

    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
        cipherText = "317336, 1696274, 425598, 1007448, 1069008, 1340288, 346128, 663858, 392496, 2013024, 734808, 1233758, 1268616, 1069008, 1233758, 948296, 142008, 1653936, 948296, 516368, 133974, 1612308, 1133024, 948296, 392496, 1739328, 1452776, 948296, 641264, 133974, 497274, 1783104, 1268616, 1452776, 1199544, 948296, 1531158, 133974, 1377114, 1918824, 1452776, 133974, 1414608, 1268616, 1007448, 1377114, 1653936, 948296, 556008, 619188, 948296, 1037924, 619188, 1739328, 1696274, 1133024, 392496, 133974, 1612308, 1069008, 1268616, 1452776, 1199544, 290184, 47064, 2110256"
        cipherText += finalLetter

    print= "Your ciphertext is: ", cipherText

    return cipherText

caesar(plainText, shift)
