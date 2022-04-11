# Console Application to test saving comments after asking for a password

from hashlib import sha256

hsh = '848bd78742f569ec15384f796857898594569b5a9edab251033bee5219726e85'
comment_list = []

print('Great Comment Saver version 1.0')
print('Available commands: comment, list, exit')

def comment(): #BP6
    last_comment = input('Please enter your comment: ')
    entered_password = input('Password: ')
    entered_password_hash = sha256(entered_password.encode()).hexdigest()
    if(entered_password_hash == hsh): #BP4
        print('Correct password. Comment added to the list of comments.')
        global comment_list
        comment_list = comment_list + [last_comment] #BP2
        return 'COMMENTADDSUCCESS'
    elif(entered_password != hsh):
        wrong_pw_input = input('Wrong password. Do you want to try again? (Y/N): ')
        if(wrong_pw_input == 'Y' or wrong_pw_input == 'y'):
            comment()
        elif(wrong_pw_input == 'N' or wrong_pw_input == 'n'):
            return 'TERMINATE'

def showlist():
    for i in comment_list:
        print(i) #BP3

def main():
    while True: #BP5
        command = input('>>>')
        if command == 'exit':
            break
        elif command == 'comment':
            comment()
        elif command == 'list':
            showlist()
        else:
            print("\""+command+"\" is an unrecognized command.") #BP1

main()