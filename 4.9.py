# Luo uusi etätietovarasto ja siirry sen hakemistoon
git clone <oma-repositorio>
cd <oma-repositorio>

# Lisää uusi etätietovarasto advanced-rebase
git remote add advanced-rebase https://course-gitlab.tuni.fi/git-course/advanced-rebase.git

# Nouda ja yhdistä etätietovaraston versiohistoria
git fetch advanced-rebase
git merge advanced-rebase/master --allow-unrelated-histories

# Luo uusi haara devel, joka sisältää muutokset
git checkout -b devel
echo "print('First print')" > prints.py
echo "print('Second print')" >> prints.py
git add prints.py
git commit -m "Add prints"

# Siirry takaisin päähaaraan main
git checkout main

# Yhdistä muutokset devel-haarasta fast-forwardilla
git merge devel --ff-only
