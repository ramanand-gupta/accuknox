# README

## Setup and Installation

### Getting Started

1.  **Clone the repository:**
   
    `git clone https://github.com/ramanand-gupta/accuknox`

    `cd accuknox`  

2.  **Build and start the application using Docker Compose:**

    `docker-compose up`


3.  **Access the application:**

- The application will be available at `http://localhost:8989`
  

## API Response Structure
  

### Success Response

For all successful API requests, the response structure will be:

json

    {
	    "status": true,
	    "code": {custom_code},
	    "message": "{custom_message}",
	    "data": {}
    }


-  **status**: Indicates the success of the request (`true`).
-  **code**: A custom code specific to the success type.
-  **message**: A custom message describing the success.
-  **data**: An object containing the data relevant to the request.
  

### Pagination Response

For paginated API responses, the structure will be:

json

	{
		"status": true,
		"code": {custom_code},
		"message": "{custom_message}",
		"data": {
			"count": 0,
			"next": null,
			"previous": null,
			"results": []
		}
	}


-  **status**: Indicates the success of the request (`true`).
-  **code**: A custom code specific to the success type.
-  **message**: A custom message describing the success.
-  **data**: An object containing pagination details:
-  **count**: Total number of items.
-  **next**: URL for the next page of results, if any.
-  **previous**: URL for the previous page of results, if any.
-  **results**: List of results for the current page.


### Error Response

For all failed API requests, the response structure will be:

json

	{
		"status": false,
		"code": {custom_code},
		"message": "{custom_message}",
		"error": {}
	}


-  **status**: Indicates the failure of the request (`false`).
-  **code**: A custom code specific to the error type.
-  **message**: A custom message describing the error.
-  **error**: An object containing the field-specific errors.
  

### General Notes

- For a successful request, `status` will be `true` and HTTP status code `200` will be used.
- For a failed request, `status` will be `false` and HTTP status code `400` will be used.

