def update_grid(grid, piece, col):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell == 1:
                if i < len(grid) and col + j < len(grid[i]):
                    grid[i][col + j] = 1

def get_height(grid):
    for i in range(len(grid)):
        if any(cell == 1 for cell in grid[i]):
            return len(grid) - i-1
    return 0

def tetris(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        sequences = input_file.readlines()

    results = []
    for sequence in sequences:
        sequence = sequence.strip()
        if not sequence:
            # Skip empty lines
            continue

        actions = sequence.split(',')
        grid = [[0] * 10 for _ in range(100)]

        for action in actions:
            try:
                shape, col = action[0], int(action[1:])
                if 0 <= col < 10:  # Check if the column index is within the valid range
                    piece = None
                    if shape == 'I':
                        piece = [[1, 1, 1, 1]]
                    elif shape == 'L':
                        piece = [[1, 0], [1, 0], [1, 1]]
                    elif shape == 'J':
                        piece = [[0, 1], [0, 1], [1, 1]]
                    elif shape == 'S':
                        piece = [[0, 1, 1], [1, 1, 0]]
                    elif shape == 'Z':
                        piece = [[1, 1, 0], [0, 1, 1]]
                    elif shape == 'T':
                        piece = [[1, 1, 1], [0, 1, 0]]
                    elif shape == 'Q':
                        piece = [[1, 1], [1, 1]]

                    if piece:
                        for i in range(len(piece)):
                            for j in range(len(piece[i])):
                                if piece[i][j] == 1:
                                    col_idx = col + j
                                    row_idx = 0
                                    while row_idx < 100 and grid[row_idx][col_idx] == 0:
                                        row_idx += 1
                                    grid[row_idx - 1][col_idx] = 1
                else:
                    print(f"Skipping invalid column index: {action}")
            except (IndexError, ValueError):
                print(f"Skipping invalid input action: {action}")

        # Calculate the maximum height
        max_height = get_height(grid)
        results.append(max_height)

    with open(output_filename, 'w') as output_file:
        output_file.write('\n'.join(map(str, results)))

if __name__ == "__main__":
    tetris("input.txt", "output.txt")
