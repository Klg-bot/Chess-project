import pygame
import os

class Board:
    def __init__(self, rows=8, cols=8, sq_size=60):
        self.rows = rows
        self.cols = cols
        self.sq_size = sq_size
        self.pieces = self.load_pieces()
        self.board_state = self.starting_position()
        self.selected = None

    def load_pieces(self):
        """
        Loads piece images from an 'assets' directory.
        Expects filenames like 'wP.png', 'bK.png', etc.
        """
        pieces = {}
        path = os.path.join('assets')
        for color in ['w', 'b']:
            for piece in ['K', 'Q', 'R', 'B', 'N', 'P']:
                key = f"{color}{piece}"
                img_path = os.path.join(path, f"{key}.png")
                image = pygame.image.load(img_path)
                pieces[key] = pygame.transform.scale(image, (self.sq_size, self.sq_size))
        return pieces

    def starting_position(self):
        """Return standard starting array (8×8) for a chess game."""
        return [
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bP']*8,
            ['']*8,
            ['']*8,
            ['']*8,
            ['']*8,
            ['wP']*8,
            ['wR','wN','wB','wQ','wK','wB','wN','wR']
        ]

    def draw(self, screen):
        """
        Draw the board squares and pieces. Highlight the selected square.
        """
        colors = [(255, 255, 255), (100, 100, 100)]
        for r in range(self.rows):
            for c in range(self.cols):
                rect = pygame.Rect(c*self.sq_size, r*self.sq_size, self.sq_size, self.sq_size)
                pygame.draw.rect(screen, colors[(r + c) % 2], rect)
                piece = self.board_state[r][c]
                if piece:
                    screen.blit(self.pieces[piece], rect.topleft)
        if self.selected:
            sr, sc = self.selected
            highlight = pygame.Surface((self.sq_size, self.sq_size), pygame.SRCALPHA)
            highlight.fill((0, 255, 0, 100))
            screen.blit(highlight, (sc*self.sq_size, sr*self.sq_size))
