const express = require('express');
const User = require('../models/user');
const { generateToken, authenticateToken } = require('../middleware/auth');

const router = express.Router();

// 用户注册
router.post('/register', async (req, res) => {
  try {
    const { name, email, password, phone } = req.body;

    // 基本验证
    if (!name || !email || !password) {
      return res.status(400).json({ 
        error: '请填写姓名、邮箱和密码' 
      });
    }

    if (password.length < 6) {
      return res.status(400).json({ 
        error: '密码长度至少6位' 
      });
    }

    // 创建用户
    User.create({ name, email, password, phone }, (err, user) => {
      if (err) {
        return res.status(400).json({ 
          error: err.message 
        });
      }

      // 生成token
      const token = generateToken(user);

      res.status(201).json({
        message: '注册成功',
        user: {
          id: user.id,
          name: user.name,
          email: user.email,
          phone: user.phone
        },
        token
      });
    });

  } catch (error) {
    res.status(500).json({ 
      error: '服务器错误，注册失败' 
    });
  }
});

// 用户登录
router.post('/login', (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ 
        error: '请填写邮箱和密码' 
      });
    }

    // 查找用户
    User.findByEmail(email, (err, user) => {
      if (err) {
        return res.status(500).json({ 
          error: '服务器错误' 
        });
      }

      if (!user) {
        return res.status(401).json({ 
          error: '邮箱或密码错误' 
        });
      }

      // 验证密码
      User.verifyPassword(password, user.password, (err, isMatch) => {
        if (err) {
          return res.status(500).json({ 
            error: '服务器错误' 
          });
        }

        if (!isMatch) {
          return res.status(401).json({ 
            error: '邮箱或密码错误' 
          });
        }

        // 生成token
        const token = generateToken(user);

        res.json({
          message: '登录成功',
          user: {
            id: user.id,
            name: user.name,
            email: user.email,
            phone: user.phone
          },
          token
        });
      });
    });

  } catch (error) {
    res.status(500).json({ 
      error: '服务器错误，登录失败' 
    });
  }
});

// 获取当前用户信息
router.get('/me', authenticateToken, (req, res) => {
  res.json({
    user: req.user
  });
});

// 更新用户信息
router.put('/profile', authenticateToken, (req, res) => {
  const { name, phone } = req.body;

  if (!name) {
    return res.status(400).json({ 
      error: '姓名不能为空' 
    });
  }

  User.update(req.user.id, { name, phone }, (err, result) => {
    if (err) {
      return res.status(500).json({ 
        error: '更新失败' 
      });
    }

    res.json({
      message: '资料更新成功',
      user: {
        ...req.user,
        name,
        phone
      }
    });
  });
});

module.exports = router;