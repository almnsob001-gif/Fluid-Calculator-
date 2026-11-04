from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivy.utils import platform
from kivymd.app import MDApp
import webbrowser

KV = '''
MDNavigationLayout:
    MDScreenManager:

        MDScreen:
            md_bg_color: app.theme_cls.bg_light

            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_color[0], app.theme_cls.primary_color[1], app.theme_cls.primary_color[2], 0.07
                Rectangle:
                    pos: self.pos
                    size: self.size

            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "IV Drip Rate Calculator"
                    elevation: 0
                    left_action_items: [["menu", lambda x: app.root.ids.nav_drawer.set_state("open")]]
                    right_action_items: [["theme-light-dark", lambda x: app.toggle_theme()]]

                ScrollView:
                    do_scroll_x: False

                    MDBoxLayout:
                        orientation: "vertical"
                        padding: dp(16)
                        spacing: dp(16)
                        size_hint_y: None
                        height: self.minimum_height

                        MDBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: dp(115)
                            spacing: dp(2)

                            MDIcon:
                                icon: "water-percent"
                                font_size: dp(55)
                                halign: "center"
                                theme_text_color: "Custom"
                                text_color: app.theme_cls.primary_color

                            MDLabel:
                                text: "Drip Rate Calculator"
                                halign: "center"
                                font_style: "H5"
                                theme_text_color: "Primary"
                                bold: True

                            MDLabel:
                                text: "Precise gtt/min calculation for clinical use"
                                halign: "center"
                                font_style: "Caption"
                                theme_text_color: "Secondary"

                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: dp(450)
                            padding: dp(18)
                            spacing: dp(14)
                            elevation: 6
                            radius: [22,]

                            MDLabel:
                                text: "Solution Data"
                                font_style: "Subtitle1"
                                theme_text_color: "Primary"
                                bold: True
                                size_hint_y: None
                                height: dp(28)

                            MDTextField:
                                id: volume_input
                                hint_text: "Volume (mL)"
                                input_filter: "float"
                                mode: "rectangle"
                                icon_left: "water-outline"
                                size_hint_x: 1

                            MDTextField:
                                id: time_input
                                hint_text: "Time"
                                input_filter: "float"
                                mode: "rectangle"
                                icon_left: "clock-outline"
                                size_hint_x: 1

                            MDBoxLayout:
                                size_hint_y: None
                                height: dp(45)
                                spacing: dp(8)

                                MDFlatButton:
                                    text: "MINUTES"
                                    theme_text_color: "Custom"
                                    text_color: [1,1,1,1] if app.time_unit == "minutes" else app.theme_cls.primary_color
                                    md_bg_color: app.theme_cls.primary_color if app.time_unit == "minutes" else app.theme_cls.bg_dark
                                    size_hint_x: 0.5
                                    on_release: app.set_time_unit("minutes")

                                MDFlatButton:
                                    text: "HOURS"
                                    theme_text_color: "Custom"
                                    text_color: [1,1,1,1] if app.time_unit == "hours" else app.theme_cls.primary_color
                                    md_bg_color: app.theme_cls.primary_color if app.time_unit == "hours" else app.theme_cls.bg_dark
                                    size_hint_x: 0.5
                                    on_release: app.set_time_unit("hours")

                            MDLabel:
                                text: "Drop Factor (gtt/mL)"
                                font_style: "Caption"
                                theme_text_color: "Secondary"
                                size_hint_y: None
                                height: dp(20)

                            MDBoxLayout:
                                size_hint_y: None
                                height: dp(55)
                                spacing: dp(8)

                                MDFlatButton:
                                    text: "20"
                                    font_size: dp(20)
                                    theme_text_color: "Custom"
                                    text_color: [1,1,1,1] if app.drop_factor == 20 else app.theme_cls.primary_color
                                    md_bg_color: app.theme_cls.primary_color if app.drop_factor == 20 else app.theme_cls.bg_dark
                                    size_hint_x: 0.33
                                    on_release: app.set_drop_factor(20)

                                MDFlatButton:
                                    text: "15"
                                    font_size: dp(20)
                                    theme_text_color: "Custom"
                                    text_color: [1,1,1,1] if app.drop_factor == 15 else app.theme_cls.primary_color
                                    md_bg_color: app.theme_cls.primary_color if app.drop_factor == 15 else app.theme_cls.bg_dark
                                    size_hint_x: 0.33
                                    on_release: app.set_drop_factor(15)

                                MDFlatButton:
                                    text: "10"
                                    font_size: dp(20)
                                    theme_text_color: "Custom"
                                    text_color: [1,1,1,1] if app.drop_factor == 10 else app.theme_cls.primary_color
                                    md_bg_color: app.theme_cls.primary_color if app.drop_factor == 10 else app.theme_cls.bg_dark
                                    size_hint_x: 0.33
                                    on_release: app.set_drop_factor(10)

                        MDRaisedButton:
                            text: "CALCULATE DROPS"
                            size_hint_x: 1
                            size_hint_y: None
                            height: dp(55)
                            md_bg_color: app.theme_cls.primary_color
                            font_size: dp(16)
                            on_release: app.calculate_drops()

                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: dp(200)
                            padding: dp(20)
                            spacing: dp(4)
                            elevation: 8
                            radius: [22,]
                            md_bg_color: app.theme_cls.primary_color

                            MDIcon:
                                icon: "water"
                                font_size: dp(45)
                                halign: "center"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 0.9
                                size_hint_y: None
                                height: dp(50)

                            MDLabel:
                                id: result_label
                                text: "-- gtt/min"
                                halign: "center"
                                font_style: "H3"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                bold: True

                            MDLabel:
                                id: detail_label
                                text: "Enter values to calculate"
                                halign: "center"
                                font_style: "Caption"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 0.85

                        MDLabel:
                            text: "Formula: (Volume x Drop Factor) / Time"
                            halign: "center"
                            font_style: "Caption"
                            theme_text_color: "Hint"
                            size_hint_y: None
                            height: dp(25)

    MDNavigationDrawer:
        id: nav_drawer
        radius: [0, 16, 16, 0]

        MDBoxLayout:
            orientation: "vertical"
            padding: dp(15)
            spacing: dp(10)

            MDBoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: dp(140)
                spacing: dp(4)

                MDIcon:
                    icon: "water-percent"
                    font_size: dp(50)
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color

                MDLabel:
                    text: "IV Drip Calculator"
                    halign: "center"
                    font_style: "H6"
                    bold: True
                    theme_text_color: "Primary"

                MDLabel:
                    text: "Clinical tool for nurses"
                    halign: "center"
                    font_style: "Caption"
                    theme_text_color: "Secondary"

            MDBoxLayout:
                size_hint_y: None
                height: dp(1)
                canvas.before:
                    Color:
                        rgba: app.theme_cls.divider_color
                    Rectangle:
                        pos: self.pos
                        size: self.size

            OneLineIconListItem:
                text: "Contact Us on WhatsApp"
                on_release: app.contact_whatsapp()

                IconLeftWidget:
                    icon: "whatsapp"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color

            Widget:
'''


