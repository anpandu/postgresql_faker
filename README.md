# PostgreSQL Faker

Sometimes we need to seed a certain PostgreSQL table with fake data for a certain period of time. 
This app will do inserting task with configurable data and insertion interval.

## How to use

### Init

```sh
# clone
git clone https://github.com/anpandu/postgresql_faker
cd postgresql_faker

# set env var
cp .env.template .env
nano .env

# set metadata
nano metadata.json
```

### Run Manually

```sh
# install dependencies
sudo apt-get -y  install libpq-dev python-dev
sudo apt-get -y install python-dev build-essential
sudo apt-get -y install python-pip

# set virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run
make start

```

### Docker

```sh
# build docker image and run
make build
make docker-run-detach

# monitor
docker logs -f postgresql_faker

```

## Example

### Metadata

File below is the metadata for generating fake data and inserting it into users table.

```json
[
  {
    "column": "id",
    "udt": "serial",
    "is_default": true
  },
  {
    "column": "email",
    "udt": "email",
    "is_default": false
  },
  {
    "column": "name",
    "udt": "name",
    "is_default": false
  },
  {
    "column": "status",
    "udt": "varchar(16)",
    "is_default": false
  },
  {
    "column": "description",
    "udt": "text",
    "is_default": false
  },
  {
    "column": "created_at",
    "udt": "timestamp",
    "is_default": false
  }
]
```


### Environment Variables

Below is the example of custom env var.

```properties
TABLE=users
ROWS_NUM=2
INTERVAL=1
METADATA=./metadata.json
LOCALE=en_US
STYLED=True

PG_HOST=localhost
PG_PORT=5432
PG_USER=admin
PG_PASSWORD=admin123
PG_DATABASE=mydb
```
We can set table name, rows num per insert query, insertion interval, and locale.

### Result

If we run faker with configurations above, faker will insert two rows every 1 second. Insert query will be something like this.

```sql
INSERT INTO users
  (id, email, name, status, description, created_at)
VALUES
  (default, 'lbautista@campbell.com', 'Steven Holloway', 'OptimizeCompelli', 'Agreement summer people your read sell.', '2072-09-14T21:42:54.989000Z'),
  (default, 'mspencer@gmail.com', 'Antonio Hicks', 'RepurposeScalabl', 'Cover true president mother little week affect.', '2027-05-24T04:36:23.180000Z');
```


## TODO
- [ ] Create table query
- [ ] Support various PostgreSQL's UDTs
- [ ] Parallel insertion


## References
* [Faker library for python](https://github.com/joke2k/faker)


