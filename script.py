from translate import Translator

translator= Translator(to_lang="ig")
try:
    with open('C:\\Users\\HP\\OneDrive\\Desktop\\Bright\\Tech\\CYBER SECURITY\\python projects\\Translator\\note.txt',  encoding='utf-8', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('C:\\Users\\HP\\OneDrive\\Desktop\\Bright\\Tech\\CYBER SECURITY\\python projects\\Translator\\text-es.txt', encoding='utf-8',  mode='w') as my_file2:
            my_file2.write(translation)
except Exception  as e:
    print("Check your file path", e)