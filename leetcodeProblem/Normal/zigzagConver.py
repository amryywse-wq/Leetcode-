grid =[
    ['P'],[' '],[' '],['I'],
    ['A'],[' '],['L'],[' '],
    ['Y'],['A'],[' '],[' '],
    ['P'],[' '],[' '],[' ']
]

for i in range(len(grid)) :
    if grid[i][0] != ' ':
        print(grid[i][0], end='')
    