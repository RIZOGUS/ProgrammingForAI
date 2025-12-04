import pygame
import sys
import time

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []
        
    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               abs(self.board[i] - col) == abs(i - row):
                return False
        return True
    
    def solve(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])
            return True
        
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve(row + 1):
                    return True
                self.board[row] = -1
        
        return False
    
    def solve_all(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])
            return
        
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve_all(row + 1)
                self.board[row] = -1


class NQueensGUI:
    def __init__(self, n=8):
        pygame.init()
        self.n = n
        self.cell_size = 40
        self.board_size = self.n * self.cell_size
        self.info_height = 100
        self.screen = pygame.display.set_mode((self.board_size, self.board_size + self.info_height))
        pygame.display.set_caption(f"N-Queens Problem (N={n})")
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (50, 50, 50)
        self.LIGHT_SQUARE = (240, 217, 181)
        self.DARK_SQUARE = (181, 136, 99)
        self.QUEEN_COLOR = (220, 20, 60)
        self.HIGHLIGHT = (144, 238, 144)
        self.TEXT_COLOR = (0, 0, 0)
        self.INFO_BG = (230, 230, 250)
        
        self.font_large = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 28)
        self.font_small = pygame.font.Font(None, 22)
        
        self.solver = NQueens(n)
        self.solver.solve_all()
        self.current_solution = 0
        self.solving = False
        
    def draw_board(self, board=None):
        for row in range(self.n):
            for col in range(self.n):
                color = self.LIGHT_SQUARE if (row + col) % 2 == 0 else self.DARK_SQUARE
                pygame.draw.rect(self.screen, color,
                               (col * self.cell_size, row * self.cell_size,
                                self.cell_size, self.cell_size))
        
        if board:
            for row in range(len(board)):
                if board[row] != -1:
                    col = board[row]
                    center_x = col * self.cell_size + self.cell_size // 2
                    center_y = row * self.cell_size + self.cell_size // 2
                    pygame.draw.circle(self.screen, self.QUEEN_COLOR,
                                     (center_x, center_y), self.cell_size // 3)
                    
                    crown_points = [
                        (center_x, center_y - self.cell_size // 4),
                        (center_x - self.cell_size // 6, center_y - self.cell_size // 6),
                        (center_x - self.cell_size // 8, center_y),
                        (center_x, center_y - self.cell_size // 8),
                        (center_x + self.cell_size // 8, center_y),
                        (center_x + self.cell_size // 6, center_y - self.cell_size // 6)
                    ]
                    pygame.draw.polygon(self.screen, self.WHITE, crown_points)
    
    def draw_info_panel(self):
        pygame.draw.rect(self.screen, self.INFO_BG,
                        (0, self.board_size, self.board_size, self.info_height))
        
        title = self.font_large.render(f"N-Queens (N={self.n})", True, self.TEXT_COLOR)
        self.screen.blit(title, (20, self.board_size + 10))
        
        if self.solver.solutions:
            solution_text = self.font_medium.render(
                f"Solution {self.current_solution + 1} of {len(self.solver.solutions)}",
                True, self.TEXT_COLOR
            )
            self.screen.blit(solution_text, (20, self.board_size + 50))
            
            controls = self.font_small.render(
                "← Prev | Next → | Q: Quit",
                True, self.TEXT_COLOR
            )
            self.screen.blit(controls, (20, self.board_size + 80))
        else:
            instruction = self.font_medium.render(
                "No solutions found!",
                True, self.TEXT_COLOR
            )
            self.screen.blit(instruction, (20, self.board_size + 50))
    
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    
                    elif event.key == pygame.K_LEFT and self.solver.solutions:
                        self.current_solution = (self.current_solution - 1) % len(self.solver.solutions)
                    
                    elif event.key == pygame.K_RIGHT and self.solver.solutions:
                        self.current_solution = (self.current_solution + 1) % len(self.solver.solutions)
            
            self.screen.fill(self.WHITE)
            
            if self.solver.solutions:
                self.draw_board(self.solver.solutions[self.current_solution])
            else:
                self.draw_board()
            
            self.draw_info_panel()
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    n = 8
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            if n < 4:
                print("N must be at least 4")
                n = 4
        except ValueError:
            print("Invalid input, using N=8")
    
    print(f"\nN-Queens Problem Solver (N={n})")
    print("="*50)
    print("Controls:")
    print("  ← →   - Navigate between solutions")
    print("  Q     - Quit")
    print("="*50)
    
    gui = NQueensGUI(n)
    gui.run()
