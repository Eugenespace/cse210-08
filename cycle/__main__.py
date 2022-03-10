import game.shared.gamecontants as gameconstants

from game.casting.cast import Cast
from game.casting.cycle import Cycle
from game.casting.score import Score
from game.casting.actor import Actor

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.display_service import DisplayService

from game.shared.color import Color
from game.shared.point import Point

def main():

    # create the cast
    cast = Cast()
    

    """ NEEDS TO BE UPDATED """
    """
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(gameconstants.FONT_SIZE)
    banner.set_color(gameconstants.WHITE)
    banner.set_position(Point(gameconstants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    """

    position = Point(int(gameconstants.COLS / 3), int(gameconstants.ROWS / 2)) #just a facy way of positioning proportionally to the screen size
    position = position.scale(gameconstants.CELL_SIZE)
    cycle1 = Cycle(position, 1)
    cycle1.set_velocity(Point(0, 0))
    cycle1.set_color(Color(50, 125, 200))
    cast.add_actor("cycle1", cycle1)

    position = Point(1, 1) #just a facy way of positioning proportionally to the screen size
    position = position.scale(gameconstants.CELL_SIZE)
    score1 = Score()
    score1.set_position(position)
    score1.set_color(Color(50, 125, 200))
    cast.add_actor("score1", score1)
    


    position = Point(int(gameconstants.COLS / 3 * 2), int(gameconstants.ROWS / 2))
    position = position.scale(gameconstants.CELL_SIZE)
    cycle2 = Cycle(position, 3)
    cycle2.set_velocity(Point(0, 0))
    cycle2.set_color(Color(0, 0, 200))
    cast.add_actor("cycle2", cycle2)

    position = Point((gameconstants.COLS - 6), 1) #just a facy way of positioning proportionally to the screen size
    position = position.scale(gameconstants.CELL_SIZE)
    score2 = Score()
    score2.set_position(position)
    score2.set_color(Color(0, 0, 200))
    cast.add_actor("score2", score2)

    position = Point(int(gameconstants.COLS / 2), int(gameconstants.ROWS / 2))
    position = position.scale(gameconstants.CELL_SIZE)

    message = Actor()
    message.set_text("")
    message.set_position(position)
    cast.add_actor("messages", message)

    # start the game
    keyboard_service = KeyboardService()
    display_service = DisplayService(
        gameconstants.CAPTION.format(gameconstants.CENTER),
        gameconstants.MAX_X,
        gameconstants.MAX_Y,
        gameconstants.CELL_SIZE,
        gameconstants.FRAME_RATE
        )

    director = Director(keyboard_service, display_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()
