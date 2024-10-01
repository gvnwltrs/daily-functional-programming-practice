# Daily Functional Programming Practice

## Goal: Simple implementations in 15-30 minutes or less for daily practice of functional programming and TDD principles. 

## Month 1: Python - September 1 - 30, 2024

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
Today I want to focus on extending functions. The goal is to practice situations where I may need to modify someone else's (or my own) code, but want to be minimally invasive about it by not directly modifying it (wrapper or decorator). 

### Day 10: Wednesday, September 18, 2024 - Recursion
More recursion! Nice to have an approach to handle loops or iterations in a cleaner, and at times more efficient. This is no one size fits all approach, but I believe it's a good approach to have ready in the toolbox for many cases that won't produce as stack overflow (especially if the programming language uses Tail Recursion Optimization). 

### Day 11: Thursday, September 19, 2024 - Function Composition & Currying 
Another day of practicing composition and currying. Yesterday, not the best. I implemented recursion with impure and pure functions in what felt like a sloppy way. Maybe I can redeem myself a bit today.  

### Day 12: Friday, September 20, 2024 - Immutability & Data Transformation
This is a practice of keeping functions pure. With this exercise, I utilize data structures given by pure/impure functions, but do not modify the original. Not very successful with this one today. I am trying to approach this using "closures" to handle state inside of impure functions, but messed it up. Will fix this tomorrow... 😔

### Day 13: Saturday, September 21, 2024 - Side Effects & IO Handling
Short run today (it is Saturday after all). I think I redeemed myself a bit from yesterday by doing the thing simply. I was trying to manage state in a closure, but ended up making it too complicated and really, using closures is outside of the inteneded scope of the exercise for immutabiltiy & data transformation anyway. Also did today's intended exercise to hanle IO in a way that isolates side effects (impure functions) from pure functions, where the pure function only uses the output of the side effect to do its thing. 

### Day 14: Sunday, September 22, 2024 - Rest 

### Day 15: Monday, September 23, 2024 - Pure Functions 
Not the greatest, but still tried to use impure functions to modify state then added a pure function to add to a name that was returned by the impure function. 

### Day 16: Tuesday, September 24, 2024 - Higher-Order Functions
Did it simply again today. Just using two pure functions as defaults into the pure function to modify the text or string. 

### Day 17: Wednesday, September 25, 2024 - Recursion
Simple filter that counts the number found for the target item in a list. 

### Day 18: Thursday, September 26, 2024 - Function Composition & Currying
Just currying today with a .jpg file format add to file name. 

### Day 19: Friday, September 27, 2024 - Immutability & Data Transformation 
Adding an item to a copy of a list from a function that generates a list then using another function to modify that list for a new list. 

### Day 20: Saturday, September 28, 2024 - Side Effects & IO Handling  
Setup for getting the host machines ip address, returning it, then modifying it by adding a port number. 

### Day 21: Sunday, September 29, 2024 - Rest

### Day 22: Monday, September 30, 2024 - Pure Functions
Checking to see if username exists. Ideally, I would be accessing the usernames with an impure function to get a copy of names in a database or some other data structure somewhere. But for today, this store of valid usernames is contained within the function that checks for them itself. 

### Day 23: Tuesday, September 31, 2024 - Higher-Order Functions
Higher-Order functions can either take in another function, or return another function, or do both, but doesn't have to do both to still be considered a higher-order function. Today, I made a mock procedure of an air conditioner system that has a set point (could be made to be a closure so that the set point can be updated) to check against a new temperature update. If the temperature set point is reached the air conditioner "turn off" procedure is executed like a callback and returns true if it successfully executes the procedure. There is no real code implemented that would be ran to execute the turn off procedure, but one could imagine some kind of concurrent procudure being ran like a timer or something that waits a little bit before turning off the air conditioner to ensure the room or space is sufficiently cooled after the set point is reached, such that it does not immediately turn of the air conditioner, lest an osciallating condition be created. This would also apply to an air conditioner turn on event where the set point for the target temperature is exceeded and then triggers an air conditioner on event. 