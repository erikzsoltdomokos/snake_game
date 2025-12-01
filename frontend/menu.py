import pygame
from backend.difficulty import Difficulty, get_tick_rate
from .scoreboard import load_scores
from .sound_manager import SoundManager


class Menu:
    """Main menu system for Snake game."""
    
    def __init__(self):
        self.font = pygame.font.SysFont("consolas", 28)
        self.small = pygame.font.SysFont("consolas", 22)
        self.sound_manager = SoundManager()
        
        self.options = [
            ("Easy", Difficulty.EASY),
            ("Normal", Difficulty.NORMAL),
            ("Hard", Difficulty.HARD),
        ]
        self.selected = 1
        self.wrap_edges = False
        self.show_highscores = False
        
    def handle_events(self) -> tuple[bool, bool, bool]:
        """
        Handle menu events.
        Returns: (running, start_game, fullscreen_toggle)
        """
        start_game = False
        fullscreen_toggle = False
        running = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False
                elif event.key in (pygame.K_UP, pygame.K_w):
                    self.selected = (self.selected - 1) % len(self.options)
                    self.sound_manager.play('menu_move')
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.selected = (self.selected + 1) % len(self.options)
                    self.sound_manager.play('menu_move')
                elif event.key == pygame.K_r:
                    self.wrap_edges = not self.wrap_edges
                    self.sound_manager.play('menu_move')
                elif event.key == pygame.K_f:
                    fullscreen_toggle = True
                    self.sound_manager.play('menu_move')
                elif event.key in (pygame.K_h, pygame.K_F1):
                    self.show_highscores = not self.show_highscores
                    self.sound_manager.play('menu_move')
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    self.sound_manager.play('menu_select')
                    start_game = True
                    
        return running, start_game, fullscreen_toggle
    
    def render(self, screen, fullscreen: bool):
        """Render the menu."""
        screen.fill((25, 25, 30))
        title = self.font.render("Snake", True, (240, 240, 240))
        screen.blit(title, (20, 20))
        
        # Compute column width
        header_diff_w = self.small.size("Difficulty")[0]
        header_hotkeys_w = self.small.size("Controls:")[0]
        diff_widths = [self.font.size(lbl)[0] for (lbl, _) in self.options]
        hotkey_lines = [
            "Enter/Space: Start",
            "Up/Down or W/S: Select difficulty",
            "Move: Arrows or WASD",
            "R: Toggle wrap",
            "F: Toggle fullscreen (menu + game)",
            "H/F1: Toggle Top 10 highscores",
            "P: Pause, T: Theme",
            "Esc/Q: Quit",
        ]
        hotkey_widths = [self.small.size(line)[0] for line in hotkey_lines]
        column_width = max(diff_widths + hotkey_widths + [header_diff_w, header_hotkeys_w]) + 8
        
        col_x = 40
        
        # Section: Difficulty
        diff_header = self.small.render("Difficulty", True, (200, 200, 200))
        diff_header_y = 80
        screen.blit(diff_header, (col_x, diff_header_y))
        pygame.draw.line(
            screen,
            (90, 90, 100),
            (col_x, diff_header_y + diff_header.get_height() + 2),
            (col_x + diff_header.get_width(), diff_header_y + diff_header.get_height() + 2),
            1,
        )
        
        base_y = diff_header_y + diff_header.get_height() + 12
        for i, (label, _) in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected else (170, 170, 170)
            text = self.font.render(label, True, color)
            screen.blit(text, (col_x, base_y + i * 44))
        
        diff_label = self.options[self.selected][0]
        grid_size = (30, 20)
        info2 = self.small.render(
            f"Selected: {diff_label} | Wrap: {'On' if self.wrap_edges else 'Off'} | Grid: 30x20 | Tick: {get_tick_rate(self.options[self.selected][1])}",
            True,
            (200, 200, 200),
        )
        info2_x = screen.get_width() - info2.get_width() - 20
        screen.blit(info2, (info2_x, 200))
        
        # Top 10 highscores panel
        if self.show_highscores:
            scores = load_scores()
            try:
                scores = sorted(scores, key=lambda s: int(s.get("score", 0)), reverse=True)[:10]
            except Exception:
                scores = scores[:10]
            lines = ["Top 10"]
            for idx, s in enumerate(scores, start=1):
                diff = s.get("difficulty", "-")
                grid = s.get("grid", "-")
                sc = s.get("score", 0)
                name = s.get("name") or "—"
                lines.append(f"{idx}. {sc}  [{diff}] {grid}  - {name}")
            if len(lines) == 1:
                lines.append("No scores yet")
            
            widths = [self.small.size(line)[0] for line in lines]
            block_w = max(widths) if widths else 0
            x = screen.get_width() - block_w - 20
            y = 230
            header = self.small.render(lines[0], True, (210, 210, 210))
            screen.blit(header, (x, y))
            pygame.draw.line(screen, (90, 90, 100), (x, y + header.get_height() + 2), (x + header.get_width(), y + header.get_height() + 2), 1)
            y += header.get_height() + 10
            for line in lines[1:]:
                txt = self.small.render(line, True, (185, 185, 185))
                screen.blit(txt, (x, y))
                y += 22
        
        # Fullscreen toggle button
        fs_label = self.small.render("Windowed" if not fullscreen else "Fullscreen", True, (220, 220, 220))
        fs_rect = fs_label.get_rect()
        fs_rect.top = 20
        fs_rect.right = screen.get_width() - 16
        bg_rect = fs_rect.inflate(12, 8)
        pygame.draw.rect(screen, (40, 40, 50), bg_rect, border_radius=6)
        pygame.draw.rect(screen, (70, 70, 90), bg_rect, width=1, border_radius=6)
        screen.blit(fs_label, fs_rect)
        
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            if bg_rect.collidepoint(mx, my):
                return True  # Signal fullscreen toggle via mouse
        
        # Gap between difficulty and controls
        gap_y = base_y + len(self.options) * 44 + 24
        
        # Section: Controls
        hk_header = self.small.render("Controls:", True, (200, 200, 200))
        screen.blit(hk_header, (col_x, gap_y))
        pygame.draw.line(
            screen,
            (90, 90, 100),
            (col_x, gap_y + hk_header.get_height() + 2),
            (col_x + hk_header.get_width(), gap_y + hk_header.get_height() + 2),
            1,
        )
        hk_y = gap_y + hk_header.get_height() + 10
        for line in hotkey_lines:
            txt = self.small.render(line, True, (180, 180, 180))
            screen.blit(txt, (col_x, hk_y))
            hk_y += 24
            
        return False  # No mouse fullscreen toggle
    
    def get_selected_difficulty(self) -> Difficulty:
        """Get currently selected difficulty."""
        return self.options[self.selected][1]
    
    def get_grid_size(self) -> tuple[int, int]:
        """Get grid size for game."""
        return (30, 20)
