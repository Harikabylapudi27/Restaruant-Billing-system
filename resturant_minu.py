from datetime import datetime
lists="""
Panner Butter Masala = 180
Vegetable Biriyani   = 130
Chicken Biriyani     = 180
Chapathi             = 40
South Indian Thali   = 210
Cool Drinks          = 50
"""
Price=0
TotalPrice=0
FinalPrice=0
ilist=[]
qlist=[]
plist=[]
items={"Panner Butter Masala":180,"Vegetable Biriyani":130,"Chicken Biriyani":180,
"Chapathi":40,"South Indian Thali":210,"Cool Drinks":50}
option=int(input("If you show list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    item=int(input("If you want to any item press 1 or 2 for exit:"))
    if item==2:
        break
    if item==1:
        item=input("Enter your item:")
        Quantity=int(input("enter how much quantity:"))
        if item in items.keys():
            Price=Quantity*(items[item])
            TotalPrice+=Price
            ilist.append(item)
            qlist.append(Quantity)
            plist.append(Price)
            gst=(TotalPrice*5)/100
            FinalPrice=TotalPrice+gst
        else:
            print("Sorry you entered item is not available now")
    else:
        print("Enter wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=="yes":
        print(25*"=","Speedy Eats",25*"=")
        print(25*" ","Gajuwaka")
        print(40*" ",datetime.now())
        print(75*"-")
        print("sno",8*" ","items",8*" ","Quantity",3*" ","price")
        print(i,8*" ",ilist[i],3*" ",qlist[i],8*" ",plist[i])
        print(75*"-")
        print(40*" ","TotalPrice:","Rs",TotalPrice)
        print("Gst amount",40*" ","Rs",gst)
        print(75*"-")
        print(40*" ","FinalPrice:","Rs",FinalPrice)
        print(75*"-")
        print(20*" ","Thanks For Visiting")
        print(75*"-")
            
