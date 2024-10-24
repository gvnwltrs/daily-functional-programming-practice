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

### Day 23: Tuesday, October 1, 2024 - Higher-Order Functions
Higher-Order functions can either take in another function, or return another function, or do both, but doesn't have to do both to still be considered a higher-order function. Today, I made a mock procedure of an air conditioner system that has a set point (could be made to be a closure so that the set point can be updated) to check against a new temperature update. The temperature set point is reached the air conditioner "turn off" procedure is executed like a callback and returns true if it successfully executes the procedure. There is no real code implemented that would be ran to execute the turn off procedure, but one could imagine some kind of concurrent procudure being ran like a timer or something that waits a little bit before turning off the air conditioner to ensure the room or space is sufficiently cooled after the set point is reached, such that it does not immediately turn of the air conditioner, lest an osciallating condition be created. This would also apply to an air conditioner turn on event where the set point for the target temperature is exceeded and then triggers an air conditioner on event. 

### Day 24: Wednesday, October 2, 2024 - Recursion
Used recursion today to calculate the average a list of home price values. The recursive function is generic though, in that it could be used to calculate the averages of other lists of int values. It returns the average as an int. If I wanted to format this output specifically for the house price averages, I could add a decorator in the future to modify it that way -- so it's extendable in this way. The recursive function itself has default arguments to help track the sum and the count of elements to produce the average. This could probably be done differently, maybe using a closure to make the function a one argument function. 

### Day 25: Thursday, October 3, 2024 - Composition & Currying
Made a curried function for formatting and combining size and weight details for a person. The original simply took in a size and weight integer. The composed and curried version takes in two separate functions that handle the formatting or other calculations for size and weight separately (which wil allow for future functions to be added for extension such as different formats, calculations, etc. given the use case). 

### Day 26: Friday, October 4, 2024 - Immutability & Data Structures
To practice this, I set up a simple data structure for a hypothetical restaurant order menu that is processed in a pure function to determine the final price. This promotes extensibility where there could potentially be another managing function that determines the location of the purchase to appropriately apply the sales tax in the final price based on the location of the purchase. 

### Day 27: Saturday, October 5, 2024 - Side Effects & IO 
Made a weather web API call today with a side effect based function (impure) and used the data gathered from it to output the forecast with a pure function where the output is a formatted string for a "Today's" weather temperature output for the given location. 

### Day 28: Sunday, October 6, 2024 - Rest

### Day 29: Monday, October 7, 2024 - Pure Functions
It seems hard at times to come up with ideas for pure functions outside of mathematical operations. It seems to be more the case that pure functions are generally more applicable in the case of using an impure function or operation first that returns a thing to then act on the result with a pure function. Today I made a pure function that simply calculates speed. 

### Day 30: Tuesday, October 8, 2024 - Higher-Order Functions
Technically the last day of practicing with Python. I will continue for one more month though to solidify this more. Added feature to output an investment portfolio distribution based on a person's temperament. 

### Day 31: Wednesday, October 9, 2024 - Recursion
Calculating high payment events using recursion. The single function simply takes in a list of integers, and uses defaults to determine what "high" is and outputs the count of events that exceeds that limit. 

### Day 32: Thursday, October 10, 2024 - Function Composition & Currying
Okay, so maybe I haven't been currying. I just realized I largely misunderstood what currying is compared to function composition... So, today I actually made a curried function for the first time just with adding up sums. I made a few different units tests to make sure I actually understand this using different "pre-fill" scenarios. 

### Day 33: Friday, October 11, 2024 - Immutability & Data Transformations 
Passing an input of a dictionary that contains a list of dictionaries for a bunch of events. The goal is to delete all the event entries except for the last one. Instead of taking the data structure and modifying the original, we get a copy of it and slice the entries out except for the last one to return a new data structure for events. 

### Day 34: Saturday, October 12, 2024 - Side Effects & IO
Keeping it super simple today. Today I use a side effect or impure function to grab the systems current date and time, then pass the data over to a pure function that formats the data for a string output. I isolate the datetime system calls to one being used in the unit test and one being called with a module function that then passes the data to a pure function. I could have just used the datetime in the unit test, but I wanted to practice this as a process in functional programming. The string output that comes from the pure function could be used by passing it to another side effect.  

