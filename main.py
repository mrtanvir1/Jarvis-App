from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import requests


GEMINI_API_KEY = "AQ.Ab8RN6JrEZ7nxQrP9PQLCDrlXaeEbAbmtDFszj-fssJEULreWg"


class JarvisApp(App):

  def build(self):
    self.layout = BoxLayout(
        orientation="vertical", padding=20, spacing=10
    )

    # শিরোনাম
    self.title_label = Label(
        text="[b]JARVIS AI ASSISTANT[/b]",
        markup=True,
        font_size="20sp",
        size_hint=(1, 0.1),
    )

    # উত্তর দেখানোর বক্স
    self.status_label = Label(
        text="আমি আপনাকে কীভাবে সাহায্য করতে পারি?",
        font_size="15sp",
        size_hint=(1, 0.65),
        text_size=(300, None),
        halign="center",
        valign="middle",
    )

    # ইনপুট লেখার বক্স
    self.user_input = TextInput(
        hint_text="এখানে টাইপ করুন...", multiline=False, size_hint=(1, 0.12)
    )

    # পাঠান বাটন
    self.send_btn = Button(
        text="Ask Jarvis",
        size_hint=(1, 0.13),
        background_color=(0.1, 0.5, 0.9, 1),
    )
    self.send_btn.bind(on_press=self.process_command)

    self.layout.add_widget(self.title_label)
    self.layout.add_widget(self.status_label)
    self.layout.add_widget(self.user_input)
    self.layout.add_widget(self.send_btn)

    return self.layout

  def process_command(self, instance):
    user_text = self.user_input.text.strip()
    if not user_text:
      return

    self.status_label.text = "চিন্তা করছি..."
    self.user_input.text = ""

    # Gemini API তে রিকোয়েস্ট পাঠানো
    try:
      url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
      headers = {"Content-Type": "application/json"}
      payload = {"contents": [{"parts": [{"text": user_text}]}]}

      response = requests.post(url, json=payload, headers=headers, timeout=10)
      if response.status_code == 200:
        result = response.json()
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        self.status_label.text = reply
      else:
        self.status_label.text = "API এর সাথে কানেক্ট হতে সমস্যা হয়েছে।"
    except Exception as e:
      self.status_label.text = f"ত্রুটি: {str(e)}"


if __name__ == "__main__":
  JarvisApp().run()
