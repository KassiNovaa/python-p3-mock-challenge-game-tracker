class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not hasattr(self,'_title'):
            if type(new_title) == str and len(new_title) > 0:
                self._title = new_title
    
    @property
    def results(self):
        return [ results for results in Result.all if results.game == self ]
    
    @property
    def players(self):
        return list ({ results.player for results in self.results })

    def average_score(self, player):
        if player in self.players:
            player_results = [result.score for result in player.results if result.game == self]
            return sum(player_results) / len(player_results)
        return 0
    
    # if the player is found in the list of players method, calculate the average score based on the player's results for the current game. If the player is not found, the method will directly reach the return 0 statement.

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if type(new_username) == str and 2 <= len(new_username) <= 16:
            self._username = new_username

    @property
    def results(self):
        return [ results for results in Result.all if results.player == self ]

    def games_played(self):
        return list({ results.games for results in self.results })

    @property
    def played_game(self, game):
        for result in self.results:
            if result.game == game:
                return True
        return False
    
        # return any(result.game == game for result in self.results)
        # we use the any() function to check if at least one of the boolean values in the list is True.

    def num_times_played(self, game):
        return len([g for g in self.games_played if g == game])
    # cannot use the variable name more than once it will cause errors

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,new_score):
        if not hasattr(self,"_score"):
            if type(new_score) == int and 1 <= (new_score) <= 5000:
                self._score = new_score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self,new_player):
        if isinstance( new_player, Player):
            self._player = new_player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance( new_game, Game ):
            self._game = new_game