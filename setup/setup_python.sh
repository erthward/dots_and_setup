#pip install key packages, listed in ./lists/py_pkg.txt
for pkg in `ls ./lists/py_pkg.txt`
  do
    sudo pip install $pkg
  done

