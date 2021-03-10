# by Ryan McAlpine and Nicholas Keng

import matplotlib.pyplot as plt

operationCounter = 0

def fib( k ):
    if k < 0:
        print( "Invalid input\n" )
        return k
    if k < 2:
        return k
    global operationCounter
    operationCounter += 1
    return ( fib(k-1) + fib(k-2) )

def euclid( m, n ):
    if n == 0:
        return m
    global operationCounter
    operationCounter += 1
    r = m % n
    return euclid( n, r )

def exp_DB1( a, n ):
    if n < 0:
        print( "Invalid input\n" )
        return
    if n == 0:
        return 1
    global operationCounter
    operationCounter += 1
    return ( a * exp_DB1( a, n-1 ) )

def exp_DBCF( a, n ):
    if n < 0:
        print( "Invalid input\n" )
        return
    if n == 0:
        return 1
    global operationCounter
    if (n % 2) == 0:
        operationCounter += 1
        return exp_DBCF( a, n/2 ) ** 2
    operationCounter += 2
    return a * ( exp_DBCF( a, (n-1)/2 ) ** 2 )

def exp_DAC( a, n ):
    if n < 0:
        print( "Invalid input\n" )
        return
    if n == 0:
        return 1
    global operationCounter
    if (n % 2) == 0:
        operationCounter += 1
        return exp_DAC( a, n/2 ) * exp_DAC( a, n/2 )
    operationCounter += 2
    return a * ( exp_DAC( a, (n-1)/2 ) * exp_DAC( a, (n-1)/2 ) )

def selection_sort( L ):
    for i in range( len(L) ):
        min_idx = i
        for j in range( i+1, len(L) ):
            global operationCounter
            operationCounter += 1
            if int(L[min_idx]) > int(L[j]):
                min_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]
    return L

def insertion_sort( L ):
    for i in range( 1, len(L) ):
        k = L[i]
        j = i-1
        global operationCounter
        #operationCounter += 1
        while j >= 0 and int(k) < int(L[j]):
            operationCounter += 1
            L[j+1] = L[j]
            j -= 1
        L[j+1] = k
    return L

