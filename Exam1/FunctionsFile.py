def Whichmann_Hill_Random_Number_Generator(seeds, how_many):

    # Define initial seeds
    s1 = seeds[0]
    s2 = seeds[1]
    s3 = seeds[2]

    random_values = []

    while True:
        if len(random_values) < how_many:

            # Update seed values
            s1 = ((171 * s1) % 30269)
            s2 = ((172 * s2) % 30307)
            s3 = ((170 * s3) % 30323)

            # Calculate random number
            r = s1 / 30269 + s2 / 30307 + s3 / 30323
            r = (r % 1.0)

            # Append results to values list
            random_values.append(r)

        else:
            break

    return random_values
