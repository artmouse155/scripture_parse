from enum import Enum

class TokenType(Enum):
	
	SEMICOLON = "SEMICOLON"
	COMMA = "COMMA"
	AMPERSAND = "AMPERSAND"
	COLON = "COLON"
	DASH = "DASH"
	UNDEFINED = "UNDEFINED"
	PERIOD = "PERIOD"
	END = "END"
	NUMBER = "NUMBER"

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
		
		def file():
			if expect("1") or expect("2") or expect("3") or expect("4") or expect("JS") or expect("Joseph") or expect("Abraham") or expect("Acts") or expect("Alma") or expect("Amos") or expect("Colossians") or expect("Daniel") or expect("Deuteronomy") or expect("Ecclesiastes") or expect("Enos") or expect("Ephesians") or expect("Esther") or expect("Ether") or expect("Exodus") or expect("Ezekiel") or expect("Ezra") or expect("Galatians") or expect("Genesis") or expect("Habakkuk") or expect("Haggai") or expect("Hebrews") or expect("Helaman") or expect("Hosea") or expect("Isaiah") or expect("Jacob") or expect("James") or expect("Jarom") or expect("Jeremiah") or expect("Job") or expect("Joel") or expect("John") or expect("Jonah") or expect("Joshua") or expect("Jude") or expect("Judges") or expect("Lamentations") or expect("Leviticus") or expect("Luke") or expect("Malachi") or expect("Mark") or expect("Matthew") or expect("Micah") or expect("Mormon") or expect("Moroni") or expect("Moses") or expect("Mosiah") or expect("Nahum") or expect("Nehemiah") or expect("Numbers") or expect("Obadiah") or expect("OD") or expect("Omni") or expect("Philemon") or expect("Philippians") or expect("Proverbs") or expect("Psalms") or expect("Revelation") or expect("Romans") or expect("Ruth") or expect("Song") or expect("Titus") or expect("Zechariah") or expect("Zephaniah") or expect("Abr") or expect("Col") or expect("Dan") or expect("Deut") or expect("Eccl") or expect("Eph") or expect("Esth") or expect("Ex") or expect("Ezek") or expect("Gal") or expect("Gen") or expect("Hab") or expect("Hag") or expect("Heb") or expect("Hel") or expect("Isa") or expect("Jer") or expect("Josh") or expect("Judg") or expect("Lam") or expect("Lev") or expect("Mal") or expect("Matt") or expect("Morm") or expect("Moro") or expect("Neh") or expect("Num") or expect("Obad") or expect("Philem") or expect("Philip") or expect("Prov") or expect("Ps") or expect("Rev") or expect("Rom") or expect("Zech") or expect("Zeph") or expect("Articles") or expect("A") or expect("Doctrine") or expect("Official") or expect("Song") or expect("Words") or expect("W") or expect("D") or expect(TokenType.AMPERSAND) or expect(TokenType.SEMICOLON) or expect(TokenType.DASH) or expect(TokenType.END) or expect(TokenType.NUMBER) or expect(TokenType.PERIOD) or expect(TokenType.COLON) or expect(TokenType.COMMA) or expect(TokenType.UNDEFINED):
				fileItemList()
				match(TokenType.END)
			else:
				raiseError()
		
		def fileItem():
			if expect("1") or expect("2") or expect("3") or expect("4") or expect("JS") or expect("Joseph") or expect("Abraham") or expect("Acts") or expect("Alma") or expect("Amos") or expect("Colossians") or expect("Daniel") or expect("Deuteronomy") or expect("Ecclesiastes") or expect("Enos") or expect("Ephesians") or expect("Esther") or expect("Ether") or expect("Exodus") or expect("Ezekiel") or expect("Ezra") or expect("Galatians") or expect("Genesis") or expect("Habakkuk") or expect("Haggai") or expect("Hebrews") or expect("Helaman") or expect("Hosea") or expect("Isaiah") or expect("Jacob") or expect("James") or expect("Jarom") or expect("Jeremiah") or expect("Job") or expect("Joel") or expect("John") or expect("Jonah") or expect("Joshua") or expect("Jude") or expect("Judges") or expect("Lamentations") or expect("Leviticus") or expect("Luke") or expect("Malachi") or expect("Mark") or expect("Matthew") or expect("Micah") or expect("Mormon") or expect("Moroni") or expect("Moses") or expect("Mosiah") or expect("Nahum") or expect("Nehemiah") or expect("Numbers") or expect("Obadiah") or expect("OD") or expect("Omni") or expect("Philemon") or expect("Philippians") or expect("Proverbs") or expect("Psalms") or expect("Revelation") or expect("Romans") or expect("Ruth") or expect("Song") or expect("Titus") or expect("Zechariah") or expect("Zephaniah") or expect("Abr") or expect("Col") or expect("Dan") or expect("Deut") or expect("Eccl") or expect("Eph") or expect("Esth") or expect("Ex") or expect("Ezek") or expect("Gal") or expect("Gen") or expect("Hab") or expect("Hag") or expect("Heb") or expect("Hel") or expect("Isa") or expect("Jer") or expect("Josh") or expect("Judg") or expect("Lam") or expect("Lev") or expect("Mal") or expect("Matt") or expect("Morm") or expect("Moro") or expect("Neh") or expect("Num") or expect("Obad") or expect("Philem") or expect("Philip") or expect("Prov") or expect("Ps") or expect("Rev") or expect("Rom") or expect("Zech") or expect("Zeph") or expect("Articles") or expect("A") or expect("Doctrine") or expect("Official") or expect("Song") or expect("Words") or expect("W") or expect("D"):
				scriptureRef()
			elif expect(TokenType.AMPERSAND):
				match(TokenType.AMPERSAND)
			elif expect(TokenType.SEMICOLON):
				match(TokenType.SEMICOLON)
			elif expect(TokenType.DASH):
				match(TokenType.DASH)
			elif expect(TokenType.END):
				match(TokenType.END)
			elif expect(TokenType.NUMBER):
				match(TokenType.NUMBER)
			elif expect(TokenType.PERIOD):
				match(TokenType.PERIOD)
			elif expect(TokenType.COLON):
				match(TokenType.COLON)
			elif expect(TokenType.COMMA):
				match(TokenType.COMMA)
			elif expect(TokenType.UNDEFINED):
				match(TokenType.UNDEFINED)
			else:
				raiseError()
		
		def fileItemList():
			if expect("1") or expect("2") or expect("3") or expect("4") or expect("JS") or expect("Joseph") or expect("Abraham") or expect("Acts") or expect("Alma") or expect("Amos") or expect("Colossians") or expect("Daniel") or expect("Deuteronomy") or expect("Ecclesiastes") or expect("Enos") or expect("Ephesians") or expect("Esther") or expect("Ether") or expect("Exodus") or expect("Ezekiel") or expect("Ezra") or expect("Galatians") or expect("Genesis") or expect("Habakkuk") or expect("Haggai") or expect("Hebrews") or expect("Helaman") or expect("Hosea") or expect("Isaiah") or expect("Jacob") or expect("James") or expect("Jarom") or expect("Jeremiah") or expect("Job") or expect("Joel") or expect("John") or expect("Jonah") or expect("Joshua") or expect("Jude") or expect("Judges") or expect("Lamentations") or expect("Leviticus") or expect("Luke") or expect("Malachi") or expect("Mark") or expect("Matthew") or expect("Micah") or expect("Mormon") or expect("Moroni") or expect("Moses") or expect("Mosiah") or expect("Nahum") or expect("Nehemiah") or expect("Numbers") or expect("Obadiah") or expect("OD") or expect("Omni") or expect("Philemon") or expect("Philippians") or expect("Proverbs") or expect("Psalms") or expect("Revelation") or expect("Romans") or expect("Ruth") or expect("Song") or expect("Titus") or expect("Zechariah") or expect("Zephaniah") or expect("Abr") or expect("Col") or expect("Dan") or expect("Deut") or expect("Eccl") or expect("Eph") or expect("Esth") or expect("Ex") or expect("Ezek") or expect("Gal") or expect("Gen") or expect("Hab") or expect("Hag") or expect("Heb") or expect("Hel") or expect("Isa") or expect("Jer") or expect("Josh") or expect("Judg") or expect("Lam") or expect("Lev") or expect("Mal") or expect("Matt") or expect("Morm") or expect("Moro") or expect("Neh") or expect("Num") or expect("Obad") or expect("Philem") or expect("Philip") or expect("Prov") or expect("Ps") or expect("Rev") or expect("Rom") or expect("Zech") or expect("Zeph") or expect("Articles") or expect("A") or expect("Doctrine") or expect("Official") or expect("Song") or expect("Words") or expect("W") or expect("D") or expect(TokenType.AMPERSAND) or expect(TokenType.SEMICOLON) or expect(TokenType.DASH) or expect(TokenType.END) or expect(TokenType.NUMBER) or expect(TokenType.PERIOD) or expect(TokenType.COLON) or expect(TokenType.COMMA) or expect(TokenType.UNDEFINED):
				fileItem()
				fileItemList()
			else:
				pass # lambda
		
		def scriptureRef():
			if expect("1") or expect("2") or expect("3") or expect("4") or expect("JS") or expect("Joseph") or expect("Abraham") or expect("Acts") or expect("Alma") or expect("Amos") or expect("Colossians") or expect("Daniel") or expect("Deuteronomy") or expect("Ecclesiastes") or expect("Enos") or expect("Ephesians") or expect("Esther") or expect("Ether") or expect("Exodus") or expect("Ezekiel") or expect("Ezra") or expect("Galatians") or expect("Genesis") or expect("Habakkuk") or expect("Haggai") or expect("Hebrews") or expect("Helaman") or expect("Hosea") or expect("Isaiah") or expect("Jacob") or expect("James") or expect("Jarom") or expect("Jeremiah") or expect("Job") or expect("Joel") or expect("John") or expect("Jonah") or expect("Joshua") or expect("Jude") or expect("Judges") or expect("Lamentations") or expect("Leviticus") or expect("Luke") or expect("Malachi") or expect("Mark") or expect("Matthew") or expect("Micah") or expect("Mormon") or expect("Moroni") or expect("Moses") or expect("Mosiah") or expect("Nahum") or expect("Nehemiah") or expect("Numbers") or expect("Obadiah") or expect("OD") or expect("Omni") or expect("Philemon") or expect("Philippians") or expect("Proverbs") or expect("Psalms") or expect("Revelation") or expect("Romans") or expect("Ruth") or expect("Song") or expect("Titus") or expect("Zechariah") or expect("Zephaniah") or expect("Abr") or expect("Col") or expect("Dan") or expect("Deut") or expect("Eccl") or expect("Eph") or expect("Esth") or expect("Ex") or expect("Ezek") or expect("Gal") or expect("Gen") or expect("Hab") or expect("Hag") or expect("Heb") or expect("Hel") or expect("Isa") or expect("Jer") or expect("Josh") or expect("Judg") or expect("Lam") or expect("Lev") or expect("Mal") or expect("Matt") or expect("Morm") or expect("Moro") or expect("Neh") or expect("Num") or expect("Obad") or expect("Philem") or expect("Philip") or expect("Prov") or expect("Ps") or expect("Rev") or expect("Rom") or expect("Zech") or expect("Zeph") or expect("Articles") or expect("A") or expect("Doctrine") or expect("Official") or expect("Song") or expect("Words") or expect("W") or expect("D"):
				book()
				chapterRef()
				chapterRefList()
			else:
				raiseError()
		
		def chapterRef():
			if expect(TokenType.NUMBER):
				match(TokenType.NUMBER)
				chapterEnd()
			else:
				raiseError()
		
		def chapterEnd():
			if expect(TokenType.COLON):
				chapterVerseEnd()
			elif expect(TokenType.DASH):
				chapterRangeEnd()
			else:
				pass # lambda
		
		def chapterVerseEnd():
			if expect(TokenType.COLON):
				match(TokenType.COLON)
				verseRef()
				verseRefList()
			else:
				raiseError()
		
		def chapterRangeEnd():
			if expect(TokenType.DASH):
				match(TokenType.DASH)
				match(TokenType.NUMBER)
			else:
				raiseError()
		
		def verseRef():
			if expect(TokenType.NUMBER):
				match(TokenType.NUMBER)
				verseEnd()
			else:
				raiseError()
		
		def verseEnd():
			if expect(TokenType.DASH):
				verseRangeEnd()
			else:
				pass # lambda
		
		def verseRangeEnd():
			if expect(TokenType.DASH):
				match(TokenType.DASH)
				match(TokenType.NUMBER)
			else:
				raiseError()
		
		def chapterRefList():
			if expect(TokenType.SEMICOLON):
				match(TokenType.SEMICOLON)
				chapterRef()
				chapterRefList()
			else:
				pass # lambda
		
		def verseRefList():
			if expect(TokenType.COMMA):
				match(TokenType.COMMA)
				verseRef()
				verseRefList()
			else:
				pass # lambda
		
		def book():
			if expect("1") or expect("2") or expect("3") or expect("4"):
				bookNum()
			elif expect("JS"):
				match("JS")
				match(TokenType.DASH)
				js()
			elif expect("Joseph"):
				match("Joseph")
				match("Smith")
				joseph()
			elif expect("Abraham") or expect("Acts") or expect("Alma") or expect("Amos") or expect("Colossians") or expect("Daniel") or expect("Deuteronomy") or expect("Ecclesiastes") or expect("Enos") or expect("Ephesians") or expect("Esther") or expect("Ether") or expect("Exodus") or expect("Ezekiel") or expect("Ezra") or expect("Galatians") or expect("Genesis") or expect("Habakkuk") or expect("Haggai") or expect("Hebrews") or expect("Helaman") or expect("Hosea") or expect("Isaiah") or expect("Jacob") or expect("James") or expect("Jarom") or expect("Jeremiah") or expect("Job") or expect("Joel") or expect("John") or expect("Jonah") or expect("Joshua") or expect("Jude") or expect("Judges") or expect("Lamentations") or expect("Leviticus") or expect("Luke") or expect("Malachi") or expect("Mark") or expect("Matthew") or expect("Micah") or expect("Mormon") or expect("Moroni") or expect("Moses") or expect("Mosiah") or expect("Nahum") or expect("Nehemiah") or expect("Numbers") or expect("Obadiah") or expect("OD") or expect("Omni") or expect("Philemon") or expect("Philippians") or expect("Proverbs") or expect("Psalms") or expect("Revelation") or expect("Romans") or expect("Ruth") or expect("Song") or expect("Titus") or expect("Zechariah") or expect("Zephaniah") or expect("Abr") or expect("Col") or expect("Dan") or expect("Deut") or expect("Eccl") or expect("Eph") or expect("Esth") or expect("Ex") or expect("Ezek") or expect("Gal") or expect("Gen") or expect("Hab") or expect("Hag") or expect("Heb") or expect("Hel") or expect("Isa") or expect("Jer") or expect("Josh") or expect("Judg") or expect("Lam") or expect("Lev") or expect("Mal") or expect("Matt") or expect("Morm") or expect("Moro") or expect("Neh") or expect("Num") or expect("Obad") or expect("Philem") or expect("Philip") or expect("Prov") or expect("Ps") or expect("Rev") or expect("Rom") or expect("Zech") or expect("Zeph") or expect("Articles") or expect("A") or expect("Doctrine") or expect("Official") or expect("Song") or expect("Words") or expect("W") or expect("D"):
				bookName()
			else:
				raiseError()
		
		def bookNum():
			if expect("1"):
				match("1")
				NN12()
			elif expect("2"):
				match("2")
				NN12()
			elif expect("3"):
				match("3")
				NN3()
			elif expect("4"):
				match("4")
				NN4()
			else:
				raiseError()
		
		def js():
			if expect("H"):
				match("H")
			elif expect("M"):
				match("M")
			else:
				raiseError()
		
		def joseph():
			if expect("History"):
				match("History")
			elif expect("Matthew"):
				match("Matthew")
			else:
				raiseError()
		
		def NN12():
			if expect("Chr"):
				match("Chr")
				match(TokenType.PERIOD)
			elif expect("Cor"):
				match("Cor")
				match(TokenType.PERIOD)
			elif expect("Jn"):
				match("Jn")
				match(TokenType.PERIOD)
			elif expect("Kgs"):
				match("Kgs")
				match(TokenType.PERIOD)
			elif expect("Ne"):
				match("Ne")
				match(TokenType.PERIOD)
			elif expect("Pet"):
				match("Pet")
				match(TokenType.PERIOD)
			elif expect("Sam"):
				match("Sam")
				match(TokenType.PERIOD)
			elif expect("Thes"):
				match("Thes")
				match(TokenType.PERIOD)
			elif expect("Tim"):
				match("Tim")
				match(TokenType.PERIOD)
			elif expect("Chronicles"):
				match("Chronicles")
			elif expect("Corinthians"):
				match("Corinthians")
			elif expect("John"):
				match("John")
			elif expect("Kings"):
				match("Kings")
			elif expect("Nephi"):
				match("Nephi")
			elif expect("Peter"):
				match("Peter")
			elif expect("Samuel"):
				match("Samuel")
			elif expect("Thessalonians"):
				match("Thessalonians")
			elif expect("Timothy"):
				match("Timothy")
			else:
				raiseError()
		
		def NN3():
			if expect("Jn"):
				match("Jn")
				match(TokenType.PERIOD)
			elif expect("Ne"):
				match("Ne")
				match(TokenType.PERIOD)
			elif expect("John"):
				match("John")
			elif expect("Nephi"):
				match("Nephi")
			else:
				raiseError()
		
		def NN4():
			if expect("Ne"):
				match("Ne")
				match(TokenType.PERIOD)
			elif expect("Nephi"):
				match("Nephi")
			else:
				raiseError()
		
		def bookName():
			if expect("Abraham"):
				match("Abraham")
			elif expect("Acts"):
				match("Acts")
			elif expect("Alma"):
				match("Alma")
			elif expect("Amos"):
				match("Amos")
			elif expect("Colossians"):
				match("Colossians")
			elif expect("Daniel"):
				match("Daniel")
			elif expect("Deuteronomy"):
				match("Deuteronomy")
			elif expect("Ecclesiastes"):
				match("Ecclesiastes")
			elif expect("Enos"):
				match("Enos")
			elif expect("Ephesians"):
				match("Ephesians")
			elif expect("Esther"):
				match("Esther")
			elif expect("Ether"):
				match("Ether")
			elif expect("Exodus"):
				match("Exodus")
			elif expect("Ezekiel"):
				match("Ezekiel")
			elif expect("Ezra"):
				match("Ezra")
			elif expect("Galatians"):
				match("Galatians")
			elif expect("Genesis"):
				match("Genesis")
			elif expect("Habakkuk"):
				match("Habakkuk")
			elif expect("Haggai"):
				match("Haggai")
			elif expect("Hebrews"):
				match("Hebrews")
			elif expect("Helaman"):
				match("Helaman")
			elif expect("Hosea"):
				match("Hosea")
			elif expect("Isaiah"):
				match("Isaiah")
			elif expect("Jacob"):
				match("Jacob")
			elif expect("James"):
				match("James")
			elif expect("Jarom"):
				match("Jarom")
			elif expect("Jeremiah"):
				match("Jeremiah")
			elif expect("Job"):
				match("Job")
			elif expect("Joel"):
				match("Joel")
			elif expect("John"):
				match("John")
			elif expect("Jonah"):
				match("Jonah")
			elif expect("Joshua"):
				match("Joshua")
			elif expect("Jude"):
				match("Jude")
			elif expect("Judges"):
				match("Judges")
			elif expect("Lamentations"):
				match("Lamentations")
			elif expect("Leviticus"):
				match("Leviticus")
			elif expect("Luke"):
				match("Luke")
			elif expect("Malachi"):
				match("Malachi")
			elif expect("Mark"):
				match("Mark")
			elif expect("Matthew"):
				match("Matthew")
			elif expect("Micah"):
				match("Micah")
			elif expect("Mormon"):
				match("Mormon")
			elif expect("Moroni"):
				match("Moroni")
			elif expect("Moses"):
				match("Moses")
			elif expect("Mosiah"):
				match("Mosiah")
			elif expect("Nahum"):
				match("Nahum")
			elif expect("Nehemiah"):
				match("Nehemiah")
			elif expect("Numbers"):
				match("Numbers")
			elif expect("Obadiah"):
				match("Obadiah")
			elif expect("OD"):
				match("OD")
			elif expect("Omni"):
				match("Omni")
			elif expect("Philemon"):
				match("Philemon")
			elif expect("Philippians"):
				match("Philippians")
			elif expect("Proverbs"):
				match("Proverbs")
			elif expect("Psalms"):
				match("Psalms")
			elif expect("Revelation"):
				match("Revelation")
			elif expect("Romans"):
				match("Romans")
			elif expect("Ruth"):
				match("Ruth")
			elif expect("Song"):
				match("Song")
			elif expect("Titus"):
				match("Titus")
			elif expect("Zechariah"):
				match("Zechariah")
			elif expect("Zephaniah"):
				match("Zephaniah")
			elif expect("Abr"):
				match("Abr")
				match(TokenType.PERIOD)
			elif expect("Col"):
				match("Col")
				match(TokenType.PERIOD)
			elif expect("Dan"):
				match("Dan")
				match(TokenType.PERIOD)
			elif expect("Deut"):
				match("Deut")
				match(TokenType.PERIOD)
			elif expect("Eccl"):
				match("Eccl")
				match(TokenType.PERIOD)
			elif expect("Eph"):
				match("Eph")
				match(TokenType.PERIOD)
			elif expect("Esth"):
				match("Esth")
				match(TokenType.PERIOD)
			elif expect("Ex"):
				match("Ex")
				match(TokenType.PERIOD)
			elif expect("Ezek"):
				match("Ezek")
				match(TokenType.PERIOD)
			elif expect("Gal"):
				match("Gal")
				match(TokenType.PERIOD)
			elif expect("Gen"):
				match("Gen")
				match(TokenType.PERIOD)
			elif expect("Hab"):
				match("Hab")
				match(TokenType.PERIOD)
			elif expect("Hag"):
				match("Hag")
				match(TokenType.PERIOD)
			elif expect("Heb"):
				match("Heb")
				match(TokenType.PERIOD)
			elif expect("Hel"):
				match("Hel")
				match(TokenType.PERIOD)
			elif expect("Isa"):
				match("Isa")
				match(TokenType.PERIOD)
			elif expect("Jer"):
				match("Jer")
				match(TokenType.PERIOD)
			elif expect("Josh"):
				match("Josh")
				match(TokenType.PERIOD)
			elif expect("Judg"):
				match("Judg")
				match(TokenType.PERIOD)
			elif expect("Lam"):
				match("Lam")
				match(TokenType.PERIOD)
			elif expect("Lev"):
				match("Lev")
				match(TokenType.PERIOD)
			elif expect("Mal"):
				match("Mal")
				match(TokenType.PERIOD)
			elif expect("Matt"):
				match("Matt")
				match(TokenType.PERIOD)
			elif expect("Morm"):
				match("Morm")
				match(TokenType.PERIOD)
			elif expect("Moro"):
				match("Moro")
				match(TokenType.PERIOD)
			elif expect("Neh"):
				match("Neh")
				match(TokenType.PERIOD)
			elif expect("Num"):
				match("Num")
				match(TokenType.PERIOD)
			elif expect("Obad"):
				match("Obad")
				match(TokenType.PERIOD)
			elif expect("Philem"):
				match("Philem")
				match(TokenType.PERIOD)
			elif expect("Philip"):
				match("Philip")
				match(TokenType.PERIOD)
			elif expect("Prov"):
				match("Prov")
				match(TokenType.PERIOD)
			elif expect("Ps"):
				match("Ps")
				match(TokenType.PERIOD)
			elif expect("Rev"):
				match("Rev")
				match(TokenType.PERIOD)
			elif expect("Rom"):
				match("Rom")
				match(TokenType.PERIOD)
			elif expect("Zech"):
				match("Zech")
				match(TokenType.PERIOD)
			elif expect("Zeph"):
				match("Zeph")
				match(TokenType.PERIOD)
			elif expect("Articles"):
				match("Articles")
				match("of")
				match("Faith")
			elif expect("A"):
				match("A")
				match("of")
				match("F")
			elif expect("Doctrine"):
				match("Doctrine")
				match("and")
				match("Covenants")
			elif expect("Official"):
				match("Official")
				match("Declaration")
			elif expect("Song"):
				match("Song")
				match("of")
				match("Solomon")
			elif expect("Words"):
				match("Words")
				match("of")
				match("Mormon")
			elif expect("W"):
				match("W")
				match("of")
				match("M")
			elif expect("D"):
				match("D")
				match(TokenType.AMPERSAND)
				match("C")
			else:
				raiseError()
		
		file()
	


