# death row
import random
import time


def solve_random(drawers, p):
    j = 1
    limit = len(drawers) / 2
    used = []
    while j <= limit:
        guess = random.choice(drawers)
        while guess in used:
            guess = random.choice(drawers)
        used.append(guess)
        if guess == p:
            return True, j
        j += 1
    return False, 0


def solve_loop(drawers, p):
    # choose first case of the same number as the prisoner
    index = p - 1
    limit = len(drawers) / 2
    j = 1
    next_guess = 0
    while j <= limit:
        if drawers[index] == p:
            # print("Returning True. Index = " + str(index) + ", p = " + str(p))
            return True
        index = drawers[index]
        index -= 1
        j += 1
    return False


nump = int(input("Number of prisoners: "))
runs = int(input("Number of times to run the program: "))
choice = input("1. Random algorithm\n2. Improved algorithm\n3. Both algorithms\nMake your choice: ")
# limit = nump/2

cases = []
for i in range(1, nump + 1):
    cases.append(i)
random.shuffle(cases)

run = 1
runs_won = 0

if choice == '1' or choice == '3':
    print("\nRunning random algorithm")
    start_time = time.time()
    while run <= runs:
        prisoner = 1
        failed = False
        while prisoner <= nump and failed == False:
            result, attempts = solve_random(cases, prisoner)
            if result == False:
                # This prisoner lost, no longer run loop
                failed = True
            if prisoner == nump and failed == False:
                runs_won += 1
            prisoner += 1
        run += 1
    rate = int(runs_won / runs * 100)
    print("Prisoners survived " + str(rate) + "% of the time (" + str(runs_won) + "/" + str(runs) + ")")
    print("Executed in " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))

if choice == '2' or choice == '3':
    print("\nRunning improved algorithm")
    run = 1
    runs_won = 0
    start_time = time.time()
    while run <= runs:
        prisoner = 1
        failed = False
        while prisoner <= nump:
            result = solve_loop(cases, prisoner)
            if result == False:
                # This prisoner lost, no longer run loop
                failed = True
            if prisoner == nump and failed == False:
                runs_won += 1
            prisoner += 1
        run += 1
    rate = int(runs_won / runs * 100)
    print("Prisoners survived " + str(rate) + "% of the time (" + str(runs_won) + "/" + str(runs) + ")")
    print("Executed in " + time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
