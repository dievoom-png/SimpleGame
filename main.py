import random
import cv2
import sys

bag1 = 10
bag2 =10
bag3 = 10
counter = 0
while bag1 > 0 or bag2 > 0 or bag3 > 0:
    while counter % 2 == 0:
        player = 1
        counter = counter + 1

        user_bag = int(input("please select the bag"))

        if user_bag == 3 or user_bag == 2 or user_bag == 1:
            items = int(input("please type the number of items"))
            if user_bag == 1 and bag1 <= 0:
                print("the bag is empty please select another bag")
            if user_bag == 2 and bag2 <= 0:
                print("the bag is empty please select another bag")
            if user_bag == 3 and bag3 <= 0:
                print("the bag is empty please select another bag")
        else:
            print("enter a valid bag")
            counter = counter -1

        if user_bag == 1 and bag1 > 0 and bag1 - items >= 0:
            print("you took " + str(items) + " from " + str(user_bag))
            bag1 = bag1 - items
        elif user_bag == 2 and bag2 > 0 and bag2 - items >= 0:
            print("you took " + str(items) + " from " + str(user_bag))
            bag2 = bag2 - items
        elif user_bag == 3 and bag3 > 0 and bag3 - items >= 0:
            print("you took " + str(items) + " from " + str(user_bag))
            bag3 = bag3 - items
        else:
            print("enter a valid number")
            counter = counter - 1

        print(bag1)
        print(bag2)
        print(bag3)
        break

    while counter % 2 != 0:
        player = 2
        counter = counter + 1

        user_bag = random.randint(1, 3)
        items = random.randint(1, 5)

        if user_bag == 1 and bag1 > 0 and bag1 - items >= 0:
            print("the computer took " + str(items) + " from " + str(user_bag))
            bag1 = bag1 - items
        elif user_bag == 2 and bag2 > 0 and bag2 - items >= 0:
            print("the computer took " + str(items) + " from " + str(user_bag))
            bag2 = bag2 - items
        elif user_bag == 3 and bag3 > 0 and bag3 - items >= 0:
            print("the computer took " + str(items) + " from " + str(user_bag))
            bag3 = bag3 - items
        else:
            counter = counter - 1

        print(bag1)
        print(bag2)
        print(bag3)
        break



if player != 1:
    print("YOU WON!!")

    img = cv2.imread("win.jpeg")
    if img is None:
        sys.exit("Could not read the image.")
    cv2.imshow("Display window", img)
    k = cv2.waitKey(0)
else:
    img = cv2.imread("lose.jpg")
    if img is None:
        sys.exit("Could not read the image.")
    cv2.imshow("Display window", img)
    k = cv2.waitKey(0)
    print("YOU LOST")
