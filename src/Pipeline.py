import controllers.MenuController
import controllers.GameController
import controllers.RankingController

class Pipeline(object):

    def __init__(self):

        self.controllers = {
            'menu':     controllers.MenuController.MenuController(),
            'game':     controllers.GameController.GameController(),
            'ranking':  controllers.RankingController.RankingController(),
        }

        for controller in self.controllers.values():
            controller.set_controllers(self.controllers)

    def __call__(self, controller, action, data):
        return self.controllers[controller].__getattribute__(action)(data)