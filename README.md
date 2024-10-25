# Auto_Gen_IIH_DataAssets
自动生成 西门子 Industrial Edge IIH 数据库的 Data Asset

你还在为手动拖拽生成资产而苦恼吗，你还在把大量的时间放在点位的配置上吗？

现在统统都不需要了！！！！！！！！

使用方法：
1.先安装文件中的依赖包

2.启动代码，会自动弹出一个对话框

3.将IIH 中 Commen configurator 导出按钮生成的zip文件中的datasource.json文件放在和代码同级的文件夹下

4.在对话框中输入起始的资产ID

5.点击生成OPCUA Model即可！

6.将生成的json文件导入到 Commen configurator 中

所有生成的资产顺序和名称都是和Connector的顺序是一致和匹配的
