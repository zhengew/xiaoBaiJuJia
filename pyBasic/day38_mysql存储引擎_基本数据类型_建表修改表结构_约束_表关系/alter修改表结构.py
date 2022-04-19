'''
语法：
1. 修改表名
      ALTER TABLE 表名
                      RENAME 新表名;

2. 增加字段
      ALTER TABLE 表名
                      ADD 字段名  数据类型 [完整性约束条件…],
                      ADD 字段名  数据类型 [完整性约束条件…];

3. 删除字段
      ALTER TABLE 表名
                      DROP 字段名;

4. 修改字段
      ALTER TABLE 表名
                      MODIFY  字段名 数据类型 [完整性约束条件…]; -- 常用
      ALTER TABLE 表名
                      CHANGE 旧字段名 新字段名 旧数据类型 [完整性约束条件…];
      ALTER TABLE 表名
                      CHANGE 旧字段名 新字段名 新数据类型 [完整性约束条件…];

5.修改字段排列顺序/在增加的时候指定字段位置
    ALTER TABLE 表名
                     ADD 字段名  数据类型 [完整性约束条件…]  FIRST;
    ALTER TABLE 表名
                     ADD 字段名  数据类型 [完整性约束条件…]  AFTER 字段名;
    ALTER TABLE 表名
                     CHANGE 字段名  旧字段名 新字段名 新数据类型 [完整性约束条件…]  FIRST;
    ALTER TABLE 表名
                     MODIFY 字段名  数据类型 [完整性约束条件…]  AFTER 字段名;

'''