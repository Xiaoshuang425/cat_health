const db = require('../config/database');
const bcrypt = require('bcryptjs');

class User {
  // 创建用户
  static create(userData, callback) {
    const { name, email, password, phone } = userData;
    
    // 哈希密码
    bcrypt.hash(password, 10, (err, hashedPassword) => {
      if (err) return callback(err);
      
      const sql = `
        INSERT INTO users (name, email, password, phone) 
        VALUES (?, ?, ?, ?)
      `;
      
      db.run(sql, [name, email, hashedPassword, phone], function(err) {
        if (err) {
          if (err.message.includes('UNIQUE constraint failed')) {
            return callback(new Error('该邮箱已被注册'));
          }
          return callback(err);
        }
        
        callback(null, {
          id: this.lastID,
          name,
          email,
          phone
        });
      });
    });
  }

  // 通过邮箱查找用户
  static findByEmail(email, callback) {
    const sql = 'SELECT * FROM users WHERE email = ?';
    
    db.get(sql, [email], (err, row) => {
      if (err) return callback(err);
      callback(null, row);
    });
  }

  // 通过ID查找用户
  static findById(id, callback) {
    const sql = 'SELECT id, name, email, phone, created_at FROM users WHERE id = ?';
    
    db.get(sql, [id], (err, row) => {
      if (err) return callback(err);
      callback(null, row);
    });
  }

  // 验证密码
  static verifyPassword(plainPassword, hashedPassword, callback) {
    bcrypt.compare(plainPassword, hashedPassword, callback);
  }

  // 更新用户信息
  static update(id, userData, callback) {
    const { name, phone } = userData;
    const sql = `
      UPDATE users 
      SET name = ?, phone = ?, updated_at = CURRENT_TIMESTAMP 
      WHERE id = ?
    `;
    
    db.run(sql, [name, phone, id], function(err) {
      if (err) return callback(err);
      callback(null, { changes: this.changes });
    });
  }
}

module.exports = User;