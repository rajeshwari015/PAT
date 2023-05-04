"""Given a boolean expression with the following symbols. 
Symbols 
    'T' ---> true 
    'F' ---> false 
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR 
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true. 
Let the input be in form of two arrays one contains the symbols (T and F) in order and the other contains operators (&, | and ^}
Examples: 
Input: symbol[]    = {T, F, T}
       operator[]  = {^, &}
Output: 2
The given expression is "T ^ F & T", it evaluates tr


Input: symbol[]    = {T, F, T}
       operator[]  = {^, |}
Output: 2
The given expression is "T ^ F | F", it evaluates true
in two ways "( (T ^ F) | F )" and "( T ^ (F | F) )". 

Input: symbol[]    = {T, T, F, T}
       operator[]  = {|, &, ^}
Output: 4
The given expression is "T | T & F ^ T", it evaluates true
in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T)  
and (T|((T&F)^T))
Let T(i, j) represent the number of ways to parenthesize the symbols between i and j (both inclusive) such that the subexpression between i and j evaluates to true. 
 
 
  

 
Let F(i, j) reprsent the number of ways to parenthesize the symbols between i and j (inclusive) such that the subexpression between i and j evaluates to false. Base Cases:
T(i, i) = 1 if symbol[i] = 

F(i, i) = 1 if symbol[i] = 'F'
F(i, i) = 0 if symbol[i] = '
If we draw the recursion tree of the above recursive solution, we can observe that it has many overlapping subproblems.

Code:
"""
def countParenth(symb, oper, n):
    F = [[0 for i in range(n + 1)]
    for i in range(n + 1)]
    T = [[0 for i in range(n + 1)]
    for i in range(n + 1)]
    for i in range(n):
        if symb[i] == 'F':
            F[i][i] = 1
	else:
	    F[i][i] = 0

	if symb[i] == 'T':
	    T[i][i] = 1
	else:
            T[i][i] = 0
	for gap in range(1, n):
		i = 0
		for j in range(gap, n):
			T[i][j] = F[i][j] = 0
			for g in range(gap):
				k = i + g
				tik = T[i][k] + F[i][k]
				tkj = T[k + 1][j] + F[k + 1][j]
				if oper[k] == '&':
					T[i][j] += T[i][k] * T[k + 1][j]
					F[i][j] += (tik * tkj - T[i][k] *
								T[k + 1][j])
				if oper[k] == '|':
					F[i][j] += F[i][k] * F[k + 1][j]
					T[i][j] += (tik * tkj - F[i][k] *
								F[k + 1][j])
				if oper[k] == '^':
					T[i][j] += (F[i][k] * T[k + 1][j] +
								T[i][k] * F[k + 1][j])
					F[i][j] += (T[i][k] * T[k + 1][j] +
								F[i][k] * F[k + 1][j])
			i += 1
	return T[0][n - 1]
symbols = "TTFT"
operators = "|&^"
n = len(symbols)
print(countParenth(symbols, operators, n))



