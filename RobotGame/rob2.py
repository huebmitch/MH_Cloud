import rg
class Robot:
    def act(self, game):
        
        team = set()
        enemyTeam = set()
        for loc, robot in game.robots.items():
            if robot.player_id == self.player_id:
                team.add(loc)
            else:
                enemyTeam.add(loc)
        print('ENEMY',enemyTeam)           
        all_locs = {(x, y) for x in range(19) for y in range(19)}
        inside = {(x, y) for x in range(7,12) for y in range(7,12)}
        
        spawn = {loc for loc in all_locs if 'spawn' in rg.loc_types(loc)}
        obstacle = {loc for loc in all_locs if 'obstacle' in rg.loc_types(loc)}
        allreallocs = set(all_locs) - set(obstacle) - set(spawn) - team
        adjacent = set(rg.locs_around(self.location)) - set(obstacle)        
        adjacent_enemy = adjacent & enemyTeam
        print('ENEMY AFTER FIRST SET',enemyTeam)
      
        adjaemy2 = {loc for loc in adjacent if (set(rg.locs_around(loc)) & enemyTeam)}
        adjacent_enemy2 = set(adjaemy2) - team
        safe = adjacent - adjacent_enemy - spawn - team
        outside = set(allreallocs) - set(inside) - enemyTeam - team
        print('OUTSIDE:   ' ,outside)
        print('SAFE',safe)
        print('ENEMY AFTER FIRST SET',enemyTeam)
          
        
        goals = {(7,8),(7,9),(7,10),(7,11),(8,8),(8,9),(8,11),(9,8),(9,9),(9,10),(9,11),(10,8),(10,9),(10,10),(10,11)}
        attackEnemy = ((set(all_locs) - set(obstacle) - set(inside)) & enemyTeam)
        print('LENGTH OF ATTACK',len(attackEnemy))
        
        print('ATTACK ENEMY', attackEnemy)
        mindistance = 100
        bestloc = self.location
        print('THIS BOTS ACTUAL SPOT', self.location)
        for x in attackEnemy:
            if rg.wdist(self.location,x) < mindistance and x != self.location:
                bestloc = x
                mindistance = rg.wdist(self.location,x)
        print('THIS BOTS ACTUAL SPOT', bestloc) 
           
        if len(adjacent_enemy) > 1 and self.hp < 15:
            return ['suicide']  
        elif(len(inside & enemyTeam) > 4 and rg.wdist(self.location, rg.CENTER_POINT) < 7):
            mindistance = 100
            bestloc = self.location
            for x in (enemyTeam&inside):
                if rg.wdist(self.location,x) < mindistance and x != self.location:
                    bestloc = x
            if bestloc = self.location:
                return ['move', rg.toward(self.location, bestloc)]  
            if rg.toward(self.location,bestloc) in enemyTeam:
                return ['attack',rg.toward(self.location,bestloc)]
            else:
                mindistance = 100
                bestloc = self.location
                for x in (enemyTeam&inside):
                    if rg.wdist(self.location,x) < mindistance and x != self.location:
                        bestloc = x
                return ['move', rg.toward(self.location, bestloc)]    
        elif self.location in set(spawn):
            mindistance = 100
            bestloc = self.location
            for x in safe:
                if rg.wdist(self.location,x) < mindistance and x != self.location:
                    bestloc = x
                    mindistance = rg.wdist(self.location,x)
            return ['move', rg.toward(self.location, bestloc)]      
        
        elif (len(attackEnemy) > 0 and bestloc != self.location and rg.wdist(self.location,bestloc) < 2):
            if self.hp < 10:
                for x in safe:
                    if rg.wdist(self.location,x) < mindistance and x != self.location:
                        bestloc = x
                        mindistance = rg.wdist(self.location,x)
                if (bestloc == self.location):
                    return ['suicide']
                return ['move',rg.toward(self.location,bestloc)]
            return ['attack',bestloc]
        elif (len(attackEnemy) > 0 and bestloc != self.location and rg.wdist(self.location,bestloc) < 5):
            return ['move',rg.toward(self.location,bestloc)]
        elif rg.wdist(self.location, rg.CENTER_POINT) > 8:
            return ['move',rg.toward(self.location, rg.CENTER_POINT)]
        else:
            for x in team:
                    if rg.wdist(self.location,x) < mindistance and x != self.location:
                        bestloc = x
                        mindistance = rg.wdist(self.location,x)
            return ['move',rg.toward(self.location,bestloc)]