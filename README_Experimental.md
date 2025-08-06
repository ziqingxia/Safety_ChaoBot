# Safety ChatBot System - Experimental Version

这是一个基于 Streamlit 的实验版本安全聊天机器人系统，支持三种不同的 persona 选择。

## 🎭 Persona 选择

### 1. 严格教官 (Strict Instructor)
- **风格**: 权威、严格、强调精确性和纪律
- **特点**: 不容忍错误，强调安全性和精确性
- **适用场景**: 正式培训、严格要求的环境

### 2. 友好同事 (Friendly Peer)
- **风格**: 友好、支持性、像同事一样交流
- **特点**: 提供鼓励和实用的建议，使用"我"和"你"
- **适用场景**: 轻松学习、同伴互助

### 3. AI 助手 (AI Assistant)
- **风格**: 冷静、结构化、专注于清晰指导
- **特点**: 非人类情感，但高度响应用户需求
- **适用场景**: 结构化学习、系统性指导

## 🚀 快速开始

### 方法一：使用启动脚本
```bash
python run_streamlit_exp.py
```

### 方法二：直接运行
```bash
streamlit run streamlit_exp_app.py
```

## 📋 功能特性

- ✅ **三种 Persona 选择**: 动态切换不同的训练风格
- ✅ **实验版本聊天机器人**: 基于 `main_exp.py` 的功能
- ✅ **实时 API Key 管理**: 安全的 API 密钥输入和管理
- ✅ **对话导出**: 支持将对话保存为 JSON 格式
- ✅ **事件选择**: 多种安全事件类型可供练习
- ✅ **响应式界面**: 现代化的 Web 界面设计

## 🔧 配置说明

### 配置文件
- 主配置文件: `configs/config_exp.yaml`
- 使用相对路径，适配 Windows 环境

### 依赖文件
- `chatbot_exp.py`: 实验版本聊天机器人
- `database.py`: RAG 知识库
- `fewshot_exp.py`: 上下文学习器
- `prompts_persona1.py`: 严格教官 prompts
- `prompts_persona2.py`: 友好同事 prompts  
- `prompts_persona3.py`: AI 助手 prompts

## 🎯 使用流程

1. **设置 API Key**: 在侧边栏输入 OpenAI API Key
2. **选择 Persona**: 选择你喜欢的训练风格
3. **选择事件**: 从可用的事件类型中选择一个
4. **开始对话**: 点击"Start Conversation"开始训练
5. **导出对话**: 完成后可以导出对话记录

## 📁 文件结构

```
RAG-System-exp/
├── streamlit_exp_app.py          # 主应用文件
├── run_streamlit_exp.py          # 启动脚本
├── chatbot_exp.py               # 实验版聊天机器人
├── configs/
│   └── config_exp.yaml          # 实验版配置文件
├── prompts_persona1.py          # Persona 1 prompts
├── prompts_persona2.py          # Persona 2 prompts
├── prompts_persona3.py          # Persona 3 prompts
└── README_Experimental.md       # 本说明文档
```

## 🔄 与原版本的区别

### 新增功能
- 三种 persona 动态切换
- 实验版本的聊天流程
- 更丰富的会话状态管理
- 改进的用户界面

### 技术改进
- 动态 prompt 加载
- 模块化的 persona 系统
- 更好的错误处理
- 适配 Windows 环境的路径配置

## 🛠️ 故障排除

### 常见问题

1. **API Key 错误**
   - 确保输入正确的 OpenAI API Key
   - 检查网络连接

2. **模块导入错误**
   - 确保所有依赖文件存在
   - 检查 Python 环境

3. **路径错误**
   - 确保配置文件中的路径正确
   - 检查文件和目录是否存在

### 调试模式
```bash
streamlit run streamlit_exp_app.py --logger.level debug
```

## 📝 开发说明

### 添加新的 Persona
1. 创建新的 `prompts_personaX.py` 文件
2. 定义所需的 prompt 常量
3. 在应用中添加新的 persona 选项

### 修改配置
编辑 `configs/config_exp.yaml` 文件来调整系统参数。

## 📄 许可证

本项目基于原有的 RAG-System-exp 项目开发。

---

**注意**: 这是实验版本，可能存在一些不稳定的功能。建议在生产环境使用前进行充分测试。
