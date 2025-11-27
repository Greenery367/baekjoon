txt = 'helloworld[92084]answer'

str,end = txt.find('['), txt.find(']')

print(txt[str+1:end])