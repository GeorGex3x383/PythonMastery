from flet import *
from data import *
from controller import FletGPT

def main(page: Page):
    page.title = "FletGPT"
    page.bgcolor = PAGE_BG_COLOR
    page.scroll = ScrollMode.HIDDEN
    page.padding = 0
    page.update()
    
    fletgpt = FletGPT(page)
    page.add(fletgpt.build()) 
    

app(target=main, view=AppView.FLET_APP, assets_dir="assets")

    