import openai


class OpenAIController:

	def __init__(self, api_key):
		self.api_key = api_key
		openai.api_key = self.api_key

	def getEngines(self):
		return  openai.Engine.list()

	def printEngines(self):
		engines = self.getEngines()
		for engine in engines.data:
			print(engine.id)


	def getCompletion(self,engineId, prompt , max_tokens = 0, logprobs = 0, echo = True ):
		completion = openai.Completion.create(engine=engineId , prompt= prompt, max_tokens= max_tokens , logprobs=logprobs, echo=echo )
		return completion

	def get_ExplainCode(self,  code,engineId="davinci-instruct-beta-v3" , temperature=0, max_tokens=128 ):
		response = openai.Completion.create(
			engine= engineId,
			prompt= code,
			temperature=temperature,
			max_tokens= max_tokens,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=0.0,
			stop=["\"\"\""]
		)
		return response

	def get_JavascriptChatBot(self,  code, engineId="davinci-codex", temperature=0, max_tokens=128 ):
		response = openai.Completion.create(
			engine=engineId,
			prompt=code,
			temperature=temperature,
			max_tokens=max_tokens,
			top_p=1.0,
			frequency_penalty=0.5,
			presence_penalty=0.0,
			stop=["You:"]
		)
		return response


	def get_FriendChat(self,  prompt, engineId="davinci", temperature=0.4, max_tokens=128 ):
		response = openai.Completion.create(
			engine=engineId,
			prompt=prompt,
			temperature=temperature,
			max_tokens=max_tokens,
			top_p=1.0,
			frequency_penalty=0.5,
			presence_penalty=0.0,
			stop=["You:"]
		)
		return response

	def get_WriteAPythonDocString(self,  prompt, engineId="davinci-codex", temperature=0, max_tokens=200 ):
		response = openai.Completion.create(
			engine=engineId,
			prompt=prompt,
			temperature=temperature,
			max_tokens=max_tokens,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=0.0,
			stop=["#", "\"\"\""]
		)
		return response

	def get_GrammarCorrection(self,  prompt, engineId="davinci", temperature=0, max_tokens=60 ):
		response = openai.Completion.create(
			engine=engineId,
			prompt=prompt,
			temperature=temperature,
			max_tokens=max_tokens,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=0.0,
			stop=["\n"]
		)
		return response

	def get_ExtractInformation(self,  prompt, engineId="davinci-instruct-beta", temperature=0, max_tokens=100 ):
		response = openai.Completion.create(
			engine=engineId,
			prompt=prompt,
			temperature=temperature,
			max_tokens=max_tokens,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=0.0
		)
		return response

	def get_Reviews(self,  prompt, engineId="davinci-instruct-beta", temperature=0.3, max_tokens=100 ):
		response = openai.Completion.create(
			engine=engineId,
			prompt=prompt,
			temperature=temperature,
			max_tokens=max_tokens,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=0.0
		)
		return response

	def get_Keywords(self, prompt, engineId="davinci", temperature=0.3, max_tokens=100):
		response = openai.Completion.create(
			engine=engineId,
			prompt=prompt+"\n\nKeywords:",
			temperature=temperature,
			max_tokens=max_tokens,
			top_p=1.0,
			frequency_penalty=0.8,
			presence_penalty=0.0,
			stop=["\n"]
		)
		return response

	def get_summarization(self, prompt, engineId="davinci", temperature=0.3, max_tokens=100):
		response = openai.Completion.create(
			engine  =   engineId,
			prompt  =   prompt+"\n\ntl;dr:",
			temperature         =   temperature,
			max_tokens          = max_tokens,
			top_p               =   1.0,
			frequency_penalty   =   0.0,
			presence_penalty    =   0.0
		)
		return response


	def get_SpreadsheetGenerator(self, prompt, engineId="davinci", temperature=0.3, max_tokens=100):
		response = openai.Completion.create(
			engine  =   engineId,
			prompt  =   prompt+"\n\ntl;dr:",
			temperature         =   temperature,
			max_tokens          = max_tokens,
			top_p               =   1.0,
			frequency_penalty   =   0.0,
			presence_penalty    =   0.0,
			stop=["\n"]
		)
		return response

	def get_NotesToSummary(self, prompt, engineId="davinci-instruct-beta", temperature=0.7, max_tokens=100):
		response = openai.Completion.create(
			engine  =   engineId,
			prompt  =   prompt+"\n\nSummary:",
			temperature         =   temperature,
			max_tokens          = max_tokens,
			top_p               =   1.0,
			frequency_penalty   =   0.0,
			presence_penalty    =   0.0
		)
		return response
