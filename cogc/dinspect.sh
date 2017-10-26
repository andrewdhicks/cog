docker inspect -f "{{ range .Mounts }}{{.}}{{end}}" moon_template
