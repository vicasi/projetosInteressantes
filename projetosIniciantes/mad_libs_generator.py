from re import I


def madLibGenerator():
    loop = 1
    while loop < 10:
        noun = input("Choose a noun: ")
        p_noun = input("Choose a plural noun: ")
        noun2 = input("Choose a noun: ")
        place = input("name a place: ")
        adjective = input("Choose an adjective (Describing word): ")
        noun3 = input("Choose a noun: ")
        print('-------------------------------------')
        print("Be kind to your",noun,"- footed", p_noun)
        print ("For a duck may be somebody's", noun2,",")
        print ("Be kind to your",p_noun,"in",place)
        print ("Where the weather is always",adjective,".")
        print ()
        print ("You may think that is this the",noun3,",")
        print ("Well it is.")
        print ("------------------------------------------")
        playMore = input('wish to continue?(yes/no) ')
        if playMore == 'yes':
            loop = 1
        else:
            loop = 10

if __name__ == '__main__':
    madLibGenerator()
