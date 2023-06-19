# a regular expression module
import re
#  random module to use randint
from random import *
# support for opening, manipulating, and saving many image file formats.
from PIL import Image
#  this is a syntax for the path of files used in windows
rexWin = "^[a-zA-Z]{1}[\:\/\w\W]+[\.]{1}[a-zA-Z]{3,6}"

# global list to store keys used in the program whether its random or chosen, it acts as dictionary for used keys.
global keys_list_Chosen
keys_list_Chosen = []
global keys_list_Ran
keys_list_Ran = []


# this is the main menu will be seen first to choose what they need to do with the images
def menu():
    # to handle any kind of exception during the execution of the program
    try:
        art3='''

                    ▒█▀▀█ █▀▀█ █▀▀▄ █▀▀ ▒█░░▒█ █▀▀█ █▀▀█ █▀▀ 
                    ▒█░░░ █░░█ █░░█ █▀▀ ▒█▒█▒█ █▄▄█ █▄▄▀ ▀▀█ 
                    ▒█▄▄█ ▀▀▀▀ ▀▀▀░ ▀▀▀ ▒█▄▀▄█ ▀░░▀ ▀░▀▀ ▀▀▀
        '''
        print(art3)
        print("Done BY:\n[1]Sarah AL abbas\n[2]Fatema al jarri \n[3]Shouq al hammam\n[4]Layal Abualsaud \n[5]Bushra aleid \n\n")
        while True:
            # to handle any kind of exception during the execution of the program
            try:
                ch = int(
                    input(
                        "choose from the following\n1- Encrypt image.\n2- Decrypt images\n3- print Random keys\n4- print Chosen keys\n5- Exit\nyour choice:"))
                print("-------")
                # this choice leads to the encryption menu
                if ch == 1:
                    encryptMenu()
                # this choice to the decrypt function
                elif ch == 2:
                    decryptHandlerCheck()
                # to print all the random keys.
                elif ch == 3:
                    printKeysRan()
                # to print all the chosen keys.
                elif ch == 4:
                    printKeysChoesn()
                # termination of the program
                elif ch == 5:
                    print(r'''                                                
                     ▀█▀ █░█ ▄▀█ █▄░█ █▄▀ █▄█ █▀█ █░█ ░ █▄▄ █▄█ █▀▀ ░
                     ░█░ █▀█ █▀█ █░▀█ █░█ ░█░ █▄█ █▄█ █ █▄█ ░█░ ██▄ ▄''')
                    break
                else:
                    print("Wrong option...Choose again 1-3")
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


# here is a menu that gives different choices for encrypting images
def encryptMenu():
    try:
        print('\n*********************')
        print('''\n\t                   
 █▀▄▀█ █▀▀ █▄░█ █░█
 █░▀░█ ██▄ █░▀█ █▄█\t''')
        print("\tEncryption \n")
        print('*********************')
        print(
            "choose key generation method:\n1- Random by the system.\n2- choose the Encryption key.\n3- return to menu")
        print("--------")
        ch = int(input("your choice:"))
        print("--------")
        # this choice leads random key encryption
        if ch == 1:
            encryptRandomHandler()
        # this choice leads chosen key encryption
        elif ch == 2:
            encryptChosenHandler()
        # returning to the main menu
        elif ch == 3:
            print("\tExiting the Encryption Menu\n____________________________________________")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)


# a function to generate a random key for encryption
def getKey():
    key = randint(1, 100)
    return key


# function that print Different choices of OS for the user
def OSmenu():
    print("\nChoose from the following\n(Are you using):\n1- Windows\n2- Other OS")


# function to create image files.
def SAVE(path):
    # try except to handle any issues when we try to open a path.
    try:
        # to open an image using the path passed to the function.
        im1 = Image.open(path)
        # letting the user enter the new path for the encrypted image.
        fname = input("Enter the path with new name: ").strip()
        # to avoid any errors, replace method used to replace the \\ with / because the save method works.
        fname = fname.replace("\\", "/")
        # save is a method used to save the encrypted image with the specified new path.
        im1.save(fname)
        # return the new path to used in other functions
        return fname
    except FileNotFoundError:
        msg = "Sorry, the file " + path + " does not exist."
        print(msg)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)


