class Faction:
    firstEnemy= None
    secondEnemy = None

    def __init__(self,name,numOfUnits,attackPoint,healthPoint,regNumber):
        self.name=name
        self.numOfUnits=numOfUnits
        self.attackPoint=attackPoint
        self.healthPoint=healthPoint
        self.regNumber=regNumber
        self.totalHealth = (self.healthPoint*self.numOfUnits)
        self.isAlive=True
    
    def AssignEnemies(self,obj1,obj2):
        self.firstEnemy = obj1
        self.secondEnemy = obj2

    def PerformAttack(self):
        pass

    def ReceiveAttack(self):
        pass

    def PurchaseWeapons(self):
        pass

    def PurchaseArmors(self):
        pass


    def Print(self):
        statusFunc = lambda x : "Alive" if(x==True) else "Defeated"

        print("Faction Name: "+ self.name)
        print("Status: " + statusFunc(self.isAlive))
        print("Number Of Units: " + str(self.numOfUnits))
        print("Attack Point: "+str(self.attackPoint))
        print("Health Point: "+str(self.healthPoint))
        print("Unit Regen Number: "+str(self.regNumber))
        print("Total Health: "+str(self.totalHealth))

    def EndTurn(self):

        if(self.numOfUnits <= 0):
            if(self.numOfUnits < 0):
                self.numOfUnits = 0
                self.isAlive = False
            else:
                self.isAlive= False


class Orcs(Faction):
    def __init__(self,name,numOfUnits,attackPoint,healthPoint,regNumber):
        super().__init__(self,name,numOfUnits,attackPoint,healthPoint,regNumber)

    def PerformAttack(self):
        if(super().secondEnemy != None):
            (self.numOfUnits)*(7/10)
        else:
            #attacks with all units
            super().firstEnemy.totalHealth -= self.numOfUnits*self.attackPoint
    
    def ReceiveAttack(self):
        pass


    def PurchaseWeapons(self):
        pass
    
    def PurchaseArmors(self):
        pass


    def Print(self):
        print("Stop running, you will only die tired!")
        super().Print()


class Dwarves(Faction):
    def __init__(self, name, numOfUnits, attackPoint, healthPoint, regNumber):
        super().__init__(name, numOfUnits, attackPoint, healthPoint, regNumber)


    def PerformAttack(self):
        pass
    
    def ReceiveAttack(self):
        pass


    def PurchaseWeapons(self):
        pass
    
    def PurchaseArmors(self):
        pass


    def Print(self):
        print("Taste the power of our axes!")
        super().Print()



class Elves(Faction):

    def __init__(self, name, numOfUnits, attackPoint, healthPoint, regNumber):
        super().__init__(name, numOfUnits, attackPoint, healthPoint, regNumber)
    
    def PerformAttack(self):
        pass
    
    def ReceiveAttack(self):
        pass


    def PurchaseWeapons(self):
        pass
    
    def PurchaseArmors(self):
        pass


    def Print(self):
        print("You cannot reach our elegance.")
        super().Print()
    


class Merchant:
    firstFaction = None
    secondFaction = None
    thirdFaction = None

    def __init__(self,startWeaponPoint,startArmorPoint):
        self.startWeaponPoint = startWeaponPoint
        self.startArmorPoint = startArmorPoint
        self.revenue = 0
        self.weaponPoint = 10
        self.armorPoint = 10

    def AssignFactions(self,fact1,fact2,fact3):
        self.firstFaction = fact1
        self.secondFaction = fact2
        self.thirdFaction = fact3
    
    def SellWeapons(self,wp,fact):
        if(wp > self.weaponPoint):
            print("You try to sell more weapons than you have in possession.")
            return False
        elif(fact.isAlive == False):
            print("The faction you want to sell weapons is dead!")
            return False
        else:
            print("Weapons sold!")
            return True


    def SellArmors(self,ap,fact):
        if(ap > self.armorPoint):
            print("You try to sell more armors than you have in possession.")
            return False
        elif(fact.isAlive == False):
            print("The faction you want to sell armors is dead!")
            return False
        else:
            print("Armors sold!")
            return True


    def EndTurn(self):
        self.weaponPoint = self.startWeaponPoint
        self.armorPoint = self.startArmorPoint


firstEnemy = Faction("EnemyOne",20,15,30,10)
secondEnemy = Faction("EnemyTwo",30,20,25,15)
MainFaction = Faction("Default",50,30,35,25)
MainFaction.AssignEnemies(firstEnemy,secondEnemy)