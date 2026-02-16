
# dbi3

<!-- badges: start -->
[![Lifecycle: experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
[![CRAN status](https://www.r-pkg.org/badges/version/dbi3)](https://CRAN.R-project.org/package=dbi3)
<!-- badges: end -->

The goal of this repository is to design a new database interface from scratch, based on the lessons learned from DBI and the previous R Consortium projects.
The interface provides compatibility to DBI in both directions: the new interface supports existing DBI backends (possibly with degraded performance), and backends implemented against the new interface automatically support DBI.
Backends for the new interface will be easier to implement, because they can use the full feature set provided by dbi3.

In the beginning, the issue tracker will be used to collect and categorize issues that did not fit the scope of {DBI} or related packages.
Eventually, the repository will contain a working package and a design document.

## Properties

- async-first
    - required for efficient web applications: Shiny and Plumber
    - simpler to implement a synchronous interface from an async interface than the other way round
- only pure functions/methods with callbacks
    - idiomatic to R
- agnostic to query language
    - concepts: context, connection, query objects, tables, query strings, parameters
- reference implementation: generic backend for DBI classic

## Issues and solutions

The following list of issues, collected 2024-04-14, were categorized by how (and where) they can be solved, taking into account the new [ADBC standard](https://arrow.apache.org/adbc/) and the new [adbi package](https://adbi.r-dbi.org/).

### Solved by ADBC: Performance

- [Query cancellation](https://github.com/r-dbi/dbi3/issues/20)

- [Arrow/Flight SQL](https://github.com/r-dbi/dbi3/issues/48)

- [let dbreadtable use copy ](https://github.com/r-dbi/dbi3/issues/9)

### Solved by ADBC: Data format

- [Send parameter types](https://github.com/r-dbi/dbi3/issues/2)

- [libpq expects knowledge about data types for parametrized queries](https://github.com/r-dbi/dbi3/issues/10)

- [Optionally return tibbles](https://github.com/r-dbi/dbi3/issues/58)

- [Raise error if data type domain differs between R and database](https://github.com/r-dbi/dbi3/issues/6)

- [Specialised data types in R](https://github.com/r-dbi/dbi3/issues/22)

- [Think about column conversion](https://github.com/r-dbi/dbi3/issues/17)

- [Support arrays natively](https://github.com/r-dbi/dbi3/issues/44)

### Solved by ADBC: Usability

- [Rethink `immediate` argument](https://github.com/r-dbi/dbi3/issues/47)

- [Streaming multiple statements in a single dbExecute/dbQuery/etc. call](https://github.com/r-dbi/dbi3/issues/56)

- [Add default dbWriteTable() method](https://github.com/r-dbi/dbi3/issues/51)

### To be solved by ADBC/Arrow: Usability

- [Think about asynchronous operations](https://github.com/r-dbi/dbi3/issues/19)

- [Implement RStudio Connection Contract](https://github.com/r-dbi/dbi3/issues/11)

- [dbGetChunkedQuery()](https://github.com/r-dbi/dbi3/issues/23)

### Interface: wrapper around adbcdrivermanager?

- [Progress bar for dbWriteTable?](https://github.com/r-dbi/dbi3/issues/16)

- [dbWithConnection() and dbWithResult()](https://github.com/r-dbi/dbi3/issues/24)

- [Specify n argument for dbReadTable()](https://github.com/r-dbi/dbi3/issues/25)

- [Default connection](https://github.com/r-dbi/dbi3/issues/57)

### Quoting: dbplyr?

- [`dbQuoteIdentifier` should validate SQL inputs](https://github.com/r-dbi/dbi3/issues/55)

- [Reading and writing tables with dots in name](https://github.com/r-dbi/dbi3/issues/46)

- [Stronger guarantees for quoting literals](https://github.com/r-dbi/dbi3/issues/45)

- [Specify limits per connection or per driver](https://github.com/r-dbi/dbi3/issues/52)

### SQL generation: dbplyr?

- [Allow creation of tables with primary key and/or index](https://github.com/r-dbi/dbi3/issues/4)

- [Do you have any intention of adding the "upsert" function?](https://github.com/r-dbi/dbi3/issues/18)

- [Support passing lists as arguments for queries like `SELECT a, b WHERE a IN ($1)`](https://github.com/r-dbi/dbi3/issues/43)

- [How to create an external table in Hive?](https://github.com/r-dbi/dbi3/issues/53)

- [Name collision when creating tables](https://github.com/r-dbi/dbi3/issues/41)

### Introspection: dm?

- [More arguments to dbListObjects() to narrow result set](https://github.com/r-dbi/dbi3/issues/15)

- [Think about listing temporary tables](https://github.com/r-dbi/dbi3/issues/12)

### Interface: maintenance

- [Use ellipsis::check_dots_used() in dbConnect](https://github.com/r-dbi/dbi3/issues/5)

- [Consider standard timezone and timezone_out arguments to dbConnect()](https://github.com/r-dbi/dbi3/issues/7)

- [Add tweak for restricting to one result set per connection](https://github.com/r-dbi/dbi3/issues/37)

### Documentation: maintenance

- [Dynamically list methods in generic documentation](https://github.com/r-dbi/dbi3/issues/26)

- [dbConnect should give advice about argument names](https://github.com/r-dbi/dbi3/issues/27)

- [Should backends use "Depends: DBI"?](https://github.com/r-dbi/dbi3/issues/35)

### Testing: maintenance

- [How to run tests on a user's database?](https://github.com/r-dbi/dbi3/issues/49)

- [Reenable test for dbIsReadOnly()](https://github.com/r-dbi/dbi3/issues/36)

- [Think about moving DBItest code here](https://github.com/r-dbi/dbi3/issues/8)

- [Avoid DML in tests](https://github.com/r-dbi/dbi3/issues/3)

- [Avoid hard-coded data types in queries](https://github.com/r-dbi/dbi3/issues/42)

- [Specify and test case-sensitivity for table names](https://github.com/r-dbi/dbi3/issues/40)

- [Test for formals(dbXxx) ineffective](https://github.com/r-dbi/dbi3/issues/39)

- [Specify binding of different argument types for different calls of dbBind()](https://github.com/r-dbi/dbi3/issues/38)

- [Feature Request: Virtual connection](https://github.com/r-dbi/dbi3/issues/50)

### Parameterized queries: unclear, are they necessary for data analysis?

- [Provide interfaces and support for Parameterised Queries](https://github.com/r-dbi/dbi3/issues/34)

- [Think about ways to specify placeholder in prepared/parametrized query](https://github.com/r-dbi/dbi3/issues/1)

- [Used named parameters in parameterized statements](https://github.com/r-dbi/dbi3/issues/13)

### Reconnection: unclear, long-lived or serializable connections seem a specialized use case?

- [Reconnection](https://github.com/r-dbi/dbi3/issues/54)

- [`dbIsValid()` fails in new sessions](https://github.com/r-dbi/dbi3/issues/14)

- [Connector class needs to store expression to create driver](https://github.com/r-dbi/dbi3/issues/21)

- [Feature request: add a dbResetConnection() generic](https://github.com/r-dbi/dbi3/issues/30)

### Out of scope?

- [Interface to call stored procedure with various parameters and their attributes need to be supported in DBI](https://github.com/r-dbi/dbi3/issues/29)

- [Any way to know if a connection is already inside a transaction?](https://github.com/r-dbi/dbi3/issues/28)
