if __name__ == '__main__':





    for bottles in range(99):
        one=str(98-bottles)

        if one==str(0):
            one = "no more"

        print(str(99-bottles)+ "bottles of beer on the wall, "+ str(99-bottles)+ "bottles of beer."+
"Take one down and pass it around," + one + "bottles of beer on the wall.")


        if bottles==98:
            print("No more bottles of beer on the wall, no more bottles of beer."+
"Go to the store and buy some more, 99 bottles of beer on the wall.")

