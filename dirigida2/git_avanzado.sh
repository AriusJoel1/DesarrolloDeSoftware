#!/bin/bash

while true; do
    echo "=== Menú Principal ==="
    echo "1) Gestión de ramas"
    echo "2) Gestión de diff"
    echo "3) Instalación de hook pre-commit"
    echo "4) Merge automatizado de una rama"
    echo "5) Generar reporte de estado del repositorio"
    echo "0) Salir"
    echo -n "Elige una opción: "
    read opcion

    case "$opcion" in
        1)
            # Gestión de ramas
            while true; do
                echo "=== Gestión de Ramas ==="
                echo "a) Crear nueva rama"
                echo "b) Cambiar a otra rama"
                echo "c) Listar todas las ramas"
                echo "d) Borrar una rama"
                echo "e) Renombrar una rama"
                echo "f) Volver al menú principal"
                echo -n "Seleccione una opción: "
                read opcion_rama

                case "$opcion_rama" in
                    a|A)
                        echo -n "Ingrese el nombre de la nueva rama: "
                        read nueva_rama
                        git branch "$nueva_rama"
                        echo "Rama '$nueva_rama' creada."
                        ;;
                    b|B)
                        echo -n "Ingrese el nombre de la rama a la que desea cambiar: "
                        read rama_destino
                        git checkout "$rama_destino"
                        echo "Cambiado a la rama '$rama_destino'."
                        ;;
                    c|C)
                        git branch
                        ;;
                    d|D)
                        echo -n "Ingrese el nombre de la rama a borrar: "
                        read rama
                        git branch -d "$rama"
                        echo "Rama '$rama' borrada."
                        ;;
                    e|E)
                        echo -n "Ingrese el nombre de la rama actual: "
                        read rama_actual
                        echo -n "Ingrese el nuevo nombre para la rama: "
                        read nuevo_nombre
                        current_branch=$(git rev-parse --abbrev-ref HEAD)
                        if [[ "$rama_actual" == "$current_branch" ]]; then
                            git branch -m "$nuevo_nombre"
                        else
                            git branch -m "$rama_actual" "$nuevo_nombre"
                        fi
                        echo "Rama '$rama_actual' renombrada a '$nuevo_nombre'."
                        ;;
                    f|F)
                        break
                        ;;
                    *)
                        echo "Opción no válida, intente de nuevo."
                        ;;
                esac
            done
            ;;
        2)
            # Gestión de diff
            while true; do
                echo "=== Gestión de Diff ==="
                echo "a) Ver diff entre dos ramas/commits"
                echo "b) Comparar diferencias de un archivo específico"
                echo "c) Volver al menú principal"
                echo -n "Seleccione una opción: "
                read opcion_diff

                case "$opcion_diff" in
                    a|A)
                        echo -n "Ingrese el primer identificador (rama o commit): "
                        read ref1
                        echo -n "Ingrese el segundo identificador (rama o commit): "
                        read ref2
                        git diff "$ref1" "$ref2"
                        ;;
                    b|B)
                        echo -n "Ingrese el primer identificador (rama o commit): "
                        read ref1
                        echo -n "Ingrese el segundo identificador (rama o commit): "
                        read ref2
                        echo -n "Ingrese la ruta del archivo: "
                        read ruta_archivo
                        git diff "$ref1" "$ref2" -- "$ruta_archivo"
                        ;;
                    c|C)
                        break
                        ;;
                    *)
                        echo "Opción no válida, intente de nuevo."
                        ;;
                esac
            done
            ;;
        3)
            # Instalación de hook pre-commit
            if [ ! -d .git/hooks ]; then
                echo "Este directorio no es un repositorio Git."
            else
                cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Hook pre-commit para verificar documentación en funciones

files=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(c|h|js)$')
for file in $files; do
    if ! grep -q "//" "$file"; then
        echo "Error: El archivo '$file' no contiene comentarios de documentación."
        exit 1
    fi
endone
exit 0
EOF
                chmod +x .git/hooks/pre-commit
                echo "Hook pre-commit instalado correctamente."
            fi
            ;;
        4)
            # Merge automatizado
            echo -n "Ingrese el nombre de la rama a fusionar: "
            read rama_merge
            git merge -X theirs "$rama_merge"
            if [ $? -eq 0 ]; then
                echo "Merge completado automáticamente utilizando la estrategia 'theirs'."
            else
                echo "Se encontraron conflictos. Por favor, resuélvalos manualmente."
            fi
            ;;
        5)
            # Generar reporte
            reporte="reporte_git.txt"
            {
                echo "=== Estado del repositorio ==="
                git status
                echo
                echo "=== Ramas existentes ==="
                git branch
                echo
                echo "=== Últimos 5 commits ==="
                git log -n 5
                echo
                echo "=== Lista de stashes ==="
                git stash list
            } > "$reporte"
            echo "Reporte guardado en '$reporte'."
            ;;
        0)
            echo "Saliendo..."
            exit 0
            ;;
        *)
            echo "Opción inválida. Intente de nuevo."
            ;;
    esac

done

