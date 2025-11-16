import random
def clean(id):
    room_status=random.choice(['clean','dirty'])
    if room_status=='clean':
        print("Room already cleaned")
    else:
        print("Cleaning the room")
        print("Room cleaned")

def main():
    a=input('Enter the room to cleane: ')
    a=int(a)
    clean(a)

if __name__=="__main__":
    main()