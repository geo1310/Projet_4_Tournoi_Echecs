## Configuration de l'environnement

### Installation et activation de l'environnement Virtuel
Ouvrez un nouveau terminal et taper  
```
python -m venv .venv-projet4
```
Selectionner l'environnement virtuel dans visual studio code ou l'activer en se plaçant dans le dossier **venv-projet4/scripts** et taper
```
./activate
```
Installer les dependances necessaires au projet
```
pip install -r requirements.txt
```

### Procédure en cas de restriction de sécurité sur le lancement des scripts

Dans l'invite de commandes, tapez la commande suivante pour afficher la politique d'exécution actuelle :
```
Get-ExecutionPolicy
```

Vous pouvez modifier la politique d'exécution en utilisant la commande Set-ExecutionPolicy. Par exemple, pour permettre l'exécution de scripts locaux (ce qui est généralement sûr), vous pouvez définir la politique d'exécution sur "RemoteSigned". Tapez la commande suivante :
```
Set-ExecutionPolicy RemoteSigned
```

Vous pouvez également définir la politique sur "Bypass" pour permettre l'exécution de tous les scripts sans restriction, mais cela comporte des risques de sécurité. Utilisez cette option avec prudence.

## Lancement et Fonctionnement de l'Application Chess Tournament

