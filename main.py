#Импорт библиотеки
import json



#Обьявление переменных
file = 'dump.json'  
number = str(input("Введите код профессии для поиска: "))
skills = False


#Открытие файла
#нахождение нужного скилла
#Нахождение нужной специальности
with open(file, 'r', encoding='utf-8') as file: 
    data = json.load(file) 
    for skill in data:
        if skill.get("model") == "data.skill":
            if skill["fields"].get("code") == number: 
                skill_code = skill["fields"].get("code")
                skill_title = skill["fields"].get("title")
                skills = True
            
              
                for profession in data:
                    if profession.get("model") == "data.specialty":
                        specialty_code = profession["fields"].get("code")
                        if specialty_code in number:  
                            specialty_title = profession["fields"].get("title")
                            specialty_educational = profession["fields"].get("c_type")
                            break
                           
                      
                break  


#Проверка условий
if not skills:
    print("=============== Не Найдено ===============") 
    
    
else:
    print("=============== Найдено ===============") 
    print(f"{specialty_code} >> Специальность {specialty_title} , {specialty_educational}")
    print(f"{skill_code} >> Квалификация {skill_title}")
