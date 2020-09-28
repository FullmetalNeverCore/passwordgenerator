import random
import string

try:
    pass_word = ''.join(random.choice(string.ascii_letters + string.digits) for n in range(16))

    print(pass_word)

except Exception as e:
    print(e)
    print("Solve the problem and then restart the script")

finally:
    print("Created by NeverCore@2020")
    print("714h")