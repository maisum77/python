import random
# class Hat:
#     def __init__(self):
#         self.houses=["computerScience","ArtificalIntelligence","CyberSecurity","SoftwareEngineering"]
#     def sort(self,name):
#         house = random.choice(self.houses)
#         print(f"{name},is in the some {house}")

class Hat:
    houses=["computerScience","ArtificalIntelligence","CyberSecurity","SoftwareEngineering"]
    @classmethod
    def sort(cls,name):
        house = random.choice(cls.houses)
        print(f"{name},is in the some {house}")




Hat.sort("maisum")