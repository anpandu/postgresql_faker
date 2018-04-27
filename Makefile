start:
		sh -c "python insert_continuously.py"
build:
		sh -c "docker build . -t anpandu/postgresql_faker"
build-no-cache:
		sh -c "docker build . -t anpandu/postgresql_faker --no-cache"
docker-run:
		sh -c "docker run --rm --name postgresql_faker anpandu/postgresql_faker"
docker-run-detach:
		sh -c "docker run --rm --name postgresql_faker -d anpandu/postgresql_faker"
