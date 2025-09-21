# 🚀 重新上传完整指南

## 🎯 目标
删除GitHub上的 "Conference" 文件夹，重新上传所有文件到根目录。

## 📁 需要上传的文件清单

### ✅ 根目录文件 (直接拖拽到仓库根目录)
```
✅ index.html              # 主网站文件 (16KB)
✅ test.html               # 测试页面 (4KB)
✅ README.md               # 项目说明 (3KB)
✅ parse_csv.py            # 数据解析脚本 (8KB)
```

### ✅ data/ 文件夹 (创建data文件夹，然后上传)
```
data/
✅ events.json             # 活动数据 (1.6MB) ⭐ 最重要!
✅ Generative AI Events [by cerebralvalley.ai] - 2025 Events.csv
✅ Generative AI Events [by cerebralvalley.ai] - 2025 Hackathons.csv
✅ techweek.json
```

## 🛠️ 重新上传步骤

### 步骤1: 清理GitHub仓库
1. 进入 https://github.com/walden-lin/ai-crypto-conferences
2. **删除整个 "Conference" 文件夹**
3. 确保仓库根目录是空的

### 步骤2: 上传根目录文件
1. 点击 "uploading an existing file"
2. **直接拖拽以下文件到根目录**:
   - `index.html`
   - `test.html`
   - `README.md`
   - `parse_csv.py`
3. 提交更改

### 步骤3: 创建data文件夹
1. 点击 "Create new file"
2. 文件名输入: `data/events.json`
3. 复制 `events.json` 的内容粘贴进去
4. 提交更改

### 步骤4: 上传其他data文件
1. 重复步骤3，上传其他文件到data文件夹:
   - `Generative AI Events [by cerebralvalley.ai] - 2025 Events.csv`
   - `Generative AI Events [by cerebralvalley.ai] - 2025 Hackathons.csv`
   - `techweek.json`

### 步骤5: 启用GitHub Pages
1. Settings → Pages
2. Source: "Deploy from a branch"
3. Branch: "main"
4. Folder: "/ (root)"
5. Save

## ✅ 最终验证

### 检查仓库结构
访问: https://github.com/walden-lin/ai-crypto-conferences

**应该看到:**
```
ai-crypto-conferences/
├── index.html              # ✅ 在根目录
├── test.html               # ✅ 在根目录
├── README.md               # ✅ 在根目录
├── parse_csv.py            # ✅ 在根目录
└── data/                   # ✅ 在根目录
    ├── events.json         # ✅ 在data文件夹
    └── 其他CSV文件
```

**不应该看到:**
- "Conference" 文件夹
- 任何子文件夹包含网站文件

### 访问网站
等待5-10分钟后访问:
```
https://walden-lin.github.io/ai-crypto-conferences
```

**成功标志:**
- 看到 "AI & Crypto Events Timeline" 标题
- 显示4,887个活动
- 过滤器正常工作
- 响应式设计正常

## ⚠️ 关键要点
1. **所有文件必须在根目录**
2. **不要创建任何子文件夹**
3. **`index.html` 必须在根目录**
4. **等待GitHub Pages部署完成**

---
**🎯 按照这个指南重新上传，你的网站就能完美运行!**
