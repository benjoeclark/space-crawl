class Subgame:
    """Superclass for all subgames"""
    def __init__(self, game):
        """Initialize the subgame"""
        self.game = game
        self.initialize()
        self.game.display.draw()
        self.run()

    def run(self):
        """Run the subgame"""
        while self.game.game_running:
            command = self.game.display.get_user_input()
            if command == 'quit':
                self.game.game_over()
            elif command == 'help':
                self.show_help()
            else:
                self.handle_command(command)
            self.game.display.draw()
