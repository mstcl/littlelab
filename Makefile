lint:
	ansible-lint --exclude main.yml

sync:
	git pull origin prod --rebase
	git push origin prod
