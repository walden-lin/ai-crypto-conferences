# 📁 手动上传到GitHub的文件结构指南

## 🎯 需要上传的核心文件

### **根目录文件 (必须上传)**
```
ai-crypto-events/
├── index.html              # 主网站文件 ⭐
├── test.html               # 测试页面
├── README.md               # 项目说明
├── parse_csv.py            # 数据解析脚本
└── .gitignore              # Git忽略文件
```

### **data/ 目录 (必须上传)**
```
data/
├── events.json             # 解析后的活动数据 ⭐ (最重要!)
├── Generative AI Events [by cerebralvalley.ai] - 2025 Events.csv
└── Generative AI Events [by cerebralvalley.ai] - 2025 Hackathons.csv
```

## 🚀 GitHub Pages 设置步骤

### 1. 创建仓库
- 仓库名: `ai-crypto-events`
- 设为 **Public** (GitHub Pages免费版需要)
- 不要初始化README (我们已经有了)

### 2. 上传文件
- 拖拽所有文件到GitHub网页界面
- 确保 `index.html` 在根目录
- 确保 `data/events.json` 存在

### 3. 启用GitHub Pages
- 进入仓库 → Settings → Pages
- Source: "Deploy from a branch"
- Branch: "main" 
- Folder: "/ (root)"
- 保存

### 4. 访问网站
```
https://walden-lin.github.io/ai-crypto-events
```

## ✅ 验证清单

上传前请确认：
- [ ] `index.html` 在根目录
- [ ] `data/events.json` 存在且不为空
- [ ] `data/` 目录包含所有CSV文件
- [ ] `README.md` 包含项目说明
- [ ] 仓库设为Public

## 🔧 如果网站不工作

1. **检查文件路径**: 确保 `index.html` 在根目录
2. **检查数据文件**: 确保 `data/events.json` 存在
3. **等待部署**: GitHub Pages需要几分钟部署
4. **检查控制台**: 打开浏览器开发者工具查看错误

## 📊 数据更新

如需更新活动数据：
1. 更新CSV文件
2. 运行 `python3 parse_csv.py`
3. 上传新的 `data/events.json`
4. 提交更改

---
**🎯 核心文件: index.html + data/events.json = 完整网站!**
