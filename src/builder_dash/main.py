from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Header, Footer, Label

from mindy.mindy_tui import MindyTUI


class BDList(Widget):
    def compose(self) -> ComposeResult:
        yield Label("Here will be content!")


# lista = BDList

class BuilderDashApp(MindyTUI):
    TITLE = 'Builder Dash'

    def compose(self) -> ComposeResult:
        yield Header()
        yield BDList()
        yield Footer()


def app() -> None:
    app = BuilderDashApp()
    
    app.run()

    # running: bool = True
    # while running is True:
    #     app.select_project()
    #     print(app.project)
    #     choice = input('Change choice y/n ')
    #     if choice.lower() == 'n':
    #         running = False


if __name__ == '__main__':
    app()
