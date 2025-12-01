import sys
import pygame

from frontend.menu import Menu
from frontend.game_loop import run_game
from frontend.screens import qualifies_top10, prompt_name, show_game_over
from frontend.scoreboard import save_score, load_scores


def main():
    """Entry point for Snake game."""
    pygame.init()
    pygame.display.set_caption("Snake")
    
    # Initialize menu and display
    menu = Menu()
    fullscreen = True
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    running = True
    while running:
        # Handle menu events
        running, start_game, fs_toggle = menu.handle_events()
        
        # Handle fullscreen toggle
        if fs_toggle:
            fullscreen = not fullscreen
            flags = pygame.FULLSCREEN if fullscreen else 0
            screen = pygame.display.set_mode((0, 0) if fullscreen else (600, 400), flags)
        
        # Check for mouse-triggered fullscreen toggle
        mouse_fs_toggle = menu.render(screen, fullscreen)
        if mouse_fs_toggle:
            fullscreen = not fullscreen
            flags = pygame.FULLSCREEN if fullscreen else 0
            screen = pygame.display.set_mode((0, 0) if fullscreen else (600, 400), flags)
        
        pygame.display.flip()
        pygame.time.delay(16)
        
        # Start game if requested
        if start_game:
            grid_size = menu.get_grid_size()
            difficulty = menu.get_selected_difficulty()
            
            # Run the game
            score, fullscreen = run_game(
                grid_size,
                difficulty,
                cell_size=20,
                wrap_edges=menu.wrap_edges,
                start_fullscreen=fullscreen,
            )
            
            # Restore screen after game
            flags = pygame.FULLSCREEN if fullscreen else 0
            screen = pygame.display.set_mode((0, 0) if fullscreen else (600, 400), flags)
            
            # Check if score qualifies for top 10
            name_to_save = ""
            try:
                scores = load_scores()
            except Exception:
                scores = []
            
            if qualifies_top10(scores, score):
                name_to_save = prompt_name(screen, score, difficulty, grid_size)
            
            # Save score
            try:
                save_score({
                    "score": score,
                    "difficulty": difficulty.name,
                    "grid": f"{grid_size[0]}x{grid_size[1]}",
                    "name": name_to_save,
                })
            except Exception:
                pass
            
            # Show game over screen
            restart = show_game_over(screen, score, difficulty, grid_size)
            if restart:
                # Immediate restart with same settings - just continue the loop
                start_game = True
                continue
    
    pygame.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
