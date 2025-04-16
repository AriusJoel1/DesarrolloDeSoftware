#Actividad 4

#### Configuración inicial de Git
```bash
$ git config --global user.name "AriusJoel1"
$ git config --global user.email "joel.seminario.s@uni.pe"
```

## Ingreso al repositorio local
```bash
$ cd Desktop\DesarrolloDeSoftware
```

## Crear y entrar a la carpeta de actividad
```bash
$ mkdir actividad4
$ cd actividad4
```

## Inicializar repositorio Git
```bash
$ git init
```

## Crear archivo README y verificar
```bash
$ echo "README" > README.md
$ git commit
$ git status
```

## Agregar y confirmar README
```bash
$ git add README.md
$ git commit -m "Initial commit with README.md"
$ git log
```

## Agregar archivo Python de ejemplo
```bash
$ echo "print( 'hello world') " > main.py
$ git add .
$ git commit -m "Add main.py"
$ git log --oneline
```

## Ver rama actual
```bash
$ git branch
```

## Crear y cambiar a rama nueva
```bash
$ git branch feature/new-feature
$ git checkout feature/new-feature
```

## Crear y moverse entre ramas
```bash
$ git branch new branch-name
$ git checkout new branch-name
$ git branch base-branch-name
$ git checkout feature
```

## Crear y cambiar a rama develop
```bash
$ git branch develop
$ git checkout develop
```

## Crear nueva rama desde otra
```bash
$ git branch feature/login develop
$ git checkout feature/login develop
```

## Crear rama desde un commit específico
```bash
$ git branch hotfix/bugfix 802551f
$ git checkout hotfix/bugfix
```

## Cambiar entre ramas
```bash
$ git switch feature/new-feature
$ git checkout -b feature/another-new-feature
```

## Unir ramas y eliminar rama local
```bash
$ git checkout main
$ git merge feature/new-feature
$ git branch -d feature/new-feature
```

## Volver al directorio principal
```bash
$ cd ..
$ cd ..
```

## Crear nueva rama y moverse
```bash
$ git branch feature/advanced-feature
$ git checkout feature/advanced-feature
```

## Editar main.py y confirmar cambios
```python
print('Hello World - updated in main')
```
```bash
$ git add main.py
$ git commit -m "update main.py mensaje en rama main"
$ git merge feature/advanced-feature
$ git commit - "resolve merge conflic"
```

## Ver commits realizados
```bash
$ git log --author="AriusJoel1"
$ git log --graph --oneline --all
```

## Crear rama desde nuevo commit
```bash
$ git branch bugfix/rollback-feature fd5de5a
```

## Modificar main.py y aplicar cambios
```python
print('hello wordl!')

def greet():
    print('Fixed bug in feature')
greet()
```
```bash
$ git add main.py
$ git commmit -m "fix bug"
$ git checkout main
$ git merge bugfix/rollback-feature
$ git branch -D bugfix/rollback-feature
```

## Editar y deshacer cambios
```python
print('hello word')

def greet():
    print('Fixed bug in feature')
greet()

print('this cange will be reset')
```
```bash
$ git add main.py
$ git commit -m "temp change"
$ git reset --hard HEAD~1
```

## Clonar repositorio
```bash
$ git clone "https://github.com/AriusJoel1/DesarrolloDeSoftware.git"
```

## Crear rama de colaboración
```bash
$ git branch feature/team-feature
$ echo "print('Collaboration is key!')" > collaboration.py
$ git add .
$ git commit -m "Add collaboration script"
$ git push origin feature/team-feature
```

## Modificar rama main y usar cherry-pick
```bash
$ git checkout main
$ echo "print('Cherry pick this!')" >> main.py
$ git add main.py
$ git commit -m "add cherry-pick example"
$ git cherry-pick <hash-del-commit>
```

## Realizar cambios sin confirmar
```bash
$ echo "This change is stashed" >> main.py
$ git cherry-pick --continue
```

## Ver historial de commits
```bash
$ git log
```
