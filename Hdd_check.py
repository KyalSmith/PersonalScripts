import os
import datetime

def main():

    low_drives_found = False

    computer_name = str(os.popen("hostname").read())

    val = str(os.popen("df -h").read())

    val = val.split("\n")



    for count,row in enumerate(val):

        val[count] = row.split()

        if row.__len__() == 0:
            del val[count]



    output_message = "Warning Low harddrive space on: " + computer_name+ "\n\nThe Following Drives are low:\n\n Drives:\tUsage:\t\tMount Point:\n"

    for row in val:

        if row[0] == "/dev/sda3" or row[0] == "/dev/sdb1" or row[0] == "/dev/sda2" or row[0] == "data:/spreemedia":

            perc_used = int(row[4].strip('%'))

            if perc_used > 80:

                low_drives_found = True

                output_message += row[0] + "\t" + str(perc_used) + "%\t\t"+row[5] +"\n"


    if low_drives_found:
        print(output_message)





if __name__=="__main__":
    main()