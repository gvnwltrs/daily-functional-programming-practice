# Daily Functional Programming Practice

## Goal: Simple implementations in 15-30 minutes or less for daily practice of functional programming and TDD principles. 

## Month 1: Python - September 2024

### Day 1: Monday, September 9, 2024 - Pure Functions
Just added a few test and simple pure functions to practice functional programming + TDD in Python for today. Pure functions should not have any side effects, such that they do not depend on any outside global, state, or dependency to perform an operation. 

### Day 2: Tuesday, September 10, 2024 - Higher-Order Functions
Starting with high-order functions today. Basically passing a function to another function or return a function from a function. 

### Day 3: Wednesday, September 11, 2024 - Recursion
Practicing some recursion today over using regular loops or conditionals. 

### Day 4: Thursday, September 12, 2024 - Function Composition & Currying
Function Composition and currying are primarily associated with higher-order functions. Function composition combines two or more functions into one function, and currying is the process of taking a current function that takes many arguments and breaking it out to multiple functions that take only a single argument. 

### Day 5: Friday, September 13, 2024 - Immutability & Data Transformations
Today I am going to focus on transforming data structures without mutating the original data. This relates back to the "pure functions" aspect of functional programming. Pure functions, for the same input given, should always return the same output. Immutability means, that once the data is created, it cannot change. Immutability reinforces the concept of a pure function, where functions can not modify the actual data structures directly -- instead they make a copy of the data structure and returns any modifications it makes of the copy, not the original or "real" data structure. 

### Day 6: Saturday, September 14, 2024 - Side Effects & IO Handling
Again relates to keeping functions "pure". A pure function cannot produce side effects. A function is not pure when it modifies some state external to the function. A function that prints to console is a side effect because it alters "external state". The goal here is to minimize the use of impure functions that produce side effects by isolating the side effect (single) in another function. The other function that isolates the side effect could use another pure function to support it. Can use the function to return a value from a pure function in the return while the impure function is also used.  

### Day 7: Rest

### Day 8: Monday, September 16, 2024 - Pure Functions
More practice with pure functions. Getting used to forming functions without side effects. A pure function should always take at least one input, not modify or interact with anything external to it, and return something.  

### Day 9: Tuesday, September 17, 2024 - Higher-Order Functions
