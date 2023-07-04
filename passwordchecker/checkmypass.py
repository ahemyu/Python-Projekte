import requests  # to make requests to the api
import hashlib  # to hash the password
import sys  # to get the arguments from the command line


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char  # url to get the data from the api
    res = requests.get(url)
    if res.status_code != 200:  # if the status code is not 200 raise an error
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_pw_leaks_count(hashes, hash_to_check):
    # splitlines() to split the text into lines and then split the lines at the : to get the hash and the number of leaks in a tuple
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:  # h is the hash and count is the number of leaks
        if h == hash_to_check:  # if the hash is the same as the hash we are looking for return the number of leaks
            return count
    return 0


def pwned_api_check(password):  # function to check if the password is leaked

    sha1_pw = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  # hexdigest() to convert sha1-Object to hex
    first_5_chars, tail = sha1_pw[0:5], sha1_pw[5:]  # save first 5 chars in var and the rest in tail
    response = request_api_data(first_5_chars)  # call the other function
    number_of_leaks = get_pw_leaks_count(response, tail)
    return number_of_leaks


def main(file):  # args is the list of arguments that we pass to the script
    # for password in args:
    #     count = pwned_api_check(password)
    #     if count != 0:  # if the password is leaked print the number of leaks
    #         print(f'{password} was found {count} times... you should probably change your password!')
    #     else:  # if the password is not leaked print that it is not leaked
    #         print(f'{password} was NOT found. Carry on!')

    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            count = pwned_api_check(line)
            if count != 0:
                print(f'{line} was found {count} times... you should probably change your password!')
            else:
                print(f'{line} was NOT found. Carry on!')


main("passwordchecker/pws.txt")




