def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    rooms = range(1,9)
    speaker_rooms = []
    
    for i , name in enumerate(names):
        if i < len(rooms):
            room_number = rooms[i]
            speaker_rooms.append(f"Hello, {name}! You'll be assigned to room {room_number}!")
        else:
            break
    return speaker_rooms

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in rooms:
        print(assignment)
