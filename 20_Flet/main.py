import flet as ft

COLORS = ("red","blue","green")
STATES_IN_USA = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
def main(page: ft.Page):
    
    def container_clicked(e):
        clicked = ft.Text("Container clicked",color=ft.Colors.BLACK)
        page.add(clicked)
    
    page.title = "Flet App"
    page.bgcolor = ft.Colors.GREY_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    text = ft.Text("Hola mundo, soy George")
    
    container_list = []
    for i in range(0,3):
        container_color = COLORS[i]
        container_list.append(
            ft.Container(
                content=ft.Text(f"Test Container{i}",color=ft.Colors.BLACK),
                bgcolor=container_color,
                padding=10
            )
        )
        
    page.controls.append(ft.Row(
        controls=container_list,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        # scroll=True
        wrap=True
        )
    )
    page.update()
    
    list_tile_column = ft.Column(
        controls=[
            ft.ListTile(
                title=ft.Text("Update location"),
                subtitle=ft.Text("Edit your current location"),
                trailing=ft.Icon(ft.Icons.EDIT_LOCATION),
                leading=ft.Icon(ft.Icons.EDIT_LOCATION_ALT_ROUNDED)
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.ALBUM),
                title=ft.Text("Texto texto texto"),
                trailing=ft.PopupMenuButton(
                    icon=ft.Icon(ft.Icons.MORE_VERT),
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(text="Item 2"),
                    ]
                )
            )
        ]
    )
    test_column = ft.Column()
    test_container = ft.Container(
        content=list_tile_column,
        padding=50,
        bgcolor = ft.Colors.GREEN,
        on_click = container_clicked
    )
    test_column.controls.append(test_container)
    
    test_container.border = ft.border.all(20,ft.Colors.PINK_200)
    test_container.border_radius = ft.border_radius.all(30)
    
    #ListView
    list_view = ft.ListView(
        height=300,
        width=300,
        scale=1.0,
        auto_scroll=False
    )
    for state in STATES_IN_USA:
        list_view.controls.append(ft.Text(state,color=ft.Colors.BLACK))
        page.update()
    
    list_view_container = ft.Container(
        content=list_view,
        bgcolor="white",
        padding=5
    )
    
    page.add(
        text,
        test_column,
        list_view_container
    )
    # page.controls.append(text)
    # page.update()
    
    # print(page.platform)

ft.app(target=main, view=ft.AppView.FLET_APP)