
import openai
import json



def get_text():
    api_key = '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'

    openai.api_key = api_key
    # Creat context system
    messages = [{"role": "system", "content":
                "Bạn là 1 nhà thơ, nhà văn xuất sắc"}]

    # Create request msg
    message = (
        "nhân dịp tết nguyên đán 2024, hay viết vài câu ngắn gọn chúc tết anh em bạn bè."
    )
    messages.append(
        {"role": "user", "content": message},
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    # Get reply data
    reply = chat.choices[0].message.content
    return str(reply)

def add_to_file(reply):
    list_text_new_year = []

    with open('new_year.json', 'r') as openfile:
        # Reading from json file
        _data = openfile.read()
        if _data:
            list_text_new_year = json.loads(_data)

    with open("new_year.json", "w") as outfile:
        if str(reply) not in list_text_new_year:
            list_text_new_year.append(str(reply))
            outfile.write(json.dumps(list_text_new_year))

def read_data():
    list_text_new_year = []

    with open('new_year.json', 'r') as openfile:
        # Reading from json file
        _data = openfile.read()
        if _data:
            list_text_new_year = json.loads(_data)
    return list_text_new_year

# for i in read_data():
#     print(i)
#     print('----------')
#     print('----------')
#     print('----------')
#     print('----------')
# print(len(read_data()))
import time
for i in range(14):
    add_to_file(reply=get_text())
    print(len(read_data()))
    time.sleep(20)