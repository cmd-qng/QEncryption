
#~~~~~~~~~~~~~~~Encrypt~~~~~~~~~~~~~~~~
def Encrypt(filename, Key):
#Define Encrypt 
    file = open(filename, 'rb')
    #Open File
    data = file.read()
    #Read Data
    file.close()
    #Close File
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open('QE-' + filename, 'wb')
    #Create new file
    file.write(data)
    #Write to file
    file.close()
    #Close File
    
#~~~~~~~~~~~~~~~~~~~Decrypt~~~~~~~~~~~~~~~~~~~~
def Decrypt(filename, key):
    #Define Decrypt 
    file = open(filename, 'rb')
    #Open File
    data = file.read()
    #Read Data
    file.close()
    #Close File
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open(filename, 'wb')
    #Create new file
    file.write(data)
    #Write to file
    file.close()
    #Close File

#~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~
while True:
    print(
        '[*] Press 1 for Encryption \n [*] Press 0 for Decryption \n [*] Press 01 to exit ')
    choice = input('Insert Here : ')
    #Get Menu Input
    if choice.isdigit():
        if choice == '1':
            #encrypt
            key = int( input('Enter Key 1 - 255: '))
            #Ask user for a Key
            filename = input('Input Filename: ')
            # Ask user for file name
            Encrypt(filename, key)
        elif choice == '0':
            #decrypt
            key = int( input('Enter Key 1 - 255: '))
            #Ask user for a Key
            filename = input('Input Filename: ')
            # Ask user for file name
            Decrypt(filename, key)
        elif choice == '01':
            #exit
            print('Exiting...')
            break
        else:
            #error
            print('Error \n'
                  'Please insert 0 or 1 ')