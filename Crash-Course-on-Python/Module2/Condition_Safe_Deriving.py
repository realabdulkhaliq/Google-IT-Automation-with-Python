def safe_division(numerator, denominator):
    # Complete the if block to catch any "denominator" variables
    # that are equal to 0.
    if denominator == 0:
        result = denominator
    else:
        # Complete the division equation.
        result = numerator/denominator
    return result


print(safe_division(5, 5)) # Should print 1.0
print(safe_division(5, 4)) # Should print 1.25
print(safe_division(5, 0)) # Should print 0
print(safe_division(0, 5)) # Should print 0.0