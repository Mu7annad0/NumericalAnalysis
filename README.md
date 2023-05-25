# NumericalAnalysis
This GitHub repository contains my third-year university project on numerical analysis implemented using Python and Tkinter. The project focuses on developing a user-friendly interface to solve mathematical problems numerically. I have implemented a specific numerical method and metrics:

## 1- Bisection,
The bisection method is a numerical method that iteratively divides an interval in half to find the root of a function. It works by checking the sign change of the function within the interval and narrowing down the range until the desired accuracy is achieved.

## 2- False Position,
The False Position method is a numerical method used to find the root of an equation by linearly interpolating between two points. It narrows down the interval where the root lies by considering the function's values at the interval endpoints and updating the interval based on the sign of the function at the interpolated point.

## 3- Simple Fixed Point,
The Simple Fixed Point method is a numerical method that iteratively applies a given function to an initial guess until convergence is achieved, aiming to find the fixed point of the function where f(x) = x. It requires the function to meet specific convergence conditions for accurate results.

## 4- Newton,
The Newton method, is a numerical algorithm that iteratively refines an initial guess to approximate the root of a function by using its derivative. It converges rapidly but requires an initial guess close to the actual root and relies on the function's differentiability.

## 5- Secant,
The Secant Method, is a numerical technique for finding the root of a function by approximating the derivative using finite differences. It uses two initial guesses and iteratively updates them based on the secant line to converge towards the root.

## 6- Gaussian Elimantion
Gaussian elimination is a matrix operation used to solve systems of linear equations by systematically eliminating variables. It involves transforming the augmented matrix into row-echelon form through row operations like scaling, swapping, and adding multiples of rows, ultimately yielding the solution to the system.

## 7- LU decomposition
LU decomposition, also known as LU factorization, is a matrix factorization method that decomposes a square matrix into the product of a lower triangular matrix (L) and an upper triangular matrix (U). It is often used to efficiently solve systems of linear equations and perform matrix operations.

The Tkinter library is utilized to create an interactive GUI, enabling users to input the necessary parameters and receive the computed results. Additionally, I have incorporated error handling and validation to ensure accurate input. The repository contains the source code, documentation explaining the numerical method, the GUI design, and examples of its application. Through this project, I aimed to demonstrate my understanding of numerical analysis concepts and showcase my programming skills in Python and GUI development with Tkinter.
