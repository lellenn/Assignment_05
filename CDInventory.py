#------------------------------------------#
# Title: CDInventory.py
# Desc: Added Functionality in a CD Inventory
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# LWarner, 2021-Nov-11, Modified and added code
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dicts to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        print('loading data from file')
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
           lstRow = row.strip().split(',')
           dicRow = {'Artist': lstRow[0], 'Title': lstRow[1]}
           lstTbl.append(dicRow)
        objFile.close()  
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        objFile = open(strFileName, 'a')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'Artist': strArtist, 'Title': strTitle,}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('CD Title, Artist')
        for row in lstTbl:
           strRow = ''
           for item in row.values():
               strRow += str(item) + ','
           strRow = strRow[:-1]
           print(strRow)
    elif strChoice == 'd':
        item = input('Enter the Artist you would like to delete: ')
        if item in strFileName:
            del strFileName[item]
            print('That item has been deleted')
        else:
            print('That item does not exist in the inventory.')
            pass
    elif strChoice == 's':
      # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')