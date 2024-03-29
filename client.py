# CLIENT
import pygame
from network import Network

# TODO: refactoring

pygame.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def read_pos(pos):
	pos = str.split(",")
	return int(pos[0]), int(pos[1])


def make_pos(tup):
	return str(tup[0]) + "," + str(tup[1])


def redraw_window(win, player, player2):
	win.fill((255, 255, 255))
	player.draw(win)
	player2.draw(win)
	pygame.display.update()


def main():
	run = True
	n = Network()
	p = n.get_p()
	clock = pygame.time.Clock()

	while run:
		clock.tick(60)
		p2 = n.send(p)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

		p.move()
		redraw_window(win, p, p2)


main()
