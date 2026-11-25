# SkillBridge

SkillBridge is a starter project for a university Level 6 Cloud Computing Development project: a cloud-based career development and opportunity management platform. It is an initial scaffold, not a complete application or a deployed service.

## Technology stack

- **Backend:** Python and FastAPI
- **Frontend:** HTML, CSS and JavaScript
- **Database:** PostgreSQL (connection configuration is prepared; database features are not implemented yet)
- **Cloud hosting target:** Render (deployment is not configured or claimed)
- **API testing:** Pytest; endpoints can also be explored with Postman

## Project structure

```text
backend/
  app/
    api/                 # Placeholder for future route modules
    features/            # Placeholder for application features
    config.py            # Environment-based PostgreSQL configuration
    main.py              # FastAPI application and health check
frontend/
  index.html             # Landing page
  css/styles.css
  js/main.js
tests/
  test_health.py
requirements.txt
```

## Local setup

Python 3.10 or later is recommended.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows, activate it with `.venv\Scripts\activate`.

2. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Optionally set `DATABASE_URL` to a PostgreSQL connection URL. The application reads this setting from the environment; no credentials are included in the repository. For example, configure a value such as `postgresql://<user>:<password>@<host>:<port>/<database>` in your local shell or deployment environment. The starter does not yet open a database connection.

4. Start the API from the repository root:

   ```bash
   uvicorn backend.app.main:app --reload
   ```

   The health check is available at `http://127.0.0.1:8000/api/health`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

5. Open `frontend/index.html` in a browser to view the static landing page.

## Tests and API exploration

Run the API test suite from the repository root:

```bash
pytest
```

To try the health endpoint in Postman, send a `GET` request to `http://127.0.0.1:8000/api/health`. A successful response contains `{"status":"ok"}`.

## Initial architecture and next steps

The FastAPI application currently exposes only a health check. `backend/app/api/` and `backend/app/features/` reserve clear locations for future route modules and application logic. `backend/app/config.py` reads the optional PostgreSQL `DATABASE_URL` environment variable; database models, connection management, authentication, and platform features remain future work.

The frontend is a static landing page and is not yet connected to the API. A future Render deployment can run the API with a start command such as `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT` and set `DATABASE_URL` through the service's environment settings. Deployment and database provisioning are not part of this starter.
