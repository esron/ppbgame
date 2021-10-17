import ppb
from ppb.events import KeyPressed, SceneStarted, StartScene
from scenes.game.scene import GameScene
from scenes.title.sprites.title_sprite import TitleSprite


class TitleScene(ppb.Scene):
    background_color = (0, 0, 0)

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(TitleSprite())

    def on_key_pressed(self, key_event: KeyPressed, signal):
        signal(StartScene(GameScene()))
