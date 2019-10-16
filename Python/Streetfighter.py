class Person:
  def __init__(fighter, name,country ,age,Bio,moveset):
    fighter.name = name
    fighter.country = country
    fighter.age = age
    fighter.Bio=Bio
    fighter.moveset=moveset
    

  def myfunc(fighter):
    print("Your Fighter is: " + fighter.name, "Country: "+ fighter.country ,  fighter.age
         , "BIO:"+fighter.Bio, "MoveSet: "+fighter.moveset  )

Cammy = Person("Cammy,", "Great Britan,",26, "Delta Red, ","Spiral Arrow, Cannon Drill, Spin Driver Smasher " )
Ken = Person("Ken,", "USA,", 23, "Martial Artist, ", "Hadoken, Dragon Punch, Hurricane Kick")


Cammy.myfunc()
Ken.myfunc()
