def decode(pw):
    decoded_password=""
    for digit in pw:
        decoded_digit=str((int(digit)-3)%10)
        decoded_password += decoded_digit
    return decode

def main():
    decoded_password = decode(pw)
if __name__ == '__main__':
    main()