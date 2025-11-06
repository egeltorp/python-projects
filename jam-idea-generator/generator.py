# generator.py
# @egeltorp 2025

from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer, Button
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
import random

# Data
themes = [
	"cyberpunk", "medieval", "space", "post-apocalypse", "dream world", "underwater", "time travel"
]
mechanics = [
	"turn-based combat", "puzzle solving", "deck-building", "base building", "resource management", "stealth"
]
constraints = [
	"only two colors", "no text allowed", "made in under 3 hours", "one-button control", "must include frogs"
]

def random_theme():
	return random.choice(themes)

def random_mechanic():
	return random.choice(mechanics)

def random_constraint():
	return random.choice(constraints)


class IdeaDisplay(Static):
	idea_text = reactive("")

	def watch_idea_text(self, new_text: str):
		self.update(new_text)

class IdeaApp(App):
	CSS_PATH = "style.tcss"

	BINDINGS = [
		("1", "toggle('theme')", "Toggle Theme"),
		("2", "toggle('mechanic')", "Toggle Mechanic"),
		("3", "toggle('constraint')", "Toggle Constraint"),
		("space", "generate", "Generate New Idea"),
		("q", "quit", "Quit"),
	]

	def compose(self) -> ComposeResult:
		yield Header(show_clock=True)

		with Vertical():
			with Horizontal(id="top-bar"):
				self.generate_button = Button("Generate Idea (Space)", id="generate-button", variant="warning")
				self.theme_button = Button("Theme [1]", id="theme", classes="toggle", variant="success")
				self.mechanic_button = Button("Mechanic [2]", id="mechanic", classes="toggle", variant="success")
				self.constraint_button = Button("Constraint [3]", id="constraint", classes="toggle", variant="success")
				yield self.theme_button
				yield self.mechanic_button
				yield self.constraint_button
				yield self.generate_button

			self.idea_box = IdeaDisplay(id="idea-box")
			yield self.idea_box

		yield Footer()

	def on_mount(self):
		print("\033[?25l", end="", flush=True)
		self.set_focus(self.generate_button)
		self.generate_new_idea()

	def action_generate(self):
		self.generate_new_idea()

	def action_toggle(self, category: str):
		button = getattr(self, f"{category}_button")
		# Toggle state
		if button.variant == "success":
			button.variant = "error"
		else:
			button.variant = "success"

	def on_button_pressed(self, event: Button.Pressed):
		if event.button.id == "generate-button":
			self.generate_new_idea()
		else:
			self.action_toggle(event.button.id)

	def generate_new_idea(self):
		text = []

		if self.theme_button.variant == "success":
			text.append(f"Theme: {random_theme()}")
		if self.mechanic_button.variant == "success":
			text.append(f"Mechanic: {random_mechanic()}")
		if self.constraint_button.variant == "success":
			text.append(f"Constraint: {random_constraint()}")

		self.idea_box.idea_text = "\n".join(text) if text else "No categories selected!"


if __name__ == "__main__":
	IdeaApp().run()
