1       True and True
            # True
2.      False and True
            # False
3.      1 == 1 and 2 == 1
            # False
4.      "test" == "test"
            # True
5.      1 == 1 or 2 != 1
            # True
6.      True and 1 == 1
            # True
7.      False and 0 != 0
            # False
8.      True or 1 == 1
            # True
9.      "test" == "testing"
            # False
10.     1 != 0 and 2 == 1
            # False
11.     "test" != "testing"
            # True
12.     "test" == 1
            # False
13.     not (True and False)
            # True and False == False, so not makes it True
14.     not (1 == 1 and 0 != 1)
            # 1 == 1 and 0 != 1 is True, so not makes it False
15.     not (10 == 1 or 1000 == 1000)
            # 1000 == 1000 is True, so not makes it False
16.     not (1 != 10 or 3 == 4)
            # 1 != 10 is True, so not makes it False
17.     not ("testing" == "testing" and "Zed" == "Cool Guy")
            # "Zed" == "Cool Guy" is False, so not makes it True
18.     1 == 1 and (not ("testing" == 1 or 1 == 0))
            # "testing" == 1 is False and 1 == 0 is False, so not makes it True
            #  1 == 1 is True, so True and True makes it True
19.     "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
            # 3 == 3 is True, so not makes it False
            # "chunky" == "bacon" is False, so False and False is False
20.     3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
            # "testing" == "testing" is True, so not makes it True
            # 3 == 3 is True, True and True makes it True
