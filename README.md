1. 创建虚拟环境
- conda create --name env_name python=3.9创建新的虚拟环境
- conda activate env_name进入虚拟环境
- pip install -r requirements.txt下载所需库
- pytorh版本最低为1.13.1，实际需要跟gpu的cuda版本对齐。

2. 制作微调数据
- 收集微调所需数据后，需要将数据格式修改为alpaca格式，详细格式样例见lora-finetune/data/alpaca_en_demo.json
- 在projects/lora-finetune/data/dataset_info.json中注册微调数据

3. 下载微调模型
- 将需要微调的模型下载在lora-finetune中

4. lora微调
- 修改lora-finetune/examples/train_lora/llama3_lora_sft.yaml文件："model_name_or_path:"为模型文件夹路径；"dataset:"为数据集名称，"dataset_dir:"为数据集路径；"output_dir:"为微调权重输出路径，其他超参数根据需求调整
- 在终端输入llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml开始lora微调
- 需要其他微调方式可以修改并运行projects/lora-finetune/examples/train_lora中其他的yaml文件

5. 权重融合
- 修改lora-finetune/examples/merge_lora/llama3_lora_sft.yaml文件："model_name_or_path:"原始模型路径，"adapter_name_or_path:"微调生成新权重的路径，"export_dir:"融合后的输出路径
- 运行llamafactory-cli export examples/merge_lora/llama3_lora_sft.yaml开始模型融合