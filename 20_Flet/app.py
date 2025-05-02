from flet import *
import random

COLORS = ("red","blue","green","black","white")

def main(page: Page):
    page.title = "GridView"
    page.bgcolor = "white"
    page.padding = 10
    page.scroll = ScrollMode.ALWAYS
    
    tabs = Tabs(
        selected_index=1,
        animation_duration=50,
        divider_color="green",
        tabs=[
            Tab(
                content=Text(
                    "$4,5000USD",
                    size=50,
                    color=Colors.PINK_400,
                    italic=True,
                    bgcolor=Colors.BLUE_300,
                    weight=FontWeight.BOLD,
                    style=TextThemeStyle.HEADLINE_LARGE,
                    font_family="Verdana",
                    selectable=True,
                    ),
                text="Check Balance",
                icon= Icon(
                    Icons.ACCOUNT_BALANCE,
                    color="blue",
                    # tooltip="ícono"
                    )
            ),
            Tab(
                content=Text(
                    "Método de pago",
                    size=25,
                    spans=[
                        TextSpan(
                            text="Extra",
                            style=TextStyle(bgcolor="green")
                        )
                    ]
                    ),
                text="Top-up Account",
                icon= Icon(Icons.BALANCE)
            ),
            Tab(
                content=Text("Texto"),
                text="Extrae dinero",
                icon= Icon(Icons.BALANCE)
            ),
        ]
    )
    page.add(tabs)
    page.update()
    
    # page.add(
    #     ResponsiveRow(
    #         controls=[
    #             Container(
    #                 Text("Column 1"),
    #                 padding=5,
    #                 bgcolor=Colors.YELLOW,
    #                 col={"sm":12,"lg":6,"xs":3}
    #             ),
    #             Container(
    #                 Text("Column 2"),
    #                 padding=5,
    #                 bgcolor=Colors.GREEN,
    #                 col=6
    #             ),
    #             Container(
    #                 Text("Column 3"),
    #                 padding=5,
    #                 bgcolor=Colors.BLUE,
    #                 col=6
    #             ),
    #             Container(
    #                 Text("Column 4"),
    #                 padding=5,
    #                 bgcolor=Colors.PINK_200,
    #                 col=6
    #             ),
    #         ]
    #     ),
    #     ResponsiveRow(
    #         controls=[
    #             TextField(label="TextField 1", col={"md":4}),
    #             TextField(label="TextField 2", col={"md":4}),
    #             TextField(label="TextField 3", col={"md":4}),
    #         ],
    #         run_spacing={"xs":10},
    #     )
    # )
    
    # grid_view = GridView(
    #     expand=1,
    #     child_aspect_ratio=1.0,
    #     max_extent=150,
    #     padding=5,
    #     spacing=20
    # )
    # for i in range(1,91):
    #     grid_view.controls.append(
    #         Container(
    #             content=Text(f"Container {i}"),
    #             padding=10,
    #             bgcolor=random.choice(COLORS)
    #         )
    #     )
    #     page.update()
    #     page.add(grid_view)
    # page.update()

app(target=main, view=AppView.FLET_APP)