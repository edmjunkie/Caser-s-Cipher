# Name: Ibrahim Stamili
# Section: N/A
# Date: 29/9/2016
# cipher.py

print "********** Caesar's Cipher **********"


def check_int(input):
    try:
        new_num = int(input)
        return True, new_num
    except ValueError:
        print 'error! shift value must be a valid integer'
        return False, input


def get_input():
    print 'enter phrase to encode:'
    phrase = raw_input('>> ')
    shift_val_correct = False
    while not shift_val_correct:
        shift_val = raw_input('shift value? ')
        shift_val_correct, shift_val = check_int(shift_val)
    return phrase, shift_val


def main():
    phrase, shift_val = get_input()
    encoded_phrase = ''
    for c in phrase:
        if str.isalpha(c):
            if str.isupper(c):
                xter_code = ord(c) - 65
                new_code = xter_code + shift_val
                x = (new_code % 26) + 65
                encoded_phrase = encoded_phrase + chr(x)
            else:
                xter_code = ord(c) - 97
                new_code = xter_code + shift_val
                x = (new_code % 26) + 97
                encoded_phrase = encoded_phrase + chr(x)
        else:
            encoded_phrase = encoded_phrase + c
    print '--------------'
    print 'ecoded phrase'
    print encoded_phrase


main()

