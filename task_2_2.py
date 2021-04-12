list_srt = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for idx in range(len(list_srt)):
   if list_srt[idx].isdigit() == True:
        list_srt[idx] = '"' + list_srt[idx] + '"'
        if len(list_srt[idx]) == True:
            list_srt[idx] = "0" + list_srt[idx]
print(" ".join(list_srt))





