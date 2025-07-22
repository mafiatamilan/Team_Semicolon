# 🧠 Reblaze API — Powered by Django REST Framework

A full-featured Reddit-style backend API using Django + DRF.

---

## ✅ Features To Implement

### 🧍 User System
- [x] User Registration
- [x] User Login (JWT Token-based)
- [ ] Password Reset
- [ ] User Profile (with karma, joined date, etc.)

---

### 🌐 Subreddits (Communities)
- [x] Create Subreddit
- [x] View all subreddits
- [x] View subreddit detail with posts
- [x] Moderators for subreddits
- [ ] Subreddit rules / description markdown support

---

### 📝 Posts
- [x] Create post with title, content
- [x] Support media attachments (images)
- [x] List posts from subreddit
- [x] Edit/Delete post (by author or mod)
- [ ] Flair support
- [ ] Post cross-posting (share to other subreddits)

---

### 💬 Comments
- [x] Add comment to post
- [x] Nested replies
- [x] Edit/Delete comment (by author or mod)
- [ ] Collapse/expand comment threads

---

### ⬆️⬇️ Votes
- [x] Upvote post
- [x] Downvote post
- [x] Vote once per user per post
- [x] Track score based on votes
- [ ] Vote on comments

---

### 👮 Moderator System
- [x] SubredditModerator model
- [x] Promote/Demote users as mods (admin-only)
- [x] Mods can edit/delete posts/comments in their sub
- [ ] Moderator logs / audit trail

---

### 📊 Sorting & Pagination
- [x] Pagination (page, page_size)
- [x] Sort posts by:
  - [x] New
  - [x] Top (by score)
  - [ ] Hot (by score + time decay)
- [ ] Sort comments by top/new

---

### 🔐 Auth
- [x] JWT-based login
- [ ] Refresh token rotation
- [ ] Email verification
- [ ] 2FA (optional)

---

### 🛠️ Admin Panel
- [x] Django Admin for all models
- [ ] Custom admin panel for subreddit mods

---

### 📦 API Design
- [x] RESTful endpoints
- [ ] Swagger docs
- [ ] Rate limiting / throttling

---

