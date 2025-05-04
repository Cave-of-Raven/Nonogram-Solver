import enum

Axis = enum.StrEnum('Axis', [('ROW', enum.auto()), ('COLUMN', enum.auto())])

gridRows = 0
gridColumns = 0

rowClues = []
columnClues = []
grid = []

# Initialize Nonogram grid to all empty tiles
def InitGrid() -> None:
    global grid
    grid = [[0 for _ in range(gridColumns)] for _ in range(gridRows)]
    
    
# Prompts the user for clues for the row or column, depending on the Axis enum
def GetClues(axis: Axis) -> None:
    num = None
    axisStr = None
    if axis == Axis.ROW:
        num = gridRows
        axisStr = 'row'
    elif axis == Axis.COLUMN:
        num = gridColumns
        axisStr = 'column'
        
    for i in range(gridRows):
        clue = []
        clueString = input(f"Input clue for {axisStr} {i + 1}: ")
        
        currentNumber = 0
        for num in clueString:
            if num.isnumeric():
                currentNumber = (currentNumber * 10) + int(num)
            else:
                clue.append(currentNumber)
                currentNumber = 0
        if currentNumber != 0:
            clue.append(currentNumber)
        
        if axis == Axis.ROW:
            rowClues.append(clue)
        elif axis == Axis.COLUMN:  
            columnClues.append(clue)


# Displays the grid in ASCII
def DisplayGrid() -> None:
    rowStr = ''
    for _, row in enumerate(grid):
        for col in row:
            rowStr = '  '.join([rowStr, 'X' if col else '-'])
        print(rowStr)
        rowStr = ''


def GetGridInfo():
    global gridRows, gridColumns, grid
    gridRows = int(input("Enter the grid height: "))
    gridColumns = int(input("Enter the grid width: "))
    InitGrid()
    
    GetClues(Axis.ROW)
    #GetClues(Axis.COLUMN)
        
    print(rowClues)
    print(columnClues)


def FillGridByOverlap():
    for i, rowClue in enumerate(rowClues):
        clueSum = gridColumns
        for clue in rowClue:
            clueSum -= clue
        clueSum -= (len(rowClue) - 1)
        
        horizontalIndex = 0
        for rowIndex, clue in enumerate(rowClue):
            print(i)
            if clue > clueSum:
                horizontalIndex += clueSum
                for _ in range(clue - clueSum):
                    grid[i][horizontalIndex] = 1
                    horizontalIndex += 1
            else:
                horizontalIndex += clue
            if rowIndex != len(rowClue) - 1:
                horizontalIndex += 1
                
    for i, columnClue in enumerate(columnClues):
        clueSum = gridRows
        for clue in columnClue:
            clueSum -= clue
        clueSum -= (len(columnClue) - 1)
        
        horizontalIndex = 0
        for rowIndex, clue in enumerate(columnClue):
            print(i)
            if clue > clueSum:
                horizontalIndex += clueSum
                for _ in range(clue - clueSum):
                    grid[i][horizontalIndex] = 1
                    horizontalIndex += 1
            else:
                horizontalIndex += clue
            if rowIndex != len(columnClue) - 1:
                horizontalIndex += 1


def SolveNonogram():
    FillGridByOverlap()


def main():
    print("Starting Nonogram Solver...")
    GetGridInfo()
    SolveNonogram()
    DisplayGrid()

main()