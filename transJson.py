import chardet
import pandas as pd
import json

# def detect_file_encoding(file_path):
#     with open(file_path, 'rb') as file:
#         raw_data = file.read()
#         result = chardet.detect(raw_data)
#         encoding = result['encoding']
#         return encoding

def read_csv_to_json(csv_file, output_json):
    # encoding = detect_file_encoding(csv_file)
    # print(f"检测到的文件编码为: {encoding}")

    # 尝试读取Excel文件
    df = pd.read_excel(csv_file, skiprows=0)
    print(df)

    # 打印列名和前几行数据以确认结构


    data = []

    for index, row in df.iterrows():
        print(row)


        jso = {
            "address_name": row[1],
            "address": row[0],
            "data_type": "bool"
        }
        data.append(jso)
        print(jso)

    # 将数据转换为JSON格式并写入文件
    try:
        with open(output_json, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"成功将数据写入JSON文件: {output_json}")
    except Exception as e:
        print(f"写入JSON文件时出错: {e}")

# 主函数
if __name__ == "__main__":
    csv_file = ''
    output_json = ''

    # 调用函数读取CSV并生成JSON文件
    read_csv_to_json(csv_file, output_json)