from ipywidgets.widgets import (
    Button,
    Textarea,
    VBox,
    HBox,
    Text,
    Widget,
    RadioButtons,
    Layout,
    Output,
    FileUpload
)
from IPython.core.display import display
from IPython.core.getipython import get_ipython
from aocd.models import Puzzle
from aocd.get import current_day, most_recent_year
from .aliases import lines

class AOCWidget:
    puzzle: Puzzle

    layout: Widget
    ta: Textarea

    part_select: RadioButtons

    input_button: Button
    example_button: Button
    file_upload: FileUpload

    submit_input: Text
    submit_button: Button

    output: Output

    def __init__(self, year=None, day=None):
        if day is None:
            day = current_day()
        if year is None:
            year = most_recent_year()
        self.puzzle = Puzzle(year, day)
        
        self.ta = Textarea(
            description='Input:',
            disabled=False,
            layout=Layout(width="1200px", overflow_x="auto")
        )
        self.input_button = Button(
            description="Load input",
            disabled=False
        )
        self.input_button.on_click(self.load_input)
        self.example_button = Button(
            description="Load Example",
            disabled=False
        )
        self.example_button.on_click(self.load_example)
        self.file_upload = FileUpload(
            description="Load from File",
            disabled=False,
            multiple=False
        )
        self.file_upload.observe(self.load_file, names="value")
        self.submit_input = Text(
            placeholder="Submission"
        )
        self.submit_button = Button(
            button_style="danger",
            description="Submit",
            disabled=False
        )
        self.submit_button.on_click(self.submit)
        self.layout = VBox([
            self.ta,
            HBox([
                self.input_button,
                self.example_button,
                self.file_upload,
            ]),
            HBox([
                self.submit_input,
                self.submit_button
            ])
        ])
        self.output = Output()

    def _ipython_display_(self):
        display(self.layout)
        display(self.output)

    def __str__(self):
        return self.ta.value

    def __iter__(self):
        yield from lines(self)

    @property
    def L(self):
        return lines(self)

    def load_input(self, _):
        self.output.clear_output()
        with self.output:
            self.ta.value = self.puzzle.input_data
            self.submit_input.value = ""
            self.submit_button.disabled = False

    def load_example(self, _):
        self.output.clear_output()
        with self.output:
            example = self.puzzle.examples[0]
            self.ta.value = example.input_data
            self.submit_input.value = ""
            if example.answer_a:
                self.submit_input.value += f"A: {example.answer_a} "
            if example.answer_b:
                self.submit_input.value += f"B: {example.answer_b} "
            self.submit_button.disabled = True

    def load_file(self, change):
        fileinfo, = change.value
        self.ta.value = fileinfo.content.tobytes().decode("utf-8")
        self.submit.disabled = True

    def submit(self, _):
        self.output.clear_output()
        with self.output:
            answer = self.submit_input.value.strip()
            if not len(answer):
                answer = get_ipython().displayhook._
            if not self.puzzle.answered_a:
                print(self.puzzle._submit(answer, "a"))
            else:
                print(self.puzzle._submit(answer, "b"))

