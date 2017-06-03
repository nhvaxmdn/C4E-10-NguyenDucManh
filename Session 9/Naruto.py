import pygame

class Chavacter:

    def __init__(self, name, health,damage,defend,place):
        self.name = name
        self.health = health
        self.damage = damage
        self.defend = defend
        self.place = place

    def print(self):
        print("{0}: - HP:, {1} - DAMAGE:, {2} - DENFEND:, {3} - PLACE:{4}".format( self.name,
                                                                              self.health,
                                                                              self.damage,
                                                                              self.defend,
                                                                              self.place))

    # def fight(self,chavacter):
    #
    #     damage = self.damage - chavacter.defend
    #
    #     if damage > 0:
    #         chavacter.health -= damage
    #     else:
    #         self.health += damage
    #
    #
    #     print("{0} vs {1}".format(self.name,chavacter.name))
    #     self.print()
    #     chavacter.print()
    #     print()


class Village:
    def __init__(self,name,chavacter_list):
        self.name = name
        self.members = []
        self.add_member(chavacter_list)

    def add_member (self,chavacters):

        for chavacter in chavacters:
            if chavacter.place == self.name:
                self.members.append(chavacter)

        print("Village {0} has got".format(self.name))
        for member in self.members:
            member.print()
        print()


    #
    # def print_members(self):
    #     print(self.name + "members : ", end='')
    #     for member in self.members:
    #         if member != self.members[len(self.members)- 1]:
    #             print(member.name,end =",")
    #         else:
    #             print(member.name)





Naruto = Chavacter("Naruto",8,5,1,"leaf")
Madara = Chavacter("Madara",10,6,4,"leaf")
Gaara = Chavacter("Gaara",10,4,7,"sand")
Obito = Chavacter("Obito",12,6,3,"leaf")
chavacter_list = [Naruto, Madara, Gaara, Obito]


leaf_village = Village("leaf", chavacter_list)
sand_village = Village("sand", chavacter_list)

# Naruto.fight(Madara)
# Gaara.fight(Obito)

# leaf = Village("leaf")
# leaf.add_member(Naruto)
# leaf.add_member(Madara)
# leaf.add_member(Obito)
#
# sand = Village("sand")
# sand.add_member(Gaara)
#
# leaf.print_members()
# sand.print_members()
