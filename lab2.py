
room_temp = 24.5
min_temp = float(input("Minimum temperature of your room: "))
Max_temp = float(input("Maximum temperature of your room: "))


def display_main_menu():
    print("Hello I will help you calculate the temperature around you:)")

def get_user_Input(min_temp,Max_temp):
    temp = list([min_temp,Max_temp])
    return temp

def cal_average(min_temp,Max_temp,room_temp):
    temp_avg=(min_temp+Max_temp+room_temp)/3
    return temp_avg
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_Input(min_temp,Max_temp)
    temp_avg = cal_average(min_temp,Max_temp,room_temp)
    print(num_list)
    print(temp_avg)

main()
