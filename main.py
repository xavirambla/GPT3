#!/usr/bin/python
# -*- coding: UTF-8 -*-


#    https://beta.openai.com/playground


import sys
sys.path.insert(0, "../libs")

from input_output import *
from controller.OpenAIController import OpenAIController
import argparse


api_key = "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"

parser = argparse.ArgumentParser(description=None)

parser.add_argument("-i",  "--input", default="" ,   help = "Fichero con el texto de entrada" )
parser.add_argument("-o",  "--output",               help = "Fichero con el resultado de la salida")
parser.add_argument("-e",  "--engine",               help = "Motor que se desea utilizar")
parser.add_argument("-s", "--showengines",   default=0,       help = "Muestra todos los motores disponibles")

args = parser.parse_args()

print (f"Input : {args.input}")
print (f"Output : {args.output}")



openAIController   = OpenAIController(api_key)

if (args.showengines):
	openAIController.printEngines()
	exit()

prompt =  Input_output.fileToVariable(args.input)     if     args.input  else     str(input("Texto a tratar:"))
engine =  args.engine     if     args.engine  else    "davinci"


completion = openAIController.getCompletion(engineId=engine, prompt=prompt )

# create a completion
#completion = openAIController.getCompletion(engineId="davinci", prompt="Resumen del informe anual de ventas en Cataluña" )

#así asa
#completion = openAIController.get_ExplainCode(engineId="davinci-instruct-beta-v3", code="from controller.OpenAIController import OpenAIController" )

#no funciona
#completion = openAIController.get_JavascriptChatBot("JavaScript chatbot\n\n\nYou: How do I combine arrays?\nJavaScript chatbot: You can use the concat() method.\nYou: How do make an alert appear after 10 seconds?\nJavaScript chatbot:"                                                    )
#funciona bien.
#completion = openAIController.get_FriendChat("You: Has visto alguna serie últimamente?\nFriend: Veo cosas en Netflix.\nYou: Alguna serie interesante?\nFriend:")

#no funciona. motor no activo aún
#completion = openAIController.get_WriteAPythonDocString("Python 3.7\n \ndef randomly_split_dataset(folder, filename, split_ratio=[0.8, 0.2]):\n    df = pd.read_json(folder + filename, lines=True)\n    train_name, test_name = \"train.jsonl\", \"test.jsonl\"\n    df_train, df_test = train_test_split(df, test_size=split_ratio[1], random_state=42)\n    df_train.to_json(folder + train_name, orient='records', lines=True)\n    df_test.to_json(folder + test_name, orient='records', lines=True)\nrandomly_split_dataset('finetune_data/', 'dataset.jsonl')\n    \n# An elaborate, high quality docstring for the above function:\n\"\"\"")

#funciona bien
#completion = openAIController.get_GrammarCorrection("Original: She no went to the market.\nStandard American English:")
#completion = openAIController.get_GrammarCorrection("Original: Thanks for your propuse, but I'm not finding a job.\nStandard American English:")
#sirve como traductor también
#completion = openAIController.get_GrammarCorrection("Original: Gracias por darme esta oportunidad.\nStandard American English:")
#completion = openAIController.get_GrammarCorrection("Original: El gato come una raspa de pescado.\nStandard American English:")

#horrible
#completion = openAIController.get_ExtractInformation("Estimado vecino, \nmi nombre es xavi y vengo de Abrera para encontrarme con usted,\n Tengo disponible a las 11. Le iría bien vernos?\n" + "name,city, hour")
#regular
#completion = openAIController.get_ExtractInformation("Extract the mailing address from this email:\n\nDear Xavi,\n\nIt was great to talk to you at the seminar. I thought Jane's talk was quite good.\n\nThank you for the book. Here's my address 08630 Abrera, Barcelona España 92002\n\nBest,\n\nMaya\n\nName and address:\n")

#va bastante bien
#completion = openAIController.get_Reviews("Write a newspaper review based on these notes:\n\nName: Bitcoin Website\nCoins, bitcoin, sell,buy , wallet.\n\nReview:"  )
#completion = openAIController.get_Reviews("Create a list of questions for my interview with a science fiction author:\n\n1.");

#va bien
#completion = openAIController.get_Keywords("Text: Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors.")
#completion = openAIController.get_Keywords("El electrodo permite que circule la corriente eléctrica en el interior de la célula y, por tanto, provocar la descomposición de la sal en sodio y cloro. De esta manera se obtiene cloro como desinfectante natural del agua. La cloración salina favorece el uso de un producto natural y sustituye los desinfectante químicos que pueden perjudicar a los bañistas.")

#va bien
#completion = openAIController.get_summarization("El electrodo permite que circule la corriente eléctrica en el interior de la célula y, por tanto, provocar la descomposición de la sal en sodio y cloro. De esta manera se obtiene cloro como desinfectante natural del agua. La cloración salina favorece el uso de un producto natural y sustituye los desinfectante químicos que pueden perjudicar a los bañistas.")


#completion = openAIController.get_NotesToSummary("Convert my short hand into a first-hand account of the meeting:\n\nTom: Profits up 50%\nJane: New servers are online\nKjel: Need more time to fix software\nJane: Happy to help\nParkman: Beta testing almost done")


print("RESULT")

for choice in completion.choices:
	if args.output:
		Input_output.variableToFile(args.output, choice.text )
	print( choice.text )

