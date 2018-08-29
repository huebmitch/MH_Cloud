
import rg

class Robot:

    def act(self, game):

        team = {loc for loc in game.robots if game.robots[loc].player_id == self.player_id}

        if(len(team) < 9):
            if self.location == rg.CENTER_POINT:
                return ['guard']

            if rg.loc_types(self.location) == "spawn":
                return ['move', rg.toward(self.location, rg.CENTER_POINT)]

            # if there are enemies around, attack them
            for loc, bot in game.robots.iteritems():
                if bot.player_id != self.player_id:
                    if rg.dist(loc, self.location) <= 1:
                        return ['attack', loc]

            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        else:
            for loc, bot in game.robots.iteritems():

                if bot.player_id != self.player_id and self.hp <= 8:
                    if rg.dist(loc, self.location) <= 1:
                        return ['suicide']

                if bot.player_id != self.player_id:
                    if rg.dist(loc, self.location) <= 1 and self.hp >= 8:
                        return ['attack', loc]

            # return something
            if rg.loc_types(self.location) == "spawn":
                return ['move', rg.toward(self.location, rg.CENTER_POINT)]
            if game.turn <= 49:
                return ['move', rg.toward(self.location, (15,9))]
            if(game.turn > 49 and game.turn < 70):
                return ['move', rg.toward(self.location, (3, 9))]
            if(game.turn >= 70):
                return ['move', rg.toward(self.location, (15, 9))]

        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
