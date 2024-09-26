def puzzle(heads, legs):

    rabbits = int((legs-70)/2)
    chickens = int(heads - rabbits)

    return rabbits, chickens

heads = int(input())
legs=int(input())

print(puzzle(heads, legs))