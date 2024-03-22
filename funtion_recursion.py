def sum_of_digits(n):
    if n < 10:  #Base case:If n is a single _digite nunber, return n
        return n

    else:   # Recursive cade: Calcukate the sun =m of digite
        last_digit = n % 10  # get the sum of digits
        remaining_digits = n//10 # Get the remaining digits by integer d:

        return last_digit + sum_of_digits (remaining_digits) # resursively  



print(sum_of_digits(123))
