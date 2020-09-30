from googletrans import Translator
translator = Translator()


def forward_backward(text, lang, times=1):

	backward_text=text

	for i in range(times):

		forward_text=translator.translate(backward_text,dest=lang).text

		backward_text=translator.translate(forward_text,dest='en').text

	return backward_text

