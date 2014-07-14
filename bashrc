# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions
alias grep="grep --color=auto"
#alias pd="echo -n $USER@$HOSTNAME:`pwd`/; echo $1"
export PATH=$PATH:/home/work/safe_psqa/python/so/:/home/work/svn/bin/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/work/safe_psqa/python/so/
alias py="python"
alias ..="cd .."
alias ...="cd ../.."
export PS1="\[\033[0;33m\]\`if [[ \$? = "0" ]]; then echo "\\[\\033[32m\\]";else echo "\\[\\033[31m\\]"; fi\`[\u.\h: \`if [[ `pwd|wc -c|tr -d " "` > 18 ]];then echo "\\W"; else echo "\\w"; fi\`]\$\[\033[0m\]"
