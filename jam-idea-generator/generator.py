# generator.py
# @egeltorp 2025

# --- TEXTUAL ---
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Grid
from textual.reactive import reactive
from textual.theme import Theme

# --- RICH ---
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

# --- STANDARD ---
import random
import json
from pathlib import Path

# --- THEME ---
egeltorp_theme = Theme(
    name="egeltorp",
    primary="#000000",
    secondary="#000000",
    accent="#000000",
    foreground="#000000",
    background="#000000",
    success="#000000",
    warning="#000000",
    error="#000000",
    surface="#000000",
    panel="#000000",
    dark=True,
    variables={
        "block-cursor-text-style": "none",
        "footer-key-foreground": "#000000",
        "input-selection-background": "#000000",
    },
)

# --- JSON FILE HANDLING ---
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
	data = json.load(f)

themes = data["themes"]
mechanics = data["mechanics"]
constraints = data["constraints"]
goal = data["goals"]
setting = data["settings"]
twist = data["twists"]

# --- GENERATE FUNC ---
def generate_idea() -> dict:
	return {
		"theme": random.choice(themes),
		"mechanic": random.choice(mechanics),
		"constraint": random.choice(constraints),
		"goal": random.choice(goal),
		"setting": random.choice(setting),
		"twist": random.choice(twist),
	}

# --- IdeaBox WIDGET ---
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

# --- MAIN CLASS for APP ---
class Generator(App):
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
			self.constraint_box = IdeaBox("Constraint", "yellow")
			self.goal_box = IdeaBox("Goal", "magenta")
			self.setting_box = IdeaBox("Setting", "blue")
			self.twist_box = IdeaBox("Twist", "red")

			yield self.theme_box
			yield self.mechanic_box
			yield self.constraint_box
			yield self.goal_box
			yield self.setting_box
			yield self.twist_box

		yield Footer()

	def on_mount(self):
		self.register_theme(egeltorp_theme)
		self.theme = "egeltorp"
		self.title = ""
		self.action_generate()

	def action_generate(self):
		new_idea = generate_idea()
		self.theme_box.text = new_idea["theme"]
		self.mechanic_box.text = new_idea["mechanic"]
		self.constraint_box.text = new_idea["constraint"]
		self.goal_box.text = new_idea["goal"]
		self.setting_box.text = new_idea["setting"]
		self.twist_box.text = new_idea["twist"]

# --- RUN ---
if __name__ == "__main__":
	Generator().run()
