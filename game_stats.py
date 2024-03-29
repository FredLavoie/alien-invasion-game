class GameStats:
    """ Track game statistics """

    def __init__(self, ai_game):
        """ Initialize statistics """
        self.settings = ai_game.settings
        self.reset_stats()
        # Start game in active state
        self.game_active = True

        # Start game in an inactive state
        self.game_active = False

        # Hight score should never be reset
        with open('score_save.txt') as file_object:
            saved_score = file_object.read()
            self.high_score = int(saved_score)

    def reset_stats(self):
        """ Initialize statistics that can change during game """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 0 # had to start at zero, book said 1 ??