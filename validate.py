import bcrypt

hashed_password = b'$2b$12$on1qBMWR46nfcy8mdkT3MODj5U40UijKus0QQHEFkMBSLoUi/zFiy' # taken form main hashed password

def validate(hashed_password):

    entered_password = input("Enter Password to Login: ")
    entered_password = bytes(entered_password, encoding='utf-8')
    cnt=0
    while(cnt!=5):

        if (bcrypt.checkpw(entered_password, hashed_password)):
            print("Login Successful, Welcome Sir!!!")
            break
        if(cnt==4):
            print("Last Chance Entered Correct Password")
            entered_password = input("Enter Password to Login: ")
            entered_password = bytes(entered_password, encoding='utf-8')
            cnt+=1
        else:
            print("Invalid Password, Try Again!!")
            cnt+=1
            entered_password = input("Enter Password to Login: ")
            entered_password = bytes(entered_password, encoding='utf-8')

if __name__ == '__main__':
    validate(hashed_password)