def scatterPlotMode():
    fig = plt.figure()

    print("Plotting fib()... ")

    # Place the values into a list
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    fibValues = []  # Store fib values for euclid
    numOperations = []  # Create a new empty list to hold the values of A(k)
    # Run the fib() function on each test value and record A(k)'s
    global operationCounter
    for value in values:
        operationCounter = 0
        fibValues.append( fib( int(value) ) )
        numOperations.append( operationCounter )
    # Plot the A(k) values
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.scatter( values, numOperations )
    ax1.set_xlabel('Input - k')
    ax1.set_ylabel('Number of Additions - A(k)')
    ax1.set_title("Fibonacci")
    ax1.ticklabel_format(style='plain')

    print("Euclid... ")

    # Reset our list to hold new function's D(n)
    numOperations = []
    # Use an iterator so we can grab 2 nums at a time
    it = iter( fibValues )
    # Store n values for charting x-axis
    nValues = []
    for value in it:
        operationCounter = 0
        nValues.append( int(value) )
        euclid( int( next(it) ), int(value) )
        numOperations.append( operationCounter )
    # Plot the D(n) values
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.scatter( nValues, numOperations )
    ax2.set_title("Euclid")

    print("Exp: Decrease-by-One... ")

    numOperations = []
    values = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
    for value in values:
        operationCounter = 0
        exp_DB1( 2, value )
        numOperations.append( operationCounter )
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.scatter( values, numOperations, label='Decrease by One' )
    ax3.set_xlabel('Input - n')
    ax3.set_ylabel('Number of Multiplications - M(n)')
    ax3.set_title("Exponentiation")

    print("Exp: Decrease-by-Constant-Factor... ")

    numOperations = []
    values = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
    for value in values:
        operationCounter = 0
        exp_DBCF(2, value)
        numOperations.append(operationCounter)
    ax3.scatter(values, numOperations, label='Decrease by Constant Factor')


    print("Exp: Divide-and-Conquer... ")

    numOperations = []
    values = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
    for value in values:
        operationCounter = 0
        exp_DAC(2, value)
        numOperations.append(operationCounter)
    ax3.scatter(values, numOperations, label='Divide and Conquer')

    print("Sorting... ")
    ##################################################
    #                Selection Sort                  #
    ##################################################

    ### SORTED INPUT ###

    # Open the file with the test values
    file_values = open("testSet\data100_sorted.txt", "r")
    values = file_values.readlines()
    list_lengths = [100]
    numOperations = []
    operationCounter = 0
    selection_sort(values)
    numOperations.append(operationCounter)
    i = 1000
    while i <= 10000:
        list_lengths.append(i)
        file_values = open("testSet\data%s_sorted.txt" % i, "r")
        values = file_values.readlines()
        operationCounter = 0
        selection_sort(values)
        numOperations.append(operationCounter)
        i += 1000
    ax4 = fig.add_subplot(2, 3, 4)
    ax4.scatter(list_lengths, numOperations, label='Selection')
    ax4.set_xlabel('Length of Input List - n')
    ax4.set_ylabel('Number of Comparisons - C(n)')
    ax4.set_title("Sorting - BEST CASE")
    ax4.ticklabel_format(style='plain')

    ### RANDOM INPUT ###

    file_values = open( "testSet\data100.txt", "r" )
    values = file_values.readlines()
    list_lengths = [100]
    numOperations = []
    operationCounter = 0
    selection_sort(values)
    numOperations.append(operationCounter)
    i = 1000
    while i <= 10000:
        list_lengths.append(i)
        file_values = open( "testSet\data%s.txt" % i, "r" )
        values = file_values.readlines()
        operationCounter = 0
        selection_sort(values)
        numOperations.append(operationCounter)
        i += 1000
    ax5 = fig.add_subplot(2, 3, 5)
    ax5.scatter( list_lengths, numOperations, label='Selection' )
    ax5.set_xlabel('Length of Input List - n')
    ax5.set_ylabel('Number of Comparisons - C(n)')
    ax5.set_title("Sorting - AVG CASE")
    ax5.ticklabel_format(style='plain')

    ### REVERSE-SORTED INPUT ###

    file_values = open("testSet\data100_rSorted.txt", "r")
    values = file_values.readlines()
    list_lengths = [100]
    numOperations = []
    operationCounter = 0
    selection_sort(values)
    numOperations.append(operationCounter)
    i = 1000
    while i <= 10000:
        list_lengths.append(i)
        file_values = open("testSet\data%s_rSorted.txt" % i, "r")
        values = file_values.readlines()
        operationCounter = 0
        selection_sort(values)
        numOperations.append(operationCounter)
        i += 1000
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.scatter(list_lengths, numOperations, label='Selection')
    ax6.set_xlabel('Length of Input List - n')
    ax6.set_ylabel('Number of Comparisons - C(n)')
    ax6.set_title("Sorting - WORST CASE")
    ax6.ticklabel_format(style='plain')

    ##################################################
    #                Insertion Sort                  #
    ##################################################

    ### SORTED INPUT ###

    file_values = open("testSet\data100_sorted.txt", "r")
    values = file_values.readlines()
    list_lengths = [100]
    numOperations = []
    operationCounter = 0
    insertion_sort(values)
    numOperations.append(operationCounter)
    i = 1000
    while i <= 10000:
        list_lengths.append(i)
        file_values = open("testSet\data%s_sorted.txt" % i, "r")
        values = file_values.readlines()
        operationCounter = 0
        insertion_sort(values)
        numOperations.append(operationCounter)
        i += 1000
    ax4.scatter(list_lengths, numOperations, label='Insertion')

    ### RANDOM INPUT ###

    file_values = open("testSet\data100.txt", "r")
    values = file_values.readlines()
    list_lengths = [100]
    numOperations = []
    operationCounter = 0
    insertion_sort(values)
    numOperations.append(operationCounter)
    i = 1000
    while i <= 10000:
        list_lengths.append(i)
        file_values = open("testSet\data%s.txt" % i, "r")
        values = file_values.readlines()
        operationCounter = 0
        insertion_sort(values)
        numOperations.append(operationCounter)
        i += 1000
    ax5.scatter(list_lengths, numOperations, label='Insertion')

    ### REVERSE-SORTED INPUT ###

    file_values = open("testSet\data100_rSorted.txt", "r")
    values = file_values.readlines()
    list_lengths = [100]
    numOperations = []
    operationCounter = 0
    insertion_sort(values)
    numOperations.append(operationCounter)
    i = 1000
    while i <= 10000:
        list_lengths.append(i)
        file_values = open("testSet\data%s_rSorted.txt" % i, "r")
        values = file_values.readlines()
        operationCounter = 0
        insertion_sort(values)
        numOperations.append(operationCounter)
        i += 1000
    ax6.scatter(list_lengths, numOperations, label='Insertion')

    plt.legend(loc='upper left')
    ax3.legend(prop={'size': 10})
    ax4.legend(prop={'size': 10})
    ax5.legend(prop={'size': 10})
    ax6.legend(prop={'size': 10})
    plt.show()

