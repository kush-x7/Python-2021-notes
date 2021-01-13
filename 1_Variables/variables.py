# How to initilize a variable

    s = 3600                  # integer
    seconds = 3600            # integer
    seconds_per_hour = 3600   # integer

    name = "kush"             #string

    choice =True              #boolean


# How to print a variable

    print(s)                # output-> 3600
    print(seconds)          # output-> 3600
    print(seconds_per_hour) # output-> 3600

# Things to remember
    # 1-> correct way for naming variable
            KUSH
            kush
            _kush
            kush_age

    # 2-> Wrong way for naming variable
        9lives
        99_balloons
        2beOrNot2BeInadditiontoEng

    # 3-> Case sensetive
        seconds =3600
        print(SECONDS)   #it will show error
                         # name 'SECONDS' is not defined

    # 4-> Never initilize an empty variable
        hours  #Wrong  because you have to give some value to store

        hours = 0  #correct
        hr = ""    #correct

    # 5-> You can change value later on
        num =65
        num =23

# We can save a variable in a variable

    final = s + s
    print(final)             #->18
