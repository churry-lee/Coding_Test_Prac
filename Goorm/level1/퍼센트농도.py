import sys
input_ = sys.stdin.readline

def calculate_concentration(current_mass, current_concentration, added_water):
    # Convert the current mass and concentration into the mass of NaOH
    original_solute_mass = current_mass * current_concentration / 100
    
    # Calculate the new total mass
    new_total_mass = current_mass + added_water
    
    # Calculate the new concentration
    new_concentration = (original_solute_mass / new_total_mass) * 100
    
    return new_concentration

# The main loop
while True:
    # added_water = float(input("추가할 물의 양 Tg을 입력하십시오 (종료하려면 음수를 입력하십시오): "))
    added_water = float(input_().strip())
    
    # The sentinel value to end the program
    if added_water < 0:
        break
    
    # Calculate the new concentration
    new_concentration = calculate_concentration(500, 3, added_water)
    
    # print(f"만들어질 새로운 용액의 농도는 {new_concentration} %입니다.")
    print(new_concentration)
