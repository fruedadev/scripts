module Maths where

isDivisible :: Int -> Int -> Bool
isDivisible 0 _ = True
isDivisible _ 1 = True
isDivisible n m = n `mod` m == 0

isEven :: Int -> Bool
isEven n = isDivisible n 2

isOdd :: Int -> Bool
isOdd n = not (isEven n)

factors :: Int -> [Int]
factors n = [x | x <- [1..n-1], isDivisible n x]

sqrtFactors :: Int -> [Int]
sqrtFactors n = [x | x <- [2..(round (sqrt (fromIntegral n)))], isDivisible n x]

isPrime :: Int -> Bool
isPrime 1 = False
isPrime n = length (sqrtFactors n) == 0

primes :: [Int]
primes = 2 : [ x | x <- [2..], isOdd x, isPrime x]

primeFactors :: Int -> [Int]
primeFactors n = [x | x <- sqrtFactors n, isPrime x]

isPalindrome :: Int -> Bool
isPalindrome n = show n == reverse (show n)

fac :: Int -> Int
fac 1 = 1
fac n = n * fac (n-1)
