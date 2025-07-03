from board import Board
import rules

class Game:
    """
    Controller: manages turns, applies rules, updates Board.selected.
    """
    def __init__(self, rows=8, cols=8, sq_size=60):
        self.board = Board(rows=rows, cols=cols, sq_size=sq_size)
        self.current_player = 'w'
        self.selected = None

    def handle_click(self, pos):
        r = pos[1] // self.board.sq_size
        c = pos[0] // self.board.sq_size
        state = self.board.board_state

        if self.selected:
            sr, sc = self.selected
            legal = rules.legal_moves(state, sr, sc)
            if (r, c) in legal:
                # perform move / capture
                state[r][c] = state[sr][sc]
                state[sr][sc] = ''
                # switch player
                self.current_player = 'b' if self.current_player == 'w' else 'w'
            self.selected = None
        else:
            piece = state[r][c]
            if piece and piece[0] == self.current_player:
                self.selected = (r, c)

        self.board.selected = self.selected
