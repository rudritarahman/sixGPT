import math
import sqlite3

# connect to the database

conn = sqlite3.connect('\project_CSE216\sensor_data.db')

# create a cursor object
cursor = conn.cursor()

# execute the query
cursor.execute('SELECT * FROM sensor_data')

# fetch all rows and store them in a list
rows = cursor.fetchall()

# close the connection
conn.close()

# print the rows
# print(rows[0])


# lifespan for row[0]:
# Import required libraries

# Define the function to calculate lifespan of fruit


def calculate_fruit_lifespan(methane_emission, temperature, humidity):

    # Define the lifespan constant for the specific fruit being analyzed
    lifespan_constant = 10.0  # This needs to be analysed from ML code for specific fruit

    # Calculate the lifespan of the fruit based on the provided inputs
    lifespan = (lifespan_constant / methane_emission) * \
        (math.exp(0.05 * (temperature - 20.0))) * (humidity / 100.0)

    # Return the calculated lifespan in days
    return lifespan


# Example usage of the function to calculate the lifespan of a hypothetical fruit
lifespan = calculate_fruit_lifespan(
    # from database
     methane_emission=rows[0][3], temperature=rows[0][1], humidity=rows[0][2]


    # approx calc
    # methane_emission=1.7, temperature=25, humidity=80
)
print(f"The estimated lifespan of the fruit is {lifespan:.2f} days.")