### Day 35: Sunday, October 13, 2024 - Rest

### Day 36: Monday, October 14, 2024 - Pure Functions 
After practicing a number of pure functions, I am finding these to be the only kind of functions I want to write. I love simple, single return line style functions. They are beautiful. Anyway, today I just made I simple pure function that strips away any numbers from a string. No thrills. Another thing I picked up though was how to looking a code in a functional way. You break the code up into 3 categories: actions, calculations, and data. Actions is the most difficult part of the code that requires more attention because an action type execution means you have a function with side effects. Calculations are ideal for executable parts of the code. Calculations are basically what pure functions are. It doesn't always have to be mathematical, a calculation function and simply perform an operation like decision making or some other task, but the result is always the same, it doesn't matter when it is called. Data is simple. This is the easiest part of the code.  

### Day 37: Tuesday, October 15, 2024 - Higher-Order Functions 
Using higher-order functions is pretty fun. There are so many ways you can refactor some side-effects into calculations, and then handle the calculations (pure functions) smartly with higher-order functions to help produce a pure function. Today the higher-order function is a mock email planning output, where a subscriber is selected, a single one in this case, from a dictionary data structure, then based on the value for referrals for the subscriber a coupon code is selected. This subscriber and coupon selection is all done in the higher order function that takes getting a get subscriber function as the argument and also uses a default coupon selector function in the arugment to help gather the details to construct an email message in JSON format (from, to, subject, body). This is very extendable where another function could be made that takes all the subscribers in an email list and creates a coupon email message list output for them all. Could be implemented using a wrapper that takes the single output given by the original and a new function as the input parameter to get all the subscribers to produce a full collection of emails to send out. 

### Day 38: Wednesday, October 16, 2024 - Recursion
Lazy approach today. Just doing a recursive sum calculation based on a list of numbers. Ideally, there should be some implementation of Tail Call Optimization (TCO), where the calculation is tracked and a new stack is used recursively to prevent a stack overflow in the event the list is very large since its size complexity is O(n). 

### Day 39 Thursday, October 17, 2024 - Function Composition & Currying
Built a simple curried sentence builder, where each successive input builds out the sentence. 

### Day 40 Friday, October 18, 2024 - Immutability & Data Transformations 
Just made a simple email message builder, a shallow copy, and some currying to implement it all. Not very pretty looking, but it works and this helps with practicing currying a little more. 

### Day 41 Saturday, October 19, 2024 - Side Effects & IO 
Made another email list output. The side-effect gets the usernames and emails from a txt file, then the pure function (calculation) extracts the username and email to output all of them as a dictionary (JSON). 

### Day 42 Sunday, October 20, 2024 - Rest 

### Day 43 Monday, October 21, 2024 - Pure Functions
Built a feature to set up a Class C IP Address using a single argument for the last octet, or a two argument input to set a subnet with the last octet. 

### Day 44 Tuesday, October 22, 2024 - Higher-Order Functions
Created a higher-order function that formats a collection of phone numbers with '-' where needed. The function simply takes a collection of phone numbers as a single input with the optional second input set to a default input function that is for '-' formatting. This way, if future implementations are needed to format phone numbers in a particular way, it can simply be used as input for the second argument. 

### Day 45 Wednesday, October 23, 2024 - Recursion
Made up a mock program load sequence that uses recursion for each load stage based on a tracking value known as "stage". Theoretically, this can be expanded on to implement other functions that handle some operation or sub-routine at each stage. The final output is a log dictionary that could then be used as a signal or info to launch other events based on its values.  

### Day 46 Thursday, October 24, 2024 - Composition & Currying
Composition is pretty straightforward. I am focusing on more currying today to apply it to hopefully identify situations that could use currying for refactoring better. I learned that what I have been doing for "currying" before was actually a partial function since I was prefilling the return of an inner function with the initial argument in the first call. So I made 2 versions, one partial, one curry to make sure I understand the difference. This was just a function that sets up a sales tax for a particular state so that a total price can be given including the sales tax. 
