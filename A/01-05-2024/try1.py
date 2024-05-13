amount=34267
notes_2k = amount // 2000
if notes_2k > 0:
    print("2000 -", notes_2k)
rem_amount= amount % 2000

notes_500 = rem_amount //500
if notes_500 > 0:
    print("500 -", notes_500)
rem_amount= amount % 500

notes_200 = rem_amount //200
if notes_200 > 0:
    print("200 -", notes_200)
rem_amount= amount % 200

notes_100 = rem_amount //100
if notes_100 > 0:
    print("100 -", notes_100)
rem_amount= amount % 100

notes_50 = rem_amount //50
if notes_50 > 0:
    print("50 -", notes_50)
rem_amount= amount % 50

notes_20, rem_amount = divmod(rem_amount,20)
if notes_20 > 0:
    print("20 -", notes_20)


notes_10, rem_amount = divmod(rem_amount,10)
if notes_10 > 0:
    print("10 -", notes_10)