text = 'sdfnsm,fdns,dfnsm nfsdmfs sdf sdf sdf sdfwer 32rw fs \
werwerwer 98 er e r er  er jkl  jtyuvxx nm,5575 dh 176  wewer \
wrwewe we rwer werwer wer232342wfs wdf werwer werw sdf sdf1'

alphabet = 'abcdefghijklmnoqprstuvwxyz'

char_set = set()
symbol_set = set()

for el in text:

    if el.lower() in alphabet:
        char_set.add(el)
    else:
        symbol_set.add(el)

print('Char_set: ', char_set)
print('Symbol_set: ', symbol_set)