# Simple Calculator app

### Purpose:
This app was developed as part of a project on boot.dev. The project was programing an application to use Google AI to
edit code. Originally the calculator only had addition, subtraction, multiplication and division. Using GenAI, the code 
first had all bugs fixed, then had exponentiation and parenthetical notation added.

### Syntax:
calculator/main.py "\<expression>"
- format is standard math notation _number operator number_
- e.g. "3 + 2 * 5"
- *result: 13*
- parenthesis can be used to override normal order of operations
- eg "(3 + 2) * 5"
- *result: 25* 