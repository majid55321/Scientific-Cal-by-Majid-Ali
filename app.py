import streamlit as st
import math
import sympy as sp

# Define available operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return math.pow(x, y)

def factorial(x):
    if x < 0:
        return "Error: Factorial of negative number"
    return math.factorial(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base=10):
    if x <= 0:
        return "Error: Logarithm of non-positive number"
    return math.log(x, base)

def exp(x):
    return math.exp(x)

def sqrt(x):
    if x < 0:
        return "Error: Square root of negative number"
    return math.sqrt(x)

def simplify(expr):
    return sp.simplify(expr)

def solve(equation, variable):
    return sp.solve(equation, variable)


# Streamlit interface
st.title("Scientific Calculator Created By Majid Ali")

# Operation selection
operation = st.selectbox(
    "Select operation:",
    ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)", "Factorial", "Sin", "Cos", "Tan", "Logarithm", "Exponential", "Square Root", "Simplify Expression", "Solve Equation"]
)

if operation in ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)"]:
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")
    if operation == "Add":
        st.write(f"Result: {add(num1, num2)}")
    elif operation == "Subtract":
        st.write(f"Result: {subtract(num1, num2)}")
    elif operation == "Multiply":
        st.write(f"Result: {multiply(num1, num2)}")
    elif operation == "Divide":
        st.write(f"Result: {divide(num1, num2)}")
    elif operation == "Power (x^y)":
        st.write(f"Result: {power(num1, num2)}")

elif operation == "Factorial":
    num = st.number_input("Enter a number", step=1, format="%d")
    st.write(f"Result: {factorial(num)}")

elif operation == "Sin":
    angle = st.number_input("Enter an angle in degrees", format="%f")
    st.write(f"Result: {sin(angle)}")

elif operation == "Cos":
    angle = st.number_input("Enter an angle in degrees", format="%f")
    st.write(f"Result: {cos(angle)}")

elif operation == "Tan":
    angle = st.number_input("Enter an angle in degrees", format="%f")
    st.write(f"Result: {tan(angle)}")

elif operation == "Logarithm":
    num = st.number_input("Enter a number", format="%f")
    base = st.number_input("Enter the base (default is 10)", value=10, format="%f")
    st.write(f"Result: {log(num, base)}")

elif operation == "Exponential":
    num = st.number_input("Enter a number", format="%f")
    st.write(f"Result: {exp(num)}")

elif operation == "Square Root":
    num = st.number_input("Enter a number", format="%f")
    st.write(f"Result: {sqrt(num)}")

elif operation == "Simplify Expression":
    expr = st.text_input("Enter an expression to simplify")
    if expr:
        result = simplify(expr)
        st.write(f"Simplified Expression: {result}")

elif operation == "Solve Equation":
    equation = st.text_input("Enter an equation (e.g., x^2 - 4 = 0)")
    variable = st.text_input("Enter the variable to solve for (e.g., x)")
    if equation and variable:
        result = solve(sp.sympify(equation), sp.Symbol(variable))
        st.write(f"Solution: {result}")

