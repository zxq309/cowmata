# 跨仓接口提案 · draft 0.1

状态：设计约定，尚未宣称现有组件完整实现。组件当前的真实 schema 仍由各组件仓维护。

## 标注 → 识别

保留 cow_id、session_id、绑定标识、标签协议版本、机器标签代码、点/区间类型、绝对时间、来源与人工复核状态。
点事件与区间事件必须区分。产犊真值和行为训练标签分开映射；未知标签应拒绝或明确报告，不能静默改成背景。
标注可选标签不等于模型支持的训练标签。TAIL_WAGGING 等差异需要按模型/协议版本做显式映射，禁止直接修改历史标签语义。

## 识别 → 决策（待适配）

建议记录 schema_version、cow_id、binding_id、event_id、event_code、start_ms、end_ms、score、quality_status、model_version、produced_at_ms、available_at_ms。
持续状态与离散事件分别标记。所有 *_ms 是 Unix 毫秒；区分发生时间与结果可用时间，供在线预警及回放控制数据泄漏。
绑定身份不确定时保留质量标记；重传通过 event_id 或显式去重规则处理。

## 辅助模块 → 决策

以 cowmata-risk 内温度/活动模块的 output.schema.json 和 as_fusion_features 为准。
保持牛—设备—绑定一致，保存证据、质量、数据时效和版本。模块评分不直接解释为产犊概率。

## 兼容验证门槛

在启用适配器之前，至少用固定样例验证标签映射、时间单位、点/区间、重复数据、缺失证据和版本不兼容拒绝。
目前 components.json 标记的是组件基线登记，不是上述跨仓检查已通过。
