# catalyst-count

catalyst-count is a Django web application designed for uploading and querying large CSV datasets. It allows users to upload a 1GB CSV file with visual progress indication, process the data into a PostgreSQL database, and perform queries using a form-based interface.

## Features

- **User Authentication:** Utilizes django-all-auth for user authentication.
- **Large File Upload:** Implements Django's chunk upload method for handling large CSV file uploads.
- **Data Management:** Processes and stores data in a PostgreSQL database.
- **Dynamic Filtering:** Enables users to query data with a form-based interface featuring dynamic filtering options.
- **UI Design:** Integrates Bootstrap 4 for responsive and modern UI design.

### Prerequisites

- Python 3.x
- Django 3.x/4.x
- PostgreSQL

## Usage
### Login

Log in using your credentials.

### Upload Data

Navigate to the "Upload Data" section and upload a large CSV file
### Query Builder
Use the query builder interface to filter data based on specified criteria. View the count of records that match the applied filters.

### all Users 
shows the list of all users in the database
