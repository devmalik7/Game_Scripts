"""
Main game controller that coordinates game logic and UI.
"""
from game.board import Board
from game.constants import COLOR_BACKGROUND, COLOR_X_MARK, COLOR_O_MARK, COLOR_DRAW
from ui.canvas import GameCanvas
from ui.animations import AnimationManager
from ui.components import UIComponents


class GameController:
    """Main game controller coordinating all components."""

    def __init__(self, root):
        """
        Initialize the game controller.

        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg=COLOR_BACKGROUND)

        # Initialize game logic
        self.board = Board()
        self.game_over = False

        # Initialize canvas
        self.game_canvas = GameCanvas(root)
        self.game_canvas.draw_grid()

        # Initialize animation manager
        self.animation_manager = AnimationManager(
            root,
            self.game_canvas.canvas,
            self.game_canvas.grid_offset_x,
            self.game_canvas.grid_offset_y,
        )

        # Initialize UI components
        self.ui_components = UIComponents(self.game_canvas.canvas)
        self.ui_components.draw_title()

        # Bind click events
        self.game_canvas.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        """
        Handle canvas click events.

        Args:
            event: Click event object
        """
        if self.game_over or self.animation_manager.animation_in_progress:
            return

        row, col = self.game_canvas.get_cell_from_click(event.x, event.y)

        if row is not None and col is not None:
            if self.board.make_move(row, col):
                self.animate_mark(row, col, self.board.current_player)

    def animate_mark(self, row, col, player):
        """
        Animate drawing a mark on the board.

        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            player: 'X' or 'O'
        """
        if player == "X":
            self.animation_manager.animate_x(row, col, self.check_game_state)
        else:
            self.animation_manager.animate_o(row, col, self.check_game_state)

    def check_game_state(self):
        """Check game state for wins or draw."""
        winner, winning_combo = self.board.check_winner()

        if winner:
            self.game_over = True
            self.animation_manager.animate_winning_line(
                winning_combo, lambda: self.show_winner_message(winner)
            )
        elif self.board.is_full():
            self.game_over = True
            self.show_draw_message()
        else:
            # Switch to next player
            self.board.switch_player()

    def show_winner_message(self, winner):
        """
        Show winner message.

        Args:
            winner: 'X' or 'O'
        """
        message = f"Player {winner} Wins!"
        color = COLOR_X_MARK if winner == "X" else COLOR_O_MARK

        def on_text_created(text_id):
            self.animation_manager.animate_bounce_text(
                text_id, 150, 170, self.show_play_again_button
            )

        self.ui_components.show_result_message(message, color, on_text_created)

    def show_draw_message(self):
        """Show draw message."""

        def on_text_created(text_id):
            self.animation_manager.animate_bounce_text(
                text_id, 150, 170, self.show_play_again_button
            )

        self.ui_components.show_result_message(
            "It's a Draw!", COLOR_DRAW, on_text_created
        )

    def show_play_again_button(self):
        """Show the play again button."""
        self.ui_components.create_play_again_button(self.reset_game)

    def reset_game(self):
        """Reset the game to initial state."""
        # Cancel all animations
        self.animation_manager.cancel_all_animations()

        # Clear canvas
        self.game_canvas.clear_marks()
        self.game_canvas.clear_results()

        # Reset game state
        self.board.reset()
        self.game_over = False
        self.animation_manager.animation_in_progress = False
