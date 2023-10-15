
import argparse
from solvers.depth_first_search import solver

def main(N = 8):
    board = [[0 for x in range(N)] for y in range(N)]

    if solver(board, 0, N) == False:
        print("Solution does not exist")
        return False

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='N-Queen solver Cli')
    
    parser.add_argument('n', type=int,
                    help='A number of chessboard dimensions')
    
    args = parser.parse_args()
    
    main(args.n)