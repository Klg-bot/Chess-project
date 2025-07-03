# rules.py — pure move-generation logic

BOARD_SIZE = 8

def is_enemy(piece, target):
    """True if target is occupied by the opposite color."""
    return bool(piece and target and piece[0] != target[0])

def pawn_moves(board, r, c):
    moves = []
    color = board[r][c][0]
    direction = -1 if color == 'w' else 1

    # forward one
    nr = r + direction
    if 0 <= nr < BOARD_SIZE and board[nr][c] == '':
        moves.append((nr, c))

    # captures
    for dc in (-1, 1):
        nc = c + dc
        if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
            if is_enemy(board[r][c], board[nr][nc]):
                moves.append((nr, nc))
    return moves

def knight_moves(board, r, c):
    deltas = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    moves = []
    for dr, dc in deltas:
        nr, nc = r+dr, c+dc
        if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
            if board[nr][nc] == '' or is_enemy(board[r][c], board[nr][nc]):
                moves.append((nr, nc))
    return moves

def sliding_moves(board, r, c, directions):
    moves = []
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        while 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
            if board[nr][nc] == '':
                moves.append((nr, nc))
            else:
                if is_enemy(board[r][c], board[nr][nc]):
                    moves.append((nr, nc))
                break
            nr += dr
            nc += dc
    return moves

def bishop_moves(board, r, c):
    return sliding_moves(board, r, c, [(-1,-1),(-1,1),(1,-1),(1,1)])

def rook_moves(board, r, c):
    return sliding_moves(board, r, c, [(-1,0),(1,0),(0,-1),(0,1)])

def queen_moves(board, r, c):
    return bishop_moves(board, r, c) + rook_moves(board, r, c)

def king_moves(board, r, c):
    deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    moves = []
    for dr, dc in deltas:
        nr, nc = r+dr, c+dc
        if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
            if board[nr][nc] == '' or is_enemy(board[r][c], board[nr][nc]):
                moves.append((nr, nc))
    return moves

def legal_moves(board, r, c):
    piece = board[r][c]
    if not piece:
        return []
    kind = piece[1]
    if kind == 'P': return pawn_moves(board, r, c)
    if kind == 'N': return knight_moves(board, r, c)
    if kind == 'B': return bishop_moves(board, r, c)
    if kind == 'R': return rook_moves(board, r, c)
    if kind == 'Q': return queen_moves(board, r, c)
    if kind == 'K': return king_moves(board, r, c)
    return []
