#def process_file(filepath) :
#    with open(filepath,'r') as f :
#        print(f.read())


def process_file(filepath):
    # 1. منطقة المحاولة (جرب تفتح الملف)
    try:
        with open(filepath, 'r') as f:
            # مؤقتاً هنطبع المحتوى عشان نتأكد إنه شغال
            content = f.read()
            print("The File is found")
            print(content)
            
    # 2. منطقة الطوارئ (لو الملف مش موجود)
    except FileNotFoundError:
        print(f'The file Is NOT found BE sure from This Path  {filepath} and The Name of File')


process_file(r"D:\ACC AI_ML_BootCamp\raw_transactions.txt")         

