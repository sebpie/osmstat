Avant d'executer, il faut editer ChangesetMonitor.py et verifier les dates de debut, fin et �ventuellement changer la liste des utilisateurs (nom de compte OSM)

Ensuite il faut avoir python d'installer et lancer le script de cette facon en ligne de commandes (terminal/cmd):
python  ChangesetMonitor.py > fichier.csv

Sous windows, on peut simplement executer le fichier stats.bat qui cr��ra stats.csv

Ce qui cr�� le fichier .csv
Ouvrir ensuite ce fichier dans excel et copier le contenu.

Ouvrir https://docs.google.com/spreadsheet/ccc?key=0AoVY0MEec8dGdENyVHZMby1IUlZPc1NVTlQtQUREdHc&hl=en_GB#gid=7
Dupliquer une des feuille de calcul en la renommant sur la p�riode voulue (e.g. semaine 41)
coller le contenu du fichier.csv dans cette feuille
trier selon le nombre de noeuds, ways... decroissants
et voila!

Sebastien Pierrel