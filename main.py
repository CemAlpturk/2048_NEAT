from _2048_ import Game
import neat
import os
import numpy as np
from sklearn.preprocessing import normalize
import visualize

directions = ["Left","Right","Up","Down"]

def scale(state):
    for row in state:
        for cell in row:
            if cell != 0:
                cell = np.log2(cell)
    return state

def eval(genomes, config):
    for genome_id, genome in genomes:

        net = neat.nn.FeedForwardNetwork.create(genome, config)
        game = Game()
        score = 0
        count = 0
        while (not game.ended()) and count < 5:
            inputs = game.board.copy()
            output = net.activate(scale(inputs.reshape(-1, 1)))
            direction = directions[np.argmax(output)]
            game.move(direction)
            if game.score == score:
                count += 1
                if count > 5: break
            else:
                score = game.score
                count = 0
        genome.fitness = int(score)



def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)


    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    winner = p.run(eval, 100)

    print('\nBest genome:\n{!s}'.format(winner))

    visualize.draw_net(config, winner, True)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    run(config_path)
