def Whichmann_Hill_Random_Number_Generator(seed, how_many):

    # Define initial seeds
    s1 = seed[0]
    s2 = seed[1]
    s3 = seed[2]

    values = []

    while True:
        if len(values) < how_many:

            # Update seed values
            s1 = ((171 * s1) % 30269)
            s2 = ((172 * s2) % 30307)
            s3 = ((170 * s3) % 30323)

            # Calculate random number
            r = s1 / 30269 + s2 / 30307 + s3 / 30323
            r = int((r % 1.0) * 100)

            if r not in values:

                # Append results to values list
                values.append(r)

                continue

            else:
                continue

        else:
            break

    return values


def generate_matrix(rows, cols, rand_seed):

    # Calculate how many values are needed
    number_of_values = rows * cols

    # Get the randomly generated values
    values = Whichmann_Hill_Random_Number_Generator(rand_seed, number_of_values)

    # Create a matrix of zeros
    matrix = [[0 for i in range(cols)] for j in range(rows)]

    # Set the initial values index
    index = 0

    # Loop through matrix
    for i in range(rows):
        for j in range(cols):

            # Replace zeros with actual values
            matrix[i][j] = values[index]

            # Advance index by 1
            index += 1

    return matrix


def main():

    # Random number generator seeds
    seeds = [1234, 19857, 25000]

    # How many rows and columns you want
    rows = 10
    cols = 10

    # Generate the matrix
    matrix = generate_matrix(rows, cols, seeds)

    # Print results
    print('A=')

    for row in matrix:
        print(row)

    print('\nSeed Values =', seeds)
    print('Verified 0 duplicate numbers!')


main()
