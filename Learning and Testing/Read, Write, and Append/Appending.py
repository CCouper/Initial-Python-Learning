
appendMe = "\nNew bit of information"

appendFile = open("Appending.txt", "a")
appendFile.write(appendMe)
appendFile.close()