class MedicalDropsApp(MDApp):
    time_unit = StringProperty("minutes")
    drop_factor = NumericProperty(20)

    def build(self):
        self.title = "IV Drip Rate Calculator"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        # ✅ فرض الوضع العمودي على أندرويد
        if platform == "android":
            try:
                from android import mActivity
                # 1 = SCREEN_ORIENTATION_PORTRAIT
                mActivity.setRequestedOrientation(1)
            except Exception as e:
                print(f"Orientation lock failed: {e}")

    def toggle_theme(self):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def set_drop_factor(self, value):
        self.drop_factor = int(value)

    def set_time_unit(self, unit):
        self.time_unit = unit

    def contact_whatsapp(self):
        self.root.ids.nav_drawer.set_state("close")
        webbrowser.open("https://wa.me/967774602007")

    def calculate_drops(self):
        volume_text = self.root.ids.volume_input.text
        time_text = self.root.ids.time_input.text

        if not volume_text or not time_text:
            self.root.ids.result_label.text = "Missing input"
            self.root.ids.detail_label.text = "Please enter volume and time"
            return

        try:
            volume = float(volume_text)
            time_value = float(time_text)
        except ValueError:
            self.root.ids.result_label.text = "Invalid values"
            self.root.ids.detail_label.text = "Please enter valid numbers"
            return

        if time_value <= 0:
            self.root.ids.result_label.text = "Invalid time"
            self.root.ids.detail_label.text = "Time must be greater than zero"
            return

        if volume <= 0:
            self.root.ids.result_label.text = "Invalid volume"
            self.root.ids.detail_label.text = "Volume must be greater than zero"
            return

        time_min = time_value * 60 if self.time_unit == "hours" else time_value
        drops_per_min = (volume * self.drop_factor) / time_min
        rounded_drops = round(drops_per_min)

        self.root.ids.result_label.text = f"{rounded_drops} gtt/min"
        self.root.ids.detail_label.text = (
            f"({volume} mL x {self.drop_factor} gtt/mL) / {time_min:.1f} min\n"
            f"Exact: {drops_per_min:.2f} gtt/min"
        )


if __name__ == "__main__":
    MedicalDropsApp().run()
