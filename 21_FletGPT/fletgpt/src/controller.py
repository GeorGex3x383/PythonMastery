from flet import *
from data import DEFAULT_PROMPTS, CHATGPT_IMAGE_URL, MY_IMAGE_PATH, cohere_response

class FletGPT:
    def __init__(self, page):
        self.page = page
        self.appname = self.page.title
        self.prompts = []
        super().__init__()

    def new_chat(self, event):
        chat2 = Row(
            controls=[
                Icon(Icons.CHAT_BUBBLE_OUTLINE_ROUNDED, color=Colors.WHITE),
                Text("New Chat", color=Colors.WHITE)
            ]
        )
        chat = Text("New Chat", color=Colors.WHITE)
        self.chat_history.controls.insert(0, chat2)
        self.top_row.update()
        
    def prompt_hover(self,event):
        # Data property --> True as a str
        # Data property --> False as a str
        event.control.bgcolor = Colors.ON_SURFACE_VARIANT if event.data == 'true' else Colors.WHITE
        event.control.content.controls[-1].visible = True if event.data == 'true' else False
        self.top_row.update()
        
    def close_sidebar(self,e):
        self.left_navbar.visible = False
        self.text_interface.col = {"lg":12}
        self.applogo.margin= margin.only(bottom=250,top=50, left=450)
        self.responsive_prompt.alignment = MainAxisAlignment.CENTER
        self.sidebar.visible = True
        self.top_row.update()
        
    def open_sidebar(self,e):
        self.left_navbar.visible = True
        self.text_interface.col = {"lg":10}
        self.applogo.margin= margin.only(bottom=250,top=50, left=350)
        self.sidebar.visible = False
        self.top_row.update()
        
    def send_message(self,e):
        pass
    
    def input_focus(self,e):
        self.send_message_btn.icon_color = Colors.GREEN_400 if self.input.value != "" else Colors.GREY_400
        self.top_row.update()
        
    def submit(self, e):
        self.applogo.visible = False
        self.responsive_prompt.visible = False
        self.conversations.visible = True

        try:
            # Extrae el valor del texto del prompt (primer control del Row)
            prompt_value = f"{e.control.content.controls[0].value} {e.control.content.controls[0].spans[0].text[1:]}"
        except Exception as ex:
            # Si no es un prompt, usa lo que escribió el usuario
            prompt_value = self.input.value

        self.input.value = ""
        progress_ring = ProgressBar(color=Colors.GREY_400, bgcolor=Colors.WHITE)
        prompt_text = Text(value=prompt_value, color=Colors.BLACK, size=15)
        self.top_row.update()
        
        query = Container(
            alignment=alignment.top_left,
            padding=padding.symmetric(horizontal=50, vertical=10),
            content=Row(
                wrap=True,
                controls=[
                    Image(src=MY_IMAGE_PATH, height=25, width=25),
                    prompt_text
                ]
            )
        )
        
        self.conversations.controls.extend([query,progress_ring])
        self.top_row.update()

        cohere_api_response = cohere_response(prompt_text.value)
        self.conversations.controls.pop()
        
        response = Container(
            alignment=alignment.top_left,
            bgcolor=Colors.ON_SURFACE_VARIANT,
            padding=padding.symmetric(horizontal=50, vertical=10),
            content=Row(
                wrap=True,
                controls=[
                    Image(src=CHATGPT_IMAGE_URL, height=25, width=25),
                    Text(value=cohere_api_response, color=Colors.BLACK, size=15)
                ]
            )
        )
        self.conversations.controls.append(response)
        self.top_row.update()

    
    def build(self):
        self.action_buttons = Row(
            controls=[
                Container(
                    padding = padding.only(left=5, top=5, bottom=5, right=10),
                    border = border.all(1,Colors.GREY_400),
                    border_radius = 10,
                    content = TextButton(
                        text="New chat",
                        icon=Icons.ADD,
                        icon_color=Colors.WHITE,
                        style=ButtonStyle(
                            color=Colors.WHITE,
                        ),
                        on_click = self.new_chat
                    ) 
                ),
                Container(
                    padding = padding.symmetric(vertical=1),
                    border = border.all(1,Colors.GREY_400),
                    border_radius = 10,
                    content = IconButton(
                        on_click = self.close_sidebar,
                        icon=Icons.VIEW_SIDEBAR_OUTLINED,
                        icon_color=Colors.WHITE,
                        style=ButtonStyle(
                            color=Colors.WHITE
                        ),
                        tooltip="Close sidebar"
                    ) 
                )
            ]
        )
        self.chat_history = ListView(width=250,
                                    height=450,
                                    expand=True,
                                    spacing= 20,
                            )
        self.bottom_sheet = Column(
            controls=[
                Divider(thickness=1,height=1,color=Colors.GREY_500),
                Row(
                    controls=[
                        Icon(Icons.PERSON, color=Colors.WHITE),
                        Text("Upgrade to Plus",size=15,weight=FontWeight.W_300,color=Colors.WHITE)
                    ]
                ),
                Row(
                    controls=[
                        Image(
                            src=MY_IMAGE_PATH,
                            width=25,
                            height=25,
                        ),
                        Text("George García",size=15,weight=FontWeight.W_300,color=Colors.WHITE),
                        IconButton(icon=Icons.MORE_VERT, icon_color=Colors.WHITE)
                    ]
                )
            ]
        )
        self.applogo = Container(
            margin= margin.only(bottom=250,top=50, left=350),
            content= Text(
                "FletGPT",
                color=Colors.GREY_400,
                weight=FontWeight.BOLD,
                size=40,
            )
        )
        #For loop to create prompot buttons on text interface
        for button in DEFAULT_PROMPTS:
            prompt = Container(
                alignment=alignment.top_left,
                padding=5,
                border=border.all(1,color=Colors.GREY_500),
                border_radius=10,
                height=50,
                width=120,
                col={"lg":6},
                on_click=self.submit,
                on_hover= self.prompt_hover,
                content= Row(
                    alignment=MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        Text(
                            value=button[0],
                            weight=FontWeight.BOLD,
                            theme_style=TextThemeStyle.BODY_MEDIUM,
                            color=Colors.BLACK,
                            spans=[
                                TextSpan(
                                    text=button[1],
                                    style=TextStyle(
                                        size=12,
                                        weight=FontWeight.NORMAL,
                                    )
                                )
                            ]
                        ),    
                        Container(width=180),
                        Icon(Icons.SEND_ROUNDED,color=Colors.BLACK,visible=False),
                    ]
                )
            )
            self.prompts.append(prompt)
            
        self.responsive_prompt = ResponsiveRow(
            controls=self.prompts
        )
        self.sidebar = Container(
                    visible=False,
                    content = IconButton(
                        on_click = self.open_sidebar,
                        icon=Icons.VIEW_SIDEBAR_OUTLINED,
                        icon_color=Colors.GREY_500,
                        style=ButtonStyle(
                            color=Colors.GREY_500
                        ),
                        tooltip="Open sidebar"
                    )
                )
        self.input = TextField(
            hint_text="Send a message",
            border=InputBorder.NONE,
            cursor_color= Colors.BLACK,
            color=Colors.BLACK,
            cursor_height=25,
            cursor_width=1,
            shift_enter=True,
            multiline=True,
            on_change= self.input_focus,
            on_submit=self.submit
        )
        self.send_message_btn = IconButton(
            icon=Icons.SEND,
            icon_color=Colors.GREY_400,
            tooltip="Send message",
            on_click= self.send_message
        )
        self.send_stack = Stack(
            controls=[
                Container(
                    height=55,
                    margin = margin.only(top=5, right=5),
                    padding=padding.symmetric(horizontal=15, vertical=3),
                    bgcolor = Colors.WHITE,
                    border_radius=10,
                    content=self.input,
                    shadow=BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        offset=Offset(0,0),
                        color=Colors.with_opacity(0.4,color=Colors.BLACK)
                    )
                ),
                Container(
                    bgcolor=Colors.WHITE,
                    content=self.send_message_btn,
                    margin=margin.only(left=800, top=10, right=5),
                    height=23,
                    width=23,
                    padding=2,
                )
            ]
        )
        
        self.conversations = ListView(
            width=1000,
            height=600,
            expand=True,
            visible=False,
            spacing=20,
            auto_scroll=True
        )
        
        
        self.left_navbar = Container(
            bgcolor=Colors.GREY_900,
            padding=15,
            width=470,
            height=620,
            col={"lg": 2},
            content=Column(
                expand=True,
                alignment=MainAxisAlignment.START,
                controls=[
                    self.action_buttons,
                    self.chat_history,
                    self.bottom_sheet
                ]
            )
        )
        self.text_interface = Container(
            height= 620,
            width= 1000,
            col= {"lg":10},
            padding=padding.symmetric(vertical=30, horizontal=100),
            bgcolor=Colors.WHITE,
            content=Container(
                content=Column(
                    controls=[
                        self.sidebar,
                        self.applogo,
                        self.responsive_prompt,
                        self.conversations,
                        self.send_stack,
                    ]
                )
            )
        )
        self.top_row = ResponsiveRow(
            alignment=MainAxisAlignment.START,
            controls=[
                self.left_navbar,
                self.text_interface,
                ]
        )

        # Retornar el control completo
        return Column(controls=[self.top_row])