# method to print the keys from text file that contains the list of keys.
def printKeysRan():
    try:
        keylist = open('Randomkeys.txt', 'r')
        lines = keylist.read()
        keylist.close()
        print(lines)
    except Exception as e:
        print(e, "\nYou should encrypt at least 1 image in order to print the keys."
                 " Randomkeys.txt and Chosenkeys.txt stores encryption keys that have been previously used.\n")


# method to print the keys from text file that contains the list of keys.
def printKeysChoesn():
    try:
        keylist = open('Chosenkeys.txt', 'r')
        lines = keylist.read()
        keylist.close()
        print(lines)
    except Exception as e:
        print(e, "\nYou should encrypt at least 1 image in order to print the keys."
                 " Randomkeys.txt and Chosenkeys.txt stores encryption keys that have been previously used.\n")


# this is a function for encrypting images using the key specified by the user.
def encryptChosenHandler():
    try:
        print("---------------------")
        print("\n\n---------ENCRYPTION USING YOUR KEY---------\n\n")
        # calling the OS menu to chose from.
        OSmenu()
        ch = int(input("Your choice: "))
        # if the user using windows.
        if ch == 1:
            path = input(r'Enter path of Image : ').strip()
            # after accepting the path from the user search function is used
            # with the regex that we created to check the validity of the entered path.
            if re.search(rexWin, path):
                # encryptChosen called with path as argument.
                encryptChosen(path)
            # if the path was wrong print the else statement.
            else:
                print("couldn't find the path specified...")
        # for other OS such as mac
        elif ch == 2:
            path = input(r'Enter path of Image : ').strip()
            encryptChosen(path)
        else:
            print("Please Choose from 1-2.")

    except FileNotFoundError:
        msg = "Sorry, the file " + path + " does not exist."
        print(msg)
    except ValueError as e:
        print(e)
    except Exception:
        print('Error caught : ', Exception.__name__)


# this is a costume function for decrypting images using the key specified by the user.
def decryptHandlerCheck():
    try:
        print("\n\n-------------Decrypting Images with Your Key----------\n\n")
        OSmenu()
        ch = int(input("Your choice: "))
        if ch == 1:
            path = input(r'Enter path of Image : ').strip()
            if re.search(rexWin, path):
                # this the function for decrypting passing the path after it's been verified
                decryptK(path)
            else:
                print("couldn't find the path specified...")
        elif ch == 2:
            path = input(r'Enter path of Image : ').strip()
            decryptK(path)
        else:
            print("Wrong option. Choose from 1-2.\n_________________________\n")

    except FileNotFoundError:
        msg = "Sorry, the file " + path + " does not exist."
        print(msg)
    except ValueError as e:
        print(e)
    except Exception:
        print('Error caught : ', Exception.__name__)


# decryptK function used for the actual decryption process.
def decryptK(path):
    try:
        print("\nP.S: Make sure you're using the same key used in Encryption process.")
        print("----")
        #  takes the key as input from user.
        key = int(
            input('Enter Key for decryption of Image (key should be a number to preform xor encryption/decryption): '))
        # opening a file named fin from the specified path in read binary mode.
        fin = open(path, 'rb')
        # saving the content of the file in variable image
        image = fin.read()
        fin.close()
        # The bytearray() function returns a bytearray object.
        # It can convert objects into bytearray objects to ease the decryption/encryption process.
        image = bytearray(image)
        # for loop that use the enumerate function to decrypt/encrypt each byte using xor algorithm.
        for index, values in enumerate(image):
            image[index] = values ^ key
        # opening the path in write binary mode.
        fin = open(path, 'wb')
        # writing the decrypted/encrypted in the image.
        fin.write(image)
        fin.close()
        print('Decryption Done...')
        print("----------\n")
    except FileNotFoundError:
        msg = "Sorry, the file " + path + " does not exist."
        print(msg)
    except ValueError as e:
        print(e)

