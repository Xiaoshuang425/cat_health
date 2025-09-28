const db = require('../config/database');

// 初始化数据库表
const initDatabase = () => {
  // 用户表
  const createUsersTable = `
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      password TEXT NOT NULL,
      phone TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `;

  // 猫咪档案表
  const createCatsTable = `
    CREATE TABLE IF NOT EXISTS cats (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER NOT NULL,
      name TEXT NOT NULL,
      breed TEXT,
      age INTEGER,
      weight REAL,
      gender TEXT CHECK(gender IN ('male', 'female', 'unknown')),
      avatar_url TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    )
  `;

  // 健康记录表
  const createHealthRecordsTable = `
    CREATE TABLE IF NOT EXISTS health_records (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      cat_id INTEGER NOT NULL,
      record_type TEXT NOT NULL CHECK(record_type IN ('stool', 'urine', 'vomit', 'other')),
      image_url TEXT,
      color TEXT,
      texture TEXT,
      shape TEXT,
      health_risk TEXT,
      notes TEXT,
      recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (cat_id) REFERENCES cats (id) ON DELETE CASCADE
    )
  `;

  db.serialize(() => {
    db.run(createUsersTable, (err) => {
      if (err) {
        console.error('创建用户表失败:', err);
      } else {
        console.log('用户表创建成功');
      }
    });

    db.run(createCatsTable, (err) => {
      if (err) {
        console.error('创建猫咪表失败:', err);
      } else {
        console.log('猫咪表创建成功');
      }
    });

    db.run(createHealthRecordsTable, (err) => {
      if (err) {
        console.error('创建健康记录表失败:', err);
      } else {
        console.log('健康记录表创建成功');
      }
    });
  });

  console.log('数据库初始化完成');
};

// 如果直接运行此文件，则初始化数据库
if (require.main === module) {
  initDatabase();
}

module.exports = initDatabase;