def userTestingMode():
    global operationCounter

    ### TASK ONE ###

    k = int( input( "Enter a value 'k' for which to compute Fib(k) and Euclid( fib(k+1), fib(k) ): ") )
    m = fib( k + 1 )
    operationCounter = 0
    n = fib(k)
    print( "kth element of Fibonnaci sequence: " + str(n) + ", found in " + str(operationCounter) + " operations." )
    operationCounter = 0
    print( "GCD using Euclid's algorithm: " + str(euclid(m, n)) + ", found in " + str(operationCounter) + " operations\n" )

   ### TASK TWO ###

    a = int( input( "Enter a value 'a' for which to compute exponentiation of a^n: ") )
    n = int( input( "Enter a value 'n' for which to compute exponentiation of a^n: ") )
    operationCounter = 0
    print( "using Decrease-by-One: " + str(exp_DB1(a, n)) + ", found in " + str(operationCounter) + " operations\n" )
    operationCounter = 0
    print( "using Decreasing-by-Constant-Factor: " + str(exp_DBCF(a, n)) + ", found in " + str(operationCounter) + " operations\n" )
    operationCounter = 0
    print( "using Divide-and-Conquer: " + str(exp_DAC(a, n)) + ", found in " + str(operationCounter) + " operations\n" )

    ### TASK THREE ###
    ## Selection Sort ##

    n = int( input( "Enter a value 'n' for the size of a list for Selection Sort (Between 10-100 in increments of 10): ") )
    if n % 10 != 0 or n < 10 or n > 100:
        print( "Invalid input\n" )
    else:
        file_values = open("smallSet\data%s.txt" % n, "r")
        values = file_values.readlines()
        operationCounter = 0
        values_sorted = selection_sort(values)
        print( "Sorted array:\n" )
        for v in range(len(values_sorted)):
            print( str(values_sorted[v]) )
        print( "Sorted in " + str(operationCounter) + " operations.\n")

    ## Insertion Sort ##

    n = int(input("Enter a value 'n' for the size of a list for Insertion Sort (Between 10-100 in increments of 10): "))
    if n % 10 != 0 or n < 10 or n > 100:
        print("Invalid input\n")
    else:
        file_values = open("smallSet\data%s.txt" % n, "r")
        values = file_values.readlines()
        operationCounter = 0
        values_sorted = insertion_sort(values)
        print("Sorted array:\n")
        for v in range(len(values_sorted)):
            print( str(values_sorted[v]) )
        print("Sorted in " + str(operationCounter) + " operations.\n")

def main():
    inp = input("> Enter 'S' to plot default values in scatter plot mode, or enter 'U' to input your own values in user testing mode: ")
    if inp == 'S':
        print( 'Calculating...')
        scatterPlotMode()
    elif inp == 'U':
        userTestingMode()
    else:
        print("Invalid input. 'P' will enter scatterplot mode and 'E' will enter user testing mode.\n")

if __name__ == "__main__":
    while True:
        main()