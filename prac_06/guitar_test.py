from prac_06.guitars import Guitar

guitar_1 = (Guitar("Gibson L-5 CES", 1922, 16035.40))
guitar_2 = (Guitar("Line 6 JTV-59", 2010, 1512.9))

print(f"Gibson L-5 CES get_age() - Expected 103 got {guitar_1.get_age()}")
print(f"Line 6 JTV-59 get_age() - Expected 15 got {guitar_2.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True got {guitar_1.is_vintage()}")
print(f"Line 6 JTV-59 is_vintage() - Expected False got {guitar_2.is_vintage()}")