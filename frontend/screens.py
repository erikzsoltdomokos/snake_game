import pygame
from backend.difficulty import Difficulty
from .scoreboard import load_scores


def qualifies_top10(existing_scores, new_score, n=10):
    """Check if a score qualifies for top N."""
    try:
        ranked = sorted(existing_scores, key=lambda s: int(s.get("score", 0)), reverse=True)
    except Exception:
        ranked = existing_scores
    if len(ranked) < n:
        return True
    try:
        min_top = int(ranked[n - 1].get("score", 0))
    except Exception:
        min_top = 0
    return new_score > min_top


def prompt_name(screen, score, difficulty: Difficulty, grid_size: tuple[int, int]) -> str:
    """Prompt user for name if they qualify for top 10."""
    font = pygame.font.SysFont("consolas", 28)
    small = pygame.font.SysFont("consolas", 20)
    name = ""
    max_len = 16

    entering = True
    while entering:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                entering = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    entering = False
                elif event.key == pygame.K_RETURN:
                    entering = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    ch = event.unicode
                    if ch and ch.isprintable() and ch not in {"\r", "\n", "\t"}:
                        if len(name) < max_len:
                            name += ch

        # Draw prompt overlay
        screen.fill((25, 25, 30))
        title = font.render("New Top 10!", True, (240, 240, 240))
        screen.blit(title, (20, 20))
        sub = small.render(
            f"Score: {score}  |  {difficulty.name}  |  Grid {grid_size[0]}x{grid_size[1]}", True, (200, 200, 200)
        )
        screen.blit(sub, (20, 60))

        prompt = small.render("Enter your name (max 16):", True, (210, 210, 210))
        screen.blit(prompt, (20, 110))

        # Input box
        box_rect = pygame.Rect(20, 140, max(260, small.size(name or " ")[0] + 20), 34)
        pygame.draw.rect(screen, (40, 40, 50), box_rect, border_radius=6)
        pygame.draw.rect(screen, (90, 90, 110), box_rect, width=1, border_radius=6)

        # Cursor blink
        show_cursor = (pygame.time.get_ticks() // 500) % 2 == 0
        display_name = name + ("_" if show_cursor else "")
        txt_surface = small.render(display_name if name else ("_" if show_cursor else " "), True, (235, 235, 235))
        screen.blit(txt_surface, (box_rect.x + 10, box_rect.y + 6))

        hint = small.render("Enter: Save    Esc: Skip", True, (160, 160, 160))
        screen.blit(hint, (20, box_rect.bottom + 12))

        pygame.display.flip()
        pygame.time.delay(16)

    return name.strip()


def show_game_over(screen, score: int, difficulty: Difficulty, grid_size: tuple[int, int]) -> bool:
    """
    Display game over screen.
    Returns True if user wants to restart with same settings.
    """
    font = pygame.font.SysFont("consolas", 28)
    small = pygame.font.SysFont("consolas", 22)
    title_font = pygame.font.SysFont("consolas", 36, bold=True)
    
    # Semi-transparent overlay
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((10, 10, 14, 180))
    screen.blit(overlay, (0, 0))
    
    # Centered box
    box_w, box_h = 500, 280
    box_x = (screen.get_width() - box_w) // 2
    box_y = (screen.get_height() - box_h) // 2
    box_rect = pygame.Rect(box_x, box_y, box_w, box_h)
    
    # Box background and border
    pygame.draw.rect(screen, (30, 32, 40), box_rect, border_radius=12)
    pygame.draw.rect(screen, (80, 80, 100), box_rect, width=2, border_radius=12)
    
    # Title
    title = title_font.render("GAME OVER", True, (240, 80, 80))
    title_rect = title.get_rect(center=(box_x + box_w // 2, box_y + 45))
    screen.blit(title, title_rect)
    
    # Score
    score_txt = font.render(f"Score: {score}", True, (240, 240, 240))
    score_rect = score_txt.get_rect(center=(box_x + box_w // 2, box_y + 100))
    screen.blit(score_txt, score_rect)
    
    # Difficulty & Grid
    info_txt = small.render(f"{difficulty.name} | Grid: {grid_size[0]}x{grid_size[1]}", True, (200, 200, 200))
    info_rect = info_txt.get_rect(center=(box_x + box_w // 2, box_y + 140))
    screen.blit(info_txt, info_rect)
    
    # Instructions
    instructions = [
        "R: Restart with same settings",
        "Any other key: Return to menu"
    ]
    y_offset = box_y + 190
    for line in instructions:
        txt = small.render(line, True, (180, 180, 180))
        txt_rect = txt.get_rect(center=(box_x + box_w // 2, y_offset))
        screen.blit(txt, txt_rect)
        y_offset += 30
    
    pygame.display.flip()

    wait = True
    restart = False
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart = True
                wait = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                wait = False
        pygame.time.delay(16)
        
    return restart