# this is a function for encrypting images using the key generated by the getKey() function.
def encryptRandomHandler():
    try:
        print("\n\n---------ENCRYPTION USING RANDOM KEY---------\n\n")
        OSmenu()
        ch = int(input("Your choice: "))
        try:
            if ch == 1:
                path = input(r'Enter path of Image : ').strip()
                if re.search(rexWin, path):
                    # calling the encryptRandom passing the path specified by the user.
                    encryptRandom(path)
                else:
                    print("couldn't find the path specified...")
            elif ch == 2:
                path = input(r'Enter path of Image : ').strip()
                encryptRandom(path)
            else:
                print("Please choose from 1-2.")

        except FileNotFoundError:
            msg = "Sorry, the file " + path + " does not exist."
            print(msg)
        except ValueError as e:
            print(e)

    except Exception:
        print('Error caught : ', Exception.__name__)


# function uses random key for Encryption.
def encryptRandom(path):
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    # calling the getKey() to generate the random key
    key = getKey()
    # to save the key used in a list
    keys_list_Ran.append(key)
    # print the key to notify the user of key used in Encryption.
    print('The key used : ', key)
    for index, values in enumerate(image):
        image[index] = values ^ key
    # gives the user the choice to save the file in another image with new path or not.
    ch = int(input("Do you want to save it in another file?\n1- Yes\n2- No\nYour choice: "))
    # if no the encrypted byte will be written within the original file.
    if ch == 2:
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Encryption Done...')
        print("--------\n")
    # if yes the encrypted byte will be written within the new path specified by the user.
    elif ch == 1:
        # here the new path will replace the original path in the decryption/encryption process.
        path = SAVE(path)
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Encryption Done...')
        print("--------\n")
    else:
        print("The encryption was unable to be performed, you may entered a wrong choice.")
    # let the user decide whether to decrypt the image, Return to the encryption menu or exit the whole program.
    ch = int(input('Choose from the following:\n1- Decrypt\n2- Return\n3- exit\nYour choice: '))
    print("--------")
    # if choice was to Decrypt call decryptRandom sending the key and the path
    if ch == 1:
        decryptRandom(key, path)
    # if choice was to Return call encryptMenu.
    elif ch == 2:
        encryptMenu()
    # to exit the program.
    elif ch == 3:
        exit(0)
    else:
        print("Wrong input..")
    # to create a file named keys.txt in write mode. 
    # for the purpose of writing the keys in the file.
    with open("RandomKeys.txt", "a+") as f:
        for key in keys_list_Ran:
            print(key, file=f)


# decryptRandom takes two arguments the key and the path to preform the decryption.
def decryptRandom(key, path):
    print("\n\n---------DECRYPTION USING RANDOM KEY---------\n\n")
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    print('Decryption Done...Exit')
    print("----------\n")


# encryptChosen is costume function takes the path as arguments and let the user choose the key.
def encryptChosen(path):
    try:
        print("---------------------")
        ke = int(
            input('Enter Key for encryption of Image (key should be a number to preform xor encryption/decryption): '))
        print("---------------------")
        print('Key for Encryption : ', ke)
        # to save the key used in a list
        keys_list_Chosen.append(ke)
        # to create a file named keys.txt in write mode. 
        # for the purpose of writing the keys in the file.
        with open("ChosenKeys.txt", "a+") as f:
            for key in keys_list_Chosen:
                print(key, file=f)
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ ke
        ch = int(input("Do you want to save it in another file?\n1- Yes\n2- No\nYour choice: "))
        if ch == 2:
            fin = open(path, 'wb')
            fin.write(image)
            fin.close()
            print('Encryption Done...')
            print("---------------------")
        elif ch == 1:
            path = SAVE(path)
            fin = open(path, 'wb')
            fin.write(image)
            fin.close()
            print('Encryption Done...')
            print("---------------------")
        else:
            print("The procedure was unable to be performed.")
        ans = int(input('Choose from the following:\n1- Decrypt\n2- Return\n3- exit\nYour choice: '))
        print("---------------------\n")
        if ans == 1:
            decryptChosen(ke, path)
        elif ans == 2:
            encryptMenu()
        # to exit the program.
        elif ans == 3:
            exit(0)
    except FileNotFoundError:
        msg = "Sorry, the file " + path + " does not exist."
        print(msg)
    except ValueError as e:
        print(e)


def decryptChosen(key, path):
    print("---------------------")
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    print("Picture:" + path + "\nKEY for Decryption: " + str(key))
    print('Decryption Done...')
    print("---------------------\n")


# this where the program start calling the main function
if __name__ == '__main__':
    menu()