#!/usr/bin/env python3
"""
格式化示例：展示如何在 chatbot 回复中使用各种格式
"""

# 示例 1: 在 prompts 中使用 markdown 格式
EXAMPLE_PROMPT_WITH_FORMATTING = '''
你是一个严格的教官。请用以下格式回复：

**重要提醒：**
- 这是安全关键训练
- 必须严格按照规程执行

**当前状态：**
- 事件：{event_name}
- 你的角色：{user_role}
- AI角色：{ai_role}

**下一步操作：**
请重复以下句子：
**"{expected_response}"**

**注意事项：**
1. 发音要清晰
2. 语速要适中
3. 重点词汇要强调

如果准备好了，请开始练习。
'''

# 示例 2: 在 clean_response 函数中处理的格式
def example_formatted_response():
    """示例格式化回复"""
    return """
**=== 训练开始 ===**

🎯 **当前任务：** 练习轨道访问请求

**关键要点：**
- 使用标准术语
- 清晰表达意图
- 等待确认回复

**示例对话：**
```
你：Control, this is Alpha One requesting track access at signal 123.
控制台：Alpha One, this is Control. Track access granted at signal 123.
```

**练习要求：**
1. 发音清晰
2. 语速适中  
3. 重点词汇加粗

**现在请重复：**
**"Control, this is Alpha One requesting track access at signal 123."**
"""

# 示例 3: 在 display_chat_message 中支持的 HTML 标签
SUPPORTED_HTML_TAGS = """
支持的 HTML 标签：
- <strong>粗体文本</strong>
- <em>斜体文本</em>
- <h1>一级标题</h1>
- <h2>二级标题</h2>
- <h3>三级标题</h3>
- <li>列表项</li>
- <br>换行
- <code>代码</code>

支持的 Markdown 格式：
- **粗体**
- *斜体*
- # 标题
- - 列表项
- `代码`
"""

if __name__ == "__main__":
    print("📝 格式化示例")
    print("=" * 50)
    print(example_formatted_response())
    print("\n" + "=" * 50)
    print(SUPPORTED_HTML_TAGS)
