drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  address text not null,
  range text not null,
    item text not null
);