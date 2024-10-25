import json
import os
import tkinter

#获取IIH 生成的 datasources_data.json 文件，并将其中的参数读出来
def get_datasource():
    file_path = './'
    filename = os.listdir(file_path)
    IIH_Datasource_name = 'datasources_data.json'
    # print(filename)
    if IIH_Datasource_name in filename:
        with open('./' + IIH_Datasource_name, encoding='utf-8') as file:
            data = json.load(file)
            message = 'success'
    else:
        message = 'Error'

    return data,message

#前端界面，调用读取文件的函数和生成对应资产结构的函数
def window():
    data = get_datasource()[0]
    message = get_datasource()[1]

    window = tkinter.Tk()
    window.title('自动生成资产结构')
    window.geometry('200x200')

    l2 = tkinter.Label(window, text='输入Model起始的id')
    l2.pack()

    e2 = tkinter.Entry(window, width=15)
    e2.pack()

    gen = tkinter.Button(window,
                       text='生成OPCUA Model',  # 按钮的文字
                       bg='green',  # 背景颜色
                       width=15, height=2,  # 设置长宽
                       command=lambda : gen_model(data,e2)  # 响应事件：生成模型
                       )
    gen.pack()

    out = tkinter.Button(window,
                       text='退出',  # 按钮的文字
                       bg='red',  # 背景颜色
                       width=15, height=2,  # 设置长宽
                       command=window.quit  # 响应事件：关闭窗口
                       )
    out.pack()

    window.mainloop()

#生成对应资产结构的函数
def gen_model(data,e2):
    id = e2.get()
    key_id = int(id)
    Assets = {
        "assets": [],
        "assetRelations": []
    }

    for frame in data["IEDatabus"]:
        key_id += 1
        asset_identifier = key_id
        asset_name = frame["connectorName"]
        temp_assets = {
            "name": asset_name,
            "assetId": {
                "namespaceUri": "http://Siemens.net/IIHAsset",
                "identifierType": 0,
                "identifier": str(asset_identifier),
            },
            "aspects": [],
            "variables": []
        }
        temp_relation = {
            "assetId": {
                "namespaceUri": "http://Siemens.net/IIHAsset",
                "identifierType": 0,
                "identifier": str(asset_identifier)
            },
            "children": []
        }
        for connection in frame["connections"]:
            key_id += 1
            aspect_id = key_id
            temp_aspect = {
                "name": connection,
                "parentId": {
                    "namespaceUri": "http://Siemens.net/IIHAsset",
                    "identifierType": 0,
                    "identifier": str(asset_identifier)
                },
                "aspectId": {
                    "namespaceUri": "http://Siemens.net/IIHAsset",
                    "identifierType": 0,
                    "identifier": str(aspect_id)
                },
                "variables": []
            }
            for data in frame["connections"][connection]:
                key_id += 1
                var_id = key_id
                temp_variable = {
                    "referenceId": None,
                    "assetId": {
                        "namespaceUri": "http://Siemens.net/IIHAsset",
                        "identifierType": 0,
                        "identifier": str(asset_identifier)
                    },
                    "aspectId": {
                        "namespaceUri": "http://Siemens.net/IIHAsset",
                        "identifierType": 0,
                        "identifier": str(aspect_id)
                    },
                    "name": data['tagName'],
                    "variableId": {
                        "namespaceUri": "http://Siemens.net/IIHAsset",
                        "identifierType": 0,
                        "identifier": str(var_id)
                    },
                    "semanticaMapping": None,
                    "type": 0,
                    "semanticaValidationResult": -1,
                    "validationResults": None,
                    "validationMessage": None,
                    "archive": False,
                    "cloudSync": "none"
                }
                if data["datatype"] == "String":
                    temp_variable["type"] = 2
                temp_aspect["variables"].append(temp_variable)
                # var_id = var_id + 1
            temp_assets["aspects"].append(temp_aspect)
            # aspect_id = aspect_id + 1
        # asset_identifier = asset_identifier + 1
        # print(temp_assets)
        Assets['assets'].append(temp_assets)
        Assets['assetRelations'].append(temp_relation)

    res = json.dumps(Assets, ensure_ascii=False)

    filename = 'opc_ua_model.json'
    with open(filename, 'w', encoding='utf-16') as file_obj:
        file_obj.write(res)
        print('Created!')
    return 'Success!!!!!!'

if __name__ == '__main__':
    # data = get_datasource()[0]
    # message = get_datasource()[1]
    # asset_identifier = 10
    # gen_model(data,asset_identifier)
    window()


