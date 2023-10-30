def encode(pw):
    encoded_pw = ''
    for i in range(len(pw)):
        encoded_pw += str(((int(pw[i]) + 3) % 10))

    return encoded_pw


def decode(pw):
    decoded_password = ""
    for digit in pw:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decode

def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')

        user_option = input('Please enter an option: ')

        if user_option == '1':
            password = input('Please enter your password to encode: ')
            encoded_pw = encode(password)
            print('Your password has been encoded and stored!')

        elif user_option == '2':
            print('The encoded password is '+encoded_pw+', and the original password is '+decode(encoded_pw)+'.')


        else:
            break

if __name__ == '__main__':
    main()