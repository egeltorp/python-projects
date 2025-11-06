# generator.py
# @egeltorp 2025

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Grid
from textual.reactive import reactive
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import random
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
	data = json.load(f)

themes = data["themes"]
mechanics = data["mechanics"]
constraints = data["constraints"]

def generate_idea() -> dict:
	return {
		"theme": random.choice(themes),
		"mechanic": random.choice(mechanics),
		"constraint": random.choice(constraints),
	}

class IdeaBox(Static):
	category: str
	color: str
	text = reactive("")

	def __init__(self, category: str, color: str):
		super().__init__()
		self.category = category
		self.color = color

	def watch_text(self, text: str):
		content = Align.center(Text(text, style=f"bold {self.color}"), vertical="middle")
		panel = Panel(
			content,
			title=f"[b]{self.category}[/b]",
			border_style=self.color,
			padding=(1, 2),
			expand=True,
		)
		self.update(panel)

class IdeaApp(App):
	CSS_PATH = "style.tcss"

	BINDINGS = [
		("space", "generate", "Generate Idea"),
		("q", "quit", "Quit"),
	]

	def compose(self) -> ComposeResult:
		yield Header(show_clock=True)

		with Grid(id="idea-grid"):
			self.theme_box = IdeaBox("Theme", "cyan")
			self.mechanic_box = IdeaBox("Mechanic", "green")
			self.constraint_box = IdeaBox("Constraint", "magenta")

			yield self.theme_box
			yield self.mechanic_box
			yield self.constraint_box

		yield Footer()

	def on_mount(self):
		self.theme = "textual-dark"
		self.action_generate()

	def action_generate(self):
		new_idea = generate_idea()
		self.theme_box.text = new_idea["theme"]
		self.mechanic_box.text = new_idea["mechanic"]
		self.constraint_box.text = new_idea["constraint"]


if __name__ == "__main__":
	IdeaApp().run()
