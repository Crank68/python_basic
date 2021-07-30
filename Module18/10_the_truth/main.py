english_alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt ' \
       'cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf ' \
       'dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt ' \
       'foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc' \
       ' pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf ' \
       'sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf ' \
       'tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
pre_final_text = ''

text = text.split()
result = ''
for word in text:
    if not word.islower() and word != 'i/Evud' and word != '..':
        result += '\n'
    for symbol in word:
        if symbol in english_alph:
            index = english_alph.find(symbol)
            result += english_alph[index - 1]
        else:
            result += symbol
    result += ' '

list_result = result.split('\n')
list_result.pop(0)

shift = 3
for string in list_result:
    list_string = string.split()
    for elem in list_string:
        real_shift = shift
        while real_shift > len(elem):
            real_shift -= len(elem)
        for index in range(-real_shift, len(elem) - real_shift):
            pre_final_text += elem[index]
        pre_final_text += ' '
    pre_final_text += '\n'

    shift += 1

final_text = pre_final_text.replace('/', '.')
final_text = final_text.replace('"', '!')
final_text = final_text.replace('(', "'")
final_text = final_text.replace('+', "*")
final_text = final_text.replace('+', "*")
final_text = final_text.replace('-', ",")
final_text = final_text.replace('..', "--")

print(final_text)
