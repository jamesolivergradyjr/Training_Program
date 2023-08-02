#import random module
import random
#create list, soon to become dictionary entries as repositories for movements
legs = ["back_Squats", "hack_Squats", "leg_Press", "leg_Extensions", "conventional_Dead-lifts", "sumo_deadlifts", "lunges", "weighted_Lunges"]
chest = ["bb_Bench_Press", "db_Bench_Press", "incline_Bench", "decline_bench", "dips", "chest_flye", "hammerStrength_Incline_bench", "hammerStrength_Bench", "hammerStrength_Decline_Bench"]
back = ["pull_ups", "lat_pulls", "seated_Cable_Row", "single-arm_DB_row", "inverted_row", "db_pullover", "hammer_strength_lateral_rows", "bentover_BB_row", "back_Extensions", "power_Cleans", "reverse_Fly", "face_Pulls", "shrugs"]
shoulders = ["upright_Rows", "db_seated_shoulder_press", "bb_Overhead_Press", "arnold_Press_DB_Shoulderpress", "face_Pulls", "lateral_Raises", "front_Plate_Raises", "clean_And_Press", "db_High_Pulls", "pike_Pushups"]
arms_biceps = ["db_Curls", "ez-Bar_Curls", "preacher_Curls", "db_Hammer_Curls", "plate_Curls", "preacher_Curls", "db_Iso_Curls", "underhand_Pullups", "spider_DBorBB_curls", "overhead_Cable_Curls", "wall_curls"]
arms_triceps = ["db_Seated_Overhead_Extensions", "triceps_Cable_Pushdowns", "dip_Machine", "diamond_Pushups", "overhead_cable_triceps_extension", "laying_Triceps_Extensions", "triceps_Kickbacks", "reverse_Grip_Benchpress"]
#adding some spaces for clarity and readibility of output
print("\n")
print("\n")

#each workout movement is presented by looping through the random sample of movements taken from the repository referenced above ^^^
#legs
leg_day = random.sample(legs, 5)
print(f"*Leg day will consist of: ")
for lm in leg_day:
    print(f"{lm}: 4 sets of 12")
print("\n")
# arms 
arm_day = (random.sample(arms_triceps, 5)) + (random.sample(arms_biceps, 5))
print(f"*Arm day will consist of: ")
for am in arm_day:
    print(f"{am}: 4 sets of 12")
print("\n")
#shoulders
shoulders_day = random.sample(shoulders, 5)
print(f"*Shoulder day will consist of: ")
for sm in shoulders_day:
    print(f"{sm}: 4 sets of 12")
print("\n")
#back
back_day = random.sample(back, 5)
print(f"*Back day will consist of: ")
for bm in back_day:
    print(f"{bm}: 4 sets of 12")
print("\n")
#chest
chest_day = random.sample(chest, 5)
print(f"*Chest day will consist of: ")
for cm in chest_day:
    print(f"{cm}: 4 sets of 12")
print("\n")