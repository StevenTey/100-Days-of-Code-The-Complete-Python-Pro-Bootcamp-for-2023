THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width = 300, height = 250, bg = "white")
        # self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="Question", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic"), 
            width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.yes_image = PhotoImage(file="quizzler-app-start/images/true.png")
        self.yes_button = Button(image=self.yes_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.yes_button.grid(column=0, row=2)
        
        self.no_image = PhotoImage(file="quizzler-app-start/images/false.png")
        self.no_button = Button(image=self.no_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.no_button.grid(column=1, row=2)
        
        self.get_nextquestion()
        
        self.window.mainloop()
    
    def get_nextquestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nextquestion)