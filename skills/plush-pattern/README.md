# Plush Pattern Skill 毛绒纸样辅助技能

这是一个用于支持毛绒玩具、公仔、棉花娃娃、动物玩偶从图片、三视图或3D模型拆解到2D纸样方案的工作流 skill。

## 文件说明

- `SKILL.md`：skill核心规则与输出标准
- `workflow.md`：完整工作流程
- `prompts/3d_to_2d_pattern_prompt.md`：可直接复制使用的提示词模板
- `templates/factory_pattern_checklist.md`：工厂打样检查表

## 推荐使用方式

1. 准备正面图、侧面图、背面图或3D模型截图。
2. 复制 `prompts/3d_to_2d_pattern_prompt.md` 的内容。
3. 填写尺寸、面料、工艺和目标。
4. 让AI输出纸样拆分方案。
5. 根据 `templates/factory_pattern_checklist.md` 检查是否可打样。
6. 用 Blender、Plushify、Illustrator、CorelDRAW、Seamly2D 或 Rhino + ExactFlat 继续整理纸样。

## 注意

本 skill 输出的是打样辅助纸样逻辑，不等于一次性可量产成品纸样。复杂造型必须经过白胚试样和人工修版。
