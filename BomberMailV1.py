# -*- coding: utf-8 -*-
# By :                         EnzoZertio / HaXor DeRoutine    
# Fb :                              Enzo Zertio           
# Github :                  https://github.com/EnzoZertio
# Gmail :                         enzozertio@gmail.com 
############################################# Import some lib #############################
import os
import random
import smtplib
import sys
import getpass
import time
############################ JUST a SHIT ###################
print ('''\033[1;31m  \033[97m 
 mmmmmm                      mmmmmm                 m      "          
 #      m mm   mmmmm   mmm       #"  mmm    m mm  mm#mm  mmm     mmm  
 #mmmmm #"  #     m"  #" "#    m#   #"  #   #"  "   #      #    #" "# 
 #      #   #   m"    #   #   m"    #""""   #       #      #    #   # 
 #mmmmm #   #  #mmmm  "#m#"  ##mmmm "#mm"   #       "mm  mm#mm  "#m#" 
                                                         By EnzoZertio
''') 
print(" ")
#########################   USER INFO #########################
user = raw_input("Marque ton adresse gmail :")
passworde = getpass.getpass('Marque ton mot de passe :')
print(" ")
victime = raw_input('adresse email de la victime :')
message = raw_input('Quel est ton message ? :')
print(" ")
hani = input('Nombre de Spams à envoyé : ')
print(" ")
print("[*]Sending : ")
############################### SMTP_SERVER INFO ##################
smtp_server = 'smtp.gmail.com'
port = 587

##########################  Login ############################
try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passworde)
###################### SENDING #########################################
    for i in range(1, hani+1):
        subject = "S̵̨͙͇͓͕̤̝̽͆̓̓͘p̵̪͉̠̒͛̒̑̔̏̒̀̓̏̽͂̚͝a̶̝͇̭̫̬͔̪͖̿͑̀͗̉́̌̅́̒̅͑͋͝m̴̡̨̧̖̏̅̇͒͐͝m̷̤̋̇e̶̛̙͇͉͙͇͓̖͓̭̟̥̠͋̇͊̓̓̌͛́͑̅̈́̊͜͝͠d̴̨̧͔̫͈̜̠̹̫̗͉̥̲́͂̆́̈́̈́̽̐̽͐̚͜ ̶̭͓͉̪̻̩̪͕͗͑͜ͅb̸͈̘̦̪́̈́̈́̑̀̔̈́̇͛͒͂͑̀͘̚y̸̹̑́̈́́͂̌́̓͊̋͘͝ ̵̡̡̬̞̠̖̟̠̼̓̌̀̍̈́̄̌̀̂̔̾̒̈́͑̓͜ͅĘ̶̙̩̪̗̿̀͊̐̓͆̄ͅṋ̷̡̛̝̪̪̣̦̰̥͈͚̭̐̐̍̈́̔͒̈́̅̿̽̒̀̕͜͝ẑ̸̢̢̰̜͇͓͉̫̟̻̝̊̅o̵̢̞͇͔̜͙̜̩̭̗̪̜͆̎͜͜ͅZ̴͚̗̦̞͒͗͋͒́̇ë̶̳́̃͑̓̀́̓r̷̢̽̂̏͗̅͑́͋̇͝t̶̹̥͚̮̜̼͓̦̮̦͖̄͛̇̒͛͑͒͒̑̒̽͠į̷̠͎͚̬̪͙̘̯͚̄͊͆̀͑̊̋̉̉̕͝͠͝͠ō̷͓͊͆̀̚̕"
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user,victime,msg)
        print ("[✔] Email Envoyé %i") % i
        sys.stdout.flush()
    server.quit()
    print ('[✔] Tous les messages ont été envoyés ')
    
    
except KeyboardInterrupt:
    print ('[✘] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("[✘]Error :")
    print ('[✘]Le mot de passe ou l adresse gmail que tu as entré précédemment est incorrect.')
    print ("Regarde si dans les paramètres de ton compte gmail , tu as bien activé l option Autoriser les applications moins sûr ")
    sys.exit()


