from enum import Enum

class TokenType(Enum):
	
	pass # No terminals found

class Parser:
	
	# Implement class variables here...
	
	def __init__(self):
		pass # Implement
	
	def match(self, t : TokenType | str):
		pass # Implement
	
	def expect(self, t : TokenType | str):
		pass # Implement
	
	def raiseError(self):
		pass # Implement
	
	def parse(self):
		
		match = self.match
		expect = self.expect
		raiseError = self.raiseError
		
		def sentence():
			if expect("James") or expect("Cow") or expect("Pizza"):
				noun()
				verbStmt()
			else:
				raiseError()
		
		def noun():
			if expect("James"):
				match("James")
			elif expect("Cow"):
				match("Cow")
			elif expect("Pizza"):
				match("Pizza")
			else:
				raiseError()
		
		def verbStmt():
			if expect("eats") or expect("runs") or expect("codes"):
				verb()
				verbStmtEnd()
			else:
				raiseError()
		
		def verbStmtEnd():
			if expect("quickly") or expect("angrily") or expect("slowly"):
				adverb()
			else:
				pass # lambda
		
		def verb():
			if expect("eats"):
				match("eats")
			elif expect("runs"):
				match("runs")
			elif expect("codes"):
				match("codes")
			else:
				raiseError()
		
		def adverb():
			if expect("quickly"):
				match("quickly")
			elif expect("angrily"):
				match("angrily")
			elif expect("slowly"):
				match("slowly")
			else:
				raiseError()
		
		sentence()
	


