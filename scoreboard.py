from turtle import Turtle

FONT = ("Arial", 20, "normal")
SCORE_ALIGN = "center"


class ScoreBoard(Turtle):
	
	def __init__(self,):
		super().__init__()
		
		self.score = 0
		with open("high_score.txt") as file:
			self.high_score = int(file.read())
		self.penup()
		self.hideturtle()
		self.color("white")
		self.goto(0,270)
		self.update_scoreboard()
		

		

	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score}  High Score {self.high_score}", align = SCORE_ALIGN, font=FONT)

	# def game_over(self):
	# 	self.goto(0,0)
	# 	self.write("Game OVER", align = SCORE_ALIGN, font=FONT)
	
	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			h_score = str(self.high_score)
			with open("high_score.txt", mode = "w") as file:
				file.write(h_score)

		self.score = 0
		self.update_scoreboard()

		
	def increase_score(self):

		self.score += 1 
		self.update_scoreboard()

	
