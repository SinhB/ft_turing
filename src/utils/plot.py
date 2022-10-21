import math
import matplotlib.pyplot as plt

def plot_complexity(machine_result):
    linear_n = [0]
    O_logn = [0]
    O_n_logn = [0]
    O_n2 = [0]
    O_2n = [0]
    O_factorialn = [0]
    O_n_sqrtn = [0]
    O_sqrtn = [0]
    O_n_logn2 = [0]
    for n in range(1, 100):
        linear_n.append(n)
        O_logn.append(math.log(n))
        O_n_logn.append(n * math.log(n))
        O_n2.append(n ** 2)
        O_2n.append(2 ** n)
        O_factorialn.append(math.factorial(n))
        O_n_sqrtn.append(n * math.sqrt(n))
        O_sqrtn.append(math.sqrt(n))
        O_n_logn2.append(n * (math.log(n) ** 2))

    fig, axs = plt.subplots(2, 2)
    legend = [
        'O(logn)',
        'O(n)',
        'O(nlogn)',
        'O(n**2)',
        'O(2**n)',
        'O(n!)',
        'O(n_sqrtn)',
        'O(sqrtn)',
        'O(n_logn2)',
    ]
    for i in range(0, 2):
        for j in range(0, 2):
            axs[i, j].plot(O_logn, color='red')
            axs[i, j].plot(linear_n, color='green')
            axs[i, j].plot(O_n_logn, color="purple")
            axs[i, j].plot(O_n2, color='cyan')
            axs[i, j].plot(O_2n, color='orange')
            axs[i, j].plot(O_factorialn, color='lightblue')
            axs[i, j].plot(O_n_sqrtn, color='yellow')
            axs[i, j].plot(O_sqrtn, color='magenta')
            axs[i, j].plot(O_n_logn2, color='red')
            # axs[i, j].legend()
            axs[i, j].set_xlim([0, 10])
            axs[i, j].set_ylim([0, 100])
            axs[i, j].grid()

    legend1 = legend+ ['O(0n1n)']
    legend2 = legend+ ['O(02n)']
    legend3 = legend+ ['O(palindrome)']
    legend4 = legend+ ['O(unary_add)']

    axs[0, 0].plot(machine_result['0n1n'], color='black')
    axs[0, 0].legend(legend1)

    axs[0, 1].plot(machine_result['02n'], color='black')
    axs[0, 1].legend(legend2)

    axs[1, 0].plot(machine_result['palindrome'], color='black')
    axs[1, 0].legend(legend3)

    axs[1, 1].plot(machine_result['unary_add'], color='black')
    axs[1, 1].legend(legend4)

    plt.show()



def plot_complexity2(machine_result):
    linear_n = [0]
    O_logn = [0]
    O_n_logn = [0]
    O_n2 = [0]
    O_2n = [0]
    O_factorialn = [0]
    O_n_sqrtn = [0]
    O_sqrtn = [0]
    O_n_logn2 = [0]
    for n in range(1, 100):
        linear_n.append(n)
        O_logn.append(math.log(n))
        O_n_logn.append(n * math.log(n))
        O_n2.append(n ** 2)
        O_2n.append(2 ** n)
        O_factorialn.append(math.factorial(n))
        O_n_sqrtn.append(n * math.sqrt(n))
        O_sqrtn.append(math.sqrt(n))
        O_n_logn2.append(n * (math.log(n) ** 2))
        # O_n_logn2.append(n * (math.log(n) ** 2))
        # O_test.append(3 * n * math.log(n))

    plt.plot(O_logn, color='red')
    plt.plot(linear_n, color='green')
    plt.plot(O_n_logn, color="purple")
    plt.plot(O_n2, color='cyan')
    plt.plot(O_2n, color='orange')
    plt.plot(O_factorialn, color='lightblue')
    plt.plot(O_n_sqrtn, color='yellow')
    plt.plot(O_sqrtn, color='magenta')
    plt.plot(O_n_logn2, color='red')

    plt.plot(machine_result, color='black')
    plt.legend([
        'O(logn)',
        'O(n)',
        'O(nlogn)',
        'O(n**2)',
        'O(2**n)',
        'O(n!)',
        'O(n_sqrtn)',
        'O(sqrtn)',
        'O(n_logn2)',
        'O(machine)',
    ])
    plt.xlim([0, 10])
    plt.ylim([0, 100])
    plt.grid()
    plt.show()