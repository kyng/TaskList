import flet as ft

def main(page: ft.Page):
    def add_many_items(e):
        ft.context.disable_auto_update()
        for i in range(3):
            page.controls.append(ft.Text(f"Item {i}"))
        page.update()  # single update for all 100 items

    page.controls.append(ft.Button("Add items", on_click=add_many_items))

ft.run(main)