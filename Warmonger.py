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
        return self.numOfUnits * self.attackPoint

    def ReceiveAttack(self,attack):
        self.numOfUnits -= int(attack)

    def PurchaseWeapons(self,newWeapon):
        self.attackPoint += int(newWeapon)

    def PurchaseArmors(self,newArmor):
        self.healthPoint += int(newArmor)


    def Print(self):
        statusFunc = lambda x : "Alive" if(x==True) else "Defeated"

        print("Faction Name: "+ self.name)
        print("Status: " + statusFunc(self.isAlive))
        print("Number Of Units: " + str(self.numOfUnits))
        print("Attack Point: "+str(self.attackPoint))
        print("Health Point: "+str(self.healthPoint))
        print("Unit Regen Number: "+str(self.regNumber))
        print("Total Health: "+str(self.totalHealth)+"\n")

    def EndTurn(self):
        self.numOfUnits += self.regNumber

        if(self.numOfUnits <= 0):
            if(self.numOfUnits < 0):
                self.numOfUnits = 0
                self.isAlive = False
            else:
                self.isAlive= False
        self.totalHealth = self.numOfUnits * self.healthPoint


class Orcs(Faction):
    def __init__(self,name,numOfUnits,attackPoint,healthPoint,regNumber):
        super().__init__(name,numOfUnits,attackPoint,healthPoint,regNumber)

    def PerformAttack(self):
        if(self.firstEnemy.isAlive and self.secondEnemy.isAlive):
            if(self.firstEnemy.__class__.__name__ == "Dwarves"):
                self.firstEnemy.ReceiveAttack(super().PerformAttack()*0.7,self)
                self.secondEnemy.ReceiveAttack(super().PerformAttack()*0.3,self)
            elif(self.firstEnemy.__class__.__name__ == "Elves"):
                self.firstEnemy.ReceiveAttack(super().PerformAttack()*0.3,self)
                self.secondEnemy.ReceiveAttack(super().PerformAttack()*0.7,self)
            else:
                print('Something has gone wrong!')
        elif(self.firsEnemy.isAlive and not self.secondEnemy.isAlive):
            self.firstEnemy.ReceiveAttack(super().PerformAttack(),self)
        elif(not self.firstEnemy.isAlive and self.secondEnemy.isAlive):
            self.secondEnemy.ReceiveAttack(super().PerformAttack(),self)
        else:
            print('All enemies are dead! ')



    def ReceiveAttack(self,attack,attacker):
        if(attacker.__class__.__name__ == "Dwarves"):
            super().ReceiveAttack((attack*(0.8))/(self.healthPoint))
        elif(attacker.__class__.__name__ == "Elves"):
            super().ReceiveAttack((attack*(0.75))/(self.healthPoint))
        else:
            print('Something has gone wrong')

    def PurchaseWeapons(self,weapon):
        super().PurchaseWeapons(2*weapon)
        return 20*weapon
    
    def PurchaseArmors(self,armor):
        super().PurchaseArmors(3*armor)
        return armor


    def Print(self):
        print("Stop running, you will only die tired!")
        super().Print()


class Dwarves(Faction):
    def __init__(self, name, numOfUnits, attackPoint, healthPoint, regNumber):
        super().__init__(name, numOfUnits, attackPoint, healthPoint, regNumber)


    def PerformAttack(self):
        if(self.firstEnemy.isAlive and self.secondEnemy.isAlive):
            self.firstEnemy.ReceiveAttack(super().PerformAttack()/2,self)
            self.secondEnemy.ReceiveAttack(super().PerformAttack()/2,self)
        elif(self.firsEnemy.isAlive and not self.secondEnemy.isAlive):
            self.firstEnemy.ReceiveAttack(super().PerformAttack(),self)
        elif(not self.firstEnemy.isAlive and self.secondEnemy.isAlive):
            self.secondEnemy.ReceiveAttack(super().PerformAttack(),self)
        else:
            print('All enemies are dead! ')
    
    def ReceiveAttack(self,attack,attacker):
        try:
            super().ReceiveAttack((attack)/(self.healthPoint))
        except:
            print('Something has gone wrong')


    def PurchaseWeapons(self,weapon):
        super().PurchaseWeapons(weapon)
        return 10*weapon
    
    def PurchaseArmors(self,armor):
        super().PurchaseArmors(2*armor)
        return 3*armor


    def Print(self):
        print("Taste the power of our axes!")
        super().Print()



