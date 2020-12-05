# 1.初始化git
ssh-keygen -t ed25519 -C "386729558@qq.com"
cat /home/yanbing/.ssh/id_ed25519.pub
# 去平台增加ssh_keys
ssh -T git@github.com
git config --global user.name "row-yanbing"
git config --global user.email "386729558@qq.com"
# shell显示git分支
vim ~/.bashrc
source ~/.bashrc
# 2. clone
git clone git@github.com:row-yanbing/code_knowledge.git
# 3. checkout
git checkout python
# 4. 查看分支状态
git status
# 5. add
git add .gitignore datetime_util.py 
git add -u
# 6. commit
git commit -m 'datetime的用法'
# 7. push
git push

# 其他命令
# 增加忽略文件
vim .gitignore 
# 更新
git pull
# log
git log
git log --pretty=oneline

