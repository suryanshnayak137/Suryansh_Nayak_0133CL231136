class UnderAgeError(Exception):
    pass
class InvalidAgeError(Exception):
    pass
class AgeVerification:
    def set_age(self, age):
        try:
            if age < 0:
                raise ValueError("Age cannot be negative.")
            elif age < 18:
                raise UnderAgeError(f"Age {age} is under 18. Access denied.")
            elif age > 100:
                raise InvalidAgeError(f"Age {age} is invalid. Too high.")
            else:
                print(f"Valid age! Welcome.")

        except ValueError as e:
            print(f"ValueError: {e}")
        except UnderAgeError as e:
            print(f"UnderAgeError: {e}")
        except InvalidAgeError as e:
            print(f"InvalidAgeError: {e}")
        finally:
            print(f"Age verification attempted for age: {age}\n")



obj = AgeVerification()

print(" Test 1: Negative age")
obj.set_age(-5)

print(" Test 2: Under 18")
obj.set_age(15)

print(" Test 3: Over 100")
obj.set_age(150)

print(" Test 4: Valid age")
obj.set_age(25)