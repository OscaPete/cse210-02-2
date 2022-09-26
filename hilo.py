# Instead of "import conductor", used "import thrower" 
from gameplay.conductor import thrower

game = thrower()  # changed to "thrower()" instead of "conductor()"
game.start()