class Elves(Faction):

    def __init__(self, name, numOfUnits, attackPoint, healthPoint, regNumber):
        super().__init__(name, numOfUnits, attackPoint, healthPoint, regNumber)
    
    def PerformAttack(self):
        if(self.firstEnemy.isAlive and self.secondEnemy.isAlive):
            self.firstEnemy.ReceiveAttack((super().PerformAttack())*0.6,self)#(1.5)*(0.4)
            self.secondEnemy.ReceiveAttack((super().PerformAttack())*0.6,self)

            #if(self.firstEnemy.__class__.__name__ == "Dwarves"):
            #    self.firstEnemy.ReceiveAttack((super().PerformAttack())*0.6)#(1.5)*(0.4)
            #    self.secondEnemy.ReceiveAttack((super().PerformAttack())*0.6)
            #else:
            #    self.firstEnemy.ReceiveAttack((super().PerformAttack())*0.6)#(1.5)*(0.4)
            #    self.secondEnemy.ReceiveAttack((super().PerformAttack())*0.6)
        elif(self.firsEnemy.isAlive and not self.secondEnemy.isAlive):
            if(self.firstEnemy.__class__.__name__ == "Dwarves"):
                self.firstEnemy.ReceiveAttack((super().PerformAttack())*1.5,self)
            else:
                self.firstEnemy.ReceiveAttack(super().PerformAttack(),self)
        elif(not self.firstEnemy.isAlive and self.secondEnemy.isAlive):
            if(self.secondEnemy.__class__.__name__ == "Dwarves"):
                self.secondEnemy.ReceiveAttack((super().PerformAttack())*1.5,self)
            else:
                self.secondEnemy.ReceiveAttack(super().PerformAttack(),self)
        else:
            print('All enemies are dead! ')
    
    def ReceiveAttack(self,attack,attacker):
        if(attacker.__class__.__name__ == "Orcs"):
            super().ReceiveAttack((attack*(1.25))/(self.healthPoint))
        else:
            super().ReceiveAttack((attack*(0.75))/(self.healthPoint))


    def PurchaseWeapons(self,weapon):
        super().PurchaseWeapons(2*weapon)
        return 15*weapon
    
    def PurchaseArmors(self,armor):
        super().PurchaseArmors(4*armor)
        return 5*armor


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
        self.weaponPoint = startWeaponPoint
        self.armorPoint = startArmorPoint

    def AssignFactions(self,fact1,fact2,fact3):
        self.firstFaction = fact1
        self.secondFaction = fact2
        self.thirdFaction = fact3
    
    def SellWeapons(self,wp,fact):
        if(fact.isAlive):
            if(int(wp) > self.weaponPoint):
                print('You try to sell more weapons than you have in possession.')
            else:
                self.revenue += fact.PurchaseWeapons(int(wp))
                print('Weapons sold!')
        else:
            print('The faction you want to sell weapons is dead!')


    def SellArmors(self,ap,fact):
        if(fact.isAlive):
            if(int(ap) > self.armorPoint):
                print('You try to sell more armors than you have in possession.')
                return False
            else:
                self.revenue += fact.PurchaseArmors(int(ap))
                print('Armors sold!')
                return True
        else:
            print('The faction you want to sell armors is destroyed!')
            return False


    def EndTurn(self):
        self.weaponPoint = self.startWeaponPoint
        self.armorPoint = self.startArmorPoint




orcs = Orcs('orcs',40,20,10,5)
dwarves = Dwarves('dwarves',60,10,20,10)
elves = Elves('elves',30,20,20,5)
merchant = Merchant(20,20)

orcs.AssignEnemies(dwarves,elves)
dwarves.AssignEnemies(orcs,elves)
elves.AssignEnemies(orcs,dwarves)


def StartOver():
    orcs = Orcs('orcs',40,20,10,5)
    dwarves = Dwarves('dwarves',60,10,20,10)
    elves = Elves('elves',30,20,20,5)
    merchant = Merchant(20,20)
    
    orcs.AssignEnemies(dwarves,elves)
    dwarves.AssignEnemies(orcs,elves)
    elves.AssignEnemies(orcs,dwarves)



def StartGame():
    orcs.Print()
    dwarves.Print()
    elves.Print()

    orcs.PerformAttack()
    elves.PerformAttack()
    dwarves.PerformAttack()

    print('\nAfter the first attack phase, faction information are as follows: \n')
    orcs.Print()
    dwarves.Print()
    elves.Print()


    while(merchant.armorPoint>0 and merchant.weaponPoint>0):
        str2 = """Merchant selling phase! Select a faction to sell a weapon to! 
        1)Orcs
        2)Dwarves
        3)Elves
        """

        str3 = """Merchant selling phase! Select a faction to sell a armor to! 
        1)Orcs
        2)Dwarves
        3)Elves
        """

        val2 = input(str2)
        val3 = input(str3)

        if(val2 == '1'):
            wpn = input('Input how many weapons you want to sell! \n')
            merchant.SellWeapons(wpn,orcs)
        

        elif(val2 == '2'):
            wpn = input('Input how many weapons you want to sell! \n')
            merchant.SellWeapons(wpn,dwarves)
        elif(val2 == '3'):
            wpn = input('Input how many weapons you want to sell! \n')
            merchant.SellWeapons(wpn,elves)
        else:
            print('Input is not recognized! \n')


        if(val3 == '1'):
            arm = input('Input how many armors you want to sell! \n')
            merchant.SellArmors(wpn,orcs)
        elif(val3 == '2'):
            arm = input('Input how many armors you want to sell! \n')
            merchant.SellArmors(arm,dwarves)
        elif(val3 == '3'):
            arm = input('Input how many armors you want to sell! \n')
            merchant.SellArmors(arm,elves)
        else:
            print('Input is not recognized! \n')


        inp = input('Press 1 if you want to end the selling phase! \n')
        if(inp == '1'):
            break

    str4 = """
    1)End day
    2)End currently played game and start a new one
    3)Quit game
    """

    end = input(str4)

    if(end == '1'):
        orcs.EndTurn()
        dwarves.EndTurn()
        elves.EndTurn()
        merchant.EndTurn()
        StartGame()
    elif(end == '2'):
        
        StartOver()
        StartGame()
        
    elif(end == '3'):
        return 0
    else:
        print('Input is not recognized! \n')






StartGame()
