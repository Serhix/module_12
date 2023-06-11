from instructions_func import choise_comand
from instructions_func import address_book
import pickle



def main():

    try:
        while True:
            request = input('- ').lower()
            result = choise_comand(request)
            print(result)
            if result == 'Good bye!':
                break
    finally:    
        with open('address_book.dat', 'wb') as file:
            pickle.dump(address_book, file)


if __name__ == '__main__':
    main()


