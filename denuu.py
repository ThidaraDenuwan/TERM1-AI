#project euler
#problem 1
def multiples_of_3_and_5(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
print(multiples_of_3_and_5(1000))

#problem 2
def even_fibonacci_numbers(n):
    a, b = 0, 1
    total = 0
    while b < n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total
print(even_fibonacci_numbers(4000000))

#problem 3
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
print(largest_prime_factor(600851475143))

#problem 4
def largest_palindrome_product():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if str(product) == str(product)[::-1] and product > max_palindrome:
                max_palindrome = product
    return max_palindrome
print(largest_palindrome_product())

#problem 5
def smallest_multiple(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    multiple = 1
    for i in range(2, n + 1):
        multiple = lcm(multiple, i)
    return multiple
print(smallest_multiple(20))

#problem 6
def sum_square_difference(n):
    sum_of_squares = sum(i * i for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return square_of_sum - sum_of_squares
print(sum_square_difference(100))

#problem 7
def nth_prime(n):
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                break
        else:
            count += 1
    return candidate
print(nth_prime(10001))

#problem 8
def largest_product_in_a_series(series, n):
    max_product = 0
    for i in range(len(series) - n + 1):
        product = 1
        for j in range(n):
            product *= int(series[i + j])
        if product > max_product:
            max_product = product
    return max_product
series = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)
print(largest_product_in_a_series(series, 13))

#problem 9
def special_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a, n - a):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c
print(special_pythagorean_triplet(1000))

#problem 10
def sum_of_primes(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)
print(sum_of_primes(2000000